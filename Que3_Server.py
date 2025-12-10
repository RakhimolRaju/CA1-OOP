import socket
import sqlite3
import threading
import json
from datetime import datetime

host = "127.0.0.1"
port = 9999
db_path = 'application.db'

def database_setup():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS application (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            address TEXT NOT NULL,
            qualification TEXT NOT NULL,
            course TEXT NOT NULL,
            start_year INTEGER NOT NULL,
            start_month INTEGER NOT NULL,
            reg_number TEXT unique ,
            reg_date TEXT NOT NULL
                   
        )
    ''')
    conn.commit()
    conn.close()

def registration_number_generator(start_year : int, application_Id: int) -> str:    
    return f"DBS{start_year}{application_Id:04d}"

def save_application(data : dict) -> str:
  fields =[   
     "firstname","lastname","address","qualification","course","start_year","start_month"
  ]

  for field in fields:
     if field not in data:
        return f"Error: Missing field {field}"
  firstname = data['firstname']
  lastname = data['lastname']
  address = data['address']   
  qualification = data['qualification']
  course = data['course']
  start_year = data['start_year']
  start_month = data['start_month']
        

     
  if not (1<= start_month <= 12):
        raise ValueError("Error: start_month must be between 1 and 12")
  
  if not (firstname and lastname and address and qualification and course):
        raise ValueError("Error: String fields cannot be empty")
  
  conn = sqlite3.connect(db_path)
  cur = conn.cursor()
  cur.execute("""
    INSERT INTO application (firstname, lastname, address, qualification, course, start_year, start_month, reg_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?) 
            """,(firstname, lastname, address, qualification, course, start_year, start_month, datetime.utcnow().isoformat()),
            )
  application_id = cur.lastrowid
  reg_number = registration_number_generator(start_year, application_id)
  cur.execute('''
            UPDATE application
                    SET reg_number = ?
                    WHERE id = ?
            ''', (reg_number, application_id))


  conn.commit()   
  conn.close()
  return f"Success: Application saved with registration number {reg_number}"

    
def handle_client_connection(client_socket,addr):
    try:
       print (f"Connction from the {addr} has been established!")
       chunks = []
       
       while True:
           chunk = client_socket.recv(4096)
           if not chunk:
               break
           chunks.append(chunk)

       if not chunks:
           print (f'No data received from {addr}')
           return
       
       raw_data = b''.join(chunks)
       data_str = raw_data.decode('utf-8')
       print (f"Received data: {data_str} from {addr}")

       try:
            payload = json.loads(data_str)
       except json.JSONDecodeError:
            response = "Error: Invalid JSON format"
            client_socket.sendall(response.encode('utf-8'))
            client_socket.close()
            return
       try:
            reg_number = save_application(payload)
            response = f"Success: Application saved with registration number {reg_number}"  
       except Exception as e:
            response = f"Error: {str(e)}"
       client_socket.sendall(json.dumps(response).encode('utf-8'))
                            
    finally:
            client_socket.close()
            print (f"Connection from {addr} closed.")
    
    
def start_server():

    database_setup()
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print (f"Server listening on {host}:{port}")

    
    while True:
        client_socket, addr = server.accept()
        client_handler = threading.Thread(
            target=handle_client_connection,
            args=(client_socket,addr)
        )
        client_handler.start()
if __name__ == "__main__":
    start_server()
       

       



