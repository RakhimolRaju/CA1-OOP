using System.Collections;
using System.Diagnostics;

public class Mainclass
{
    public static void Main()

    {   
        PhoneContact a = new PhoneContact();
        bool running = true;

        while (running)
      {
        
        Console.WriteLine("\nMain Menu");
        Console.WriteLine("\n1. Add Contact");
        Console.WriteLine("\n2. Show all Contacts");
        Console.WriteLine("\n3. Show Contactt Details");
        Console.WriteLine("\n4. Update Contact ");
        Console.WriteLine("\n5. Delete Contact");
        Console.WriteLine("\n6. Exit");
        int selection = int.Parse(Console.ReadLine());
        
     

       switch(selection)
        {
            case 1:
            a.addContact();
            break;

            case 2:
            a.DisplayContact();
            break;

            case 3:
            a.DisplayDetails();
            break;

            case 4:
            a.update();
            break;

            case 5:
            a.Delete();
            break;

            case 6:
            running = false;
            Console.WriteLine("Exiting..");
            break;

            default:
            Console.WriteLine("Please Select Valid Option");
            break;
        }
        }


       
    }
}