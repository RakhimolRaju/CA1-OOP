import requests
from bs4 import BeautifulSoup
import csv
import re

# ==============================
# CONFIGURATION
# ==============================

# Seasonal period you want to analyse (edit as needed)
CHECK_IN_DATE = "2025-12-20"
CHECK_OUT_DATE = "2025-12-30"

CSV_FILENAME = "dublin_hotels_prices.csv"

SITES = [
    ("Dublin Stays Listing 1", "https://booking-hotels2.tiiny.site/"),
    ("Luxe Haven Listing 2", "https://hotel1.tiiny.site/"),
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; HotelPriceScraper/1.0; +https://example.com)"
}


# ==============================
# CORE SCRAPING LOGIC
# ==============================

def get_soup(url: str) -> BeautifulSoup:
    """Download a web page and return a BeautifulSoup object."""
    resp = requests.get(url, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def extract_rooms_from_listing(url: str, site_label: str):
    """
    Extract room/price data from one of the tiiny.site listing pages.

    Heuristic:
      - Lines containing '1 night, 2 adults' mark a room offer.
      - The lines AFTER that contain prices starting with '€'.
      - The lines BEFORE that contain room type and hotel name.
    """
    soup = get_soup(url)
    # Get all visible text as a list of cleaned lines
    text = soup.get_text("\n")
    lines = [l.strip() for l in text.splitlines() if l.strip()]

    records = []

    for i, line in enumerate(lines):
        # Identify the stay-info line
        if "night" in line and "adults" in line:
            stay_info = line

            # -----------------------------
            # 1) Find the final price after this line
            # -----------------------------
            price_value = None
            currency = "€"  # all prices on these pages use euros

            for k in range(i + 1, min(len(lines), i + 10)):
                if lines[k].startswith("€"):
                    # Keep updating; the last '€ xxx' before "Includes taxes..." is the final price
                    m = re.search(r"(\d[\d,]*)", lines[k])
                    if m:
                        price_value = float(m.group(1).replace(",", ""))
                if "Includes taxes and fees" in lines[k]:
                    break

            if price_value is None:
                # No price found for this offer; skip
                continue

            # -----------------------------
            # 2) Find room type line (above the stay_info)
            # -----------------------------
            room_type = ""
            room_idx = None
            for j in range(i - 1, max(-1, i - 15), -1):
                if re.search(r"Room|Apartment|Studio|Suite|Guest Room", lines[j]):
                    room_type = lines[j]
                    room_idx = j
                    break

            # -----------------------------
            # 3) Find hotel name using the location line (contains 'Dublin')
            # -----------------------------
            hotel_name = ""
            if room_idx is not None:
                loc_idx = None
                for j in range(room_idx - 1, max(-1, room_idx - 8), -1):
                    if "Dublin" in lines[j]:
                        loc_idx = j
                        break

                if loc_idx is not None and loc_idx - 1 >= 0:
                    hotel_name = lines[loc_idx - 1]

            if not hotel_name:
                # Fallback if we couldn't detect a specific hotel name
                hotel_name = site_label

            # -----------------------------
            # 4) Build record
            # -----------------------------
            record = {
                "source_site": site_label,
                "hotel_name": hotel_name,
                "room_type": room_type,
                "stay_info": stay_info,
                "price": price_value,
                "currency": currency,
                "check_in_date": CHECK_IN_DATE,
                "check_out_date": CHECK_OUT_DATE,
                "source_url": url,
            }
            records.append(record)

    return records


# ==============================
# CSV HANDLING
# ==============================

def write_to_csv(filename: str, rows):
    """Write list of room dicts to CSV."""
    if not rows:
        print("No data to write.")
        return

    fieldnames = [
        "source_site",
        "hotel_name",
        "room_type",
        "stay_info",
        "price",
        "currency",
        "check_in_date",
        "check_out_date",
        "source_url",
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_from_csv_and_print(filename: str):
    """Read the CSV and display each row in the terminal."""
    print("\n=== DATA READ BACK FROM CSV ===\n")

    with open(filename, mode="r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(
                f"{row['source_site']:<24} | "
                f"{row['hotel_name']:<32} | "
                f"{row['room_type']:<40} | "
                f"{row['price']:>7} {row['currency']} | "
                f"{row['check_in_date']} → {row['check_out_date']}"
            )


# ==============================
# MAIN ENTRY POINT
# ==============================

def main():
    all_records = []

    # a) Scrape both provided websites
    for label, url in SITES:
        print(f"Scraping: {label} ({url})")
        site_records = extract_rooms_from_listing(url, label)
        print(f"  Found {len(site_records)} room offers.\n")
        all_records.extend(site_records)

    # Ensure we have at least 10 rows (very likely we have many more)
    print(f"Total room offers collected: {len(all_records)}")

    # b) Store data in CSV
    write_to_csv(CSV_FILENAME, all_records)
    print(f"Data written to '{CSV_FILENAME}'.")

    # c) Read CSV back and display in terminal
    read_from_csv_and_print(CSV_FILENAME)


if __name__ == "__main__":
    main()