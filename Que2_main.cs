public class MainClass
{
    public static void Main(string[] args)
    {
        Extensions ext = new Extensions();
        
        while (true)
        {
           

            Console.WriteLine("1. Check Extension");
            Console.WriteLine("2. Exit");
            Console.WriteLine("Select an option:");
            string choice = Console.ReadLine();

            switch(choice)
            {
                case "1":
                    Console.WriteLine("Enter a file extension (e.g., .mp3, .pdf):");
                    string inputExtension = Console.ReadLine();
                     if (!inputExtension.StartsWith("."))
                     {
                       Console.WriteLine("Please enter a valid file extension starting with a dot (e.g., .mp3, .pdf):");
                       inputExtension = Console.ReadLine();
                     }
                     else
                    {
                     break;
                    }
                     ext.ShowFileType(inputExtension);
                    break;

                case "2":
                
                    return;
                default:
                    Console.WriteLine("Invalid option. Please try again.");
                    break;
            }
           
        }
       
    }
}