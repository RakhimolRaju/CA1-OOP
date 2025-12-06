using System;
using System.ComponentModel;
using System.Runtime.ExceptionServices;
using System.Runtime.InteropServices;
using System.Transactions;
public class PhoneContact
 {
    public string[] firstname = new string[20];
    public string[] lastname = new string[20];
    public string[] Company = new string[20];
    public long[] phonenumber = new long[20];
    public string[] Email = new string[20];
    public DateTime[] Birthdate = new DateTime[20];


    public int i = 0;

    public void addContact()
    {
       Console.WriteLine("Enter the firstname");
       firstname[i] = Console.ReadLine();
       Console.WriteLine("Enter the lastname");
       lastname[i] = Console.ReadLine();
       Console.WriteLine("Enter the Phone number");
       phonenumber[i] = long.Parse(Console.ReadLine());
       Console.WriteLine("Enter the Company");
       Company[i] = Console.ReadLine();
       Console.WriteLine("Enter the Email");
       Email[i] = Console.ReadLine();
       Console.WriteLine("Enter the Birthdate");
       Birthdate[i] = DateTime.Parse(Console.ReadLine());
       i++;
       

    }
    public void DisplayContact()
    {   
      Console.WriteLine("\nDisplayng Contacts");
      Console.WriteLine("------------------");
        for (int k =0 ; k<i; k++)
        { 

          Console.WriteLine($"\n CONTACTS \n {k+1}. \t{firstname[k]}");
        }
    }
    public void DisplayDetails()
    { 
            for (int j = 0; j<i; j++)
            {
               Console.WriteLine($"\nContact {j+1}:\n First Name : {firstname[j]}\n Last name :  {lastname[j]}\n Phone Number :{phonenumber[j]}\n Company : {Company[j]}\n Email : {Email[j]}\n Date of Birth : {Birthdate[j]}");
            }
      
    }
    public void update()
    {
      if (i<0)
        {
            Console.WriteLine("No contacts in the List");
            return;

        }
        Console.WriteLine("Enter which contacts to be updated \n Select 1 to {0}",i);
        int m = int.Parse(Console.ReadLine());
        m = m-1;
        
      
      if (m<0 || m>i)
        {
         Console.WriteLine("Invalid");

        } 

        Console.WriteLine("\n Which data to be updated");
        Console.WriteLine("\n 1. First Name");
        Console.WriteLine("\n 2. Last Name");
        Console.WriteLine("\n 3. Phone Number");
        Console.WriteLine("\n 4. Company");
        Console.WriteLine("\n 5. Email");
        Console.WriteLine("\n 6. Date of Birth");

        Console.WriteLine("\n Enter Your Choice");
        int choice = int.Parse(Console.ReadLine());

        switch(choice)
        {
            case 1: 
            Console.WriteLine("Enter the new First Name");
            firstname[m]= Console.ReadLine();
            break;
            case 2:
            Console.WriteLine("Enter the new Last Name");
            lastname[m]= Console.ReadLine();
            break;
            case 3:
            Console.WriteLine("Enter the new Phone number");
            phonenumber[m]= long.Parse(Console.ReadLine());
            break;
            case 4:
            Console.WriteLine("Enter the new Company");
            Company[m]= Console.ReadLine();
            break;
            case 5:
            Console.WriteLine("Enter the new Last Email");
            Email[m]= Console.ReadLine();
            break;
            case 6:
            Console.WriteLine("Enter the new Date Of Birth");
            Birthdate[m]= DateTime.Parse(Console.ReadLine());
            break;


        }


    }
    public void Delete()
        {
          Console.WriteLine("Which Contact to be deleted");
          Console.WriteLine("-----------------------------");
          Console.WriteLine("Enter the Number from 1-{0}",i);
          int input = int.Parse(Console.ReadLine());
          Console.WriteLine("Deleting the contact number {0}",input);
          input = input-1;
    
          for (i=input; i<input;i++)
        {
            firstname[i]= firstname[i+1];
            lastname[i] = lastname[i+1];
            phonenumber[i]=phonenumber[i+1];
            Company[i] = Company[i+1];
            Email[i] = Email[i+1];
            Birthdate[i]= Birthdate[i+1];

        }  
        }
 }
 