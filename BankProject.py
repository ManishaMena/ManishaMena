print("="*50)
CustomerNames=['manisha','swathi','laxmi','sandeep','fathima']
CustomerPins=['0123','2575','7257','5684','3748']
CustomerBalance=[10000,2000,4000,50000,2000]
deposition=0
withdrawal=0
balance=0
Counter_1=1
Counter_2=5
i=0
# for continues program running we use while 
while True:
    print("="*50)
    print("------Welcome to uni Bank")
    print("*"*50)
    print("=<< 1.Open a new account           >>=")
    print("=<< 2.Withdraw Money               >>=")
    print("=<< 3.Deposite Money               >>=")
    print("=<< 4.Check Customer & Balance     >>=")
    print("=<< 5.Exit /Quit                   >>=")
    print("*"*50)
   # take the option from the user 
    choiceNumber= input("Select your choice number from the above list:")
    if choiceNumber=="1":
        print("Choice number is selected by the customer")
        # the line below will take the no.of customer from the user
        NOC=eval(input("Number of customer:"))
        i=i+NOC
        # the if condition restrict the no.of new account to 5
        if i>5:
            print("\n")
            print("Customer registration exceed reached or Customer registration too low")
            i=i-NOC
        else:
            # .the while loop run according to the no.of customers
            while Counter_1 <=i:
                # take the information from the customer details and append to the list
                name=input("Enter Full Name:")
                CustomerNames.append(name)
                pin=str(input("please input a pin  of your choice:"))
                CustomerPins.append(pin)
                balance=0
                deposition=eval(input("please input a value to deposite to start to account:"))
                balance=balance+deposition
                CustomerBalance.append(balance)
                print("\nName=",end="")
                print(CustomerNames[Counter_2])
                print("Pin=",end="")
                print(CustomerPins[Counter_2])
                print("Balance=",end="")
                print(CustomerBalance[Counter_2],end="")
                print("-/Rs")
                Counter_1=Counter_1+1
                Counter_2=Counter_2+1
                print("Your  name is added to customer system")
                print("Your pin is added to customer system")
                print("your balance is added to customer system")
                print("-----New Account Created Sucessfully!-------")
                print("/n")
                print("Your name is avaliable in the customer list now:")
                print(CustomerNames)
                print("\n")
                print("Note! please Remeber the Name and Pin")
                print("="*50) 
                # this statment help the user to go the main menu to perform the furthur process or exit
        mainMenu=input("please press enter key to go back to main to perform furhter function or exit")
    elif choiceNumber=="2":
        j=0
        print("choice number 2 is selected by the customer")
        # this loop will help prevent the user using the account if username or pin wrong.
        while j<1:
            k=-1
            name=input("Enter name:")
            pin=input("Enter your pin:")
            # this while loop will keep the function running when variable k is smaller than length of the customername list
            while k<len(CustomerNames)-1:
                k=k+1
                # check the name and pin or match or not
                if name==CustomerNames[k]:
                    if pin==CustomerPins[k]:
                        j=j+1
                        # this is statement show the balance taken from the list
                        print("Your current Balance:",end="")
                        print(CustomerBalance[k])
                        
                        print("-/Rs\n")
                        balance=(CustomerBalance[k])
                        # withdraw the amount
                        withdrawal=eval(input("enter the Withdraw amount:"))
                        # the below condition check the withdraw amount is greater than the balance amount or not
                        if withdrawal>balance:
                            deposition=eval(input("please deposite higher value beacuse your balance is insuffient to draw"))
                            # update the balance
                            balance=balance+deposition
                            print("your current balance",end="")
                            print(balance,end="")
                            print("-/Rs\n")
                            
                            balance=balance-withdrawal
                            print("-\n")
                            print("---Withdraw Sucessfull!---")
                            CustomerBalance[k]=balance
                            print("your New Balance:",balance,end="")
                        else:
                            # if balance is greater than the withdraw amount
                            balance=balance-withdrawal
                            print("-----Withdraw Sucessfull!----")
                            CustomerBalance[k]=balance
                            print("Your New balance:",balance,end="")
                            print("-/Rs\n")
                               
                if j<1:
                    # .pin and name are wrong
                    print("Your Name and pin doesn't match!\n")
                    break
        mainMenu=input("please press enter key to go back to the main menu to perfoem another function or exit...")
    elif choiceNumber=="3":
        print("choice number 3 is selected by customer:")
        n=0
        # the while loop work when pin and username is wrong
        while n<1:
            name=input("Enter username:")
            pin=input("Enter pin:")
            k=-1
            # the below while loop check the correct user and pin
            while k<len(CustomerNames) -1:
                k=k+1
                # checking the condition using the if condition
                if name==CustomerNames[k] and  pin==CustomerPins[k]:
                    
                        n=n+1
                        # update the customer balance and update list values according to deposition made
                        print("Your Current Balance:",end="")
                        print(CustomerBalance[k],end="")
                        print("-/Rs\n")
                        balance=(CustomerBalance[k])
                        # taking the amount from the user
                        deposition=eval(input("enter Deposite amount:"))
                        balance=balance+deposition
                        CustomerBalance[k]=balance
                        print("\n")
                        print("----Deposition Sucessfull!-----")
                        print("your New Balance:",balance,end="")
                        print("-/Rs\n")
                if n<1:
                    print("your Name and pin doesn't match\n")
                    break
        mainMenu=input("Please press enter key to go back to main menu to perform another function or exit...")
    elif choiceNumber=="4":
        print("choice number 4 is selected by the customer")
        k=0
        print("Customer naem list and balance mentioned below:")
        print("\n")
        # the loop below running untill the customer and balnce are shown
        while k<=len(CustomerNames)-1:
            print("->.Customer=",CustomerNames[k])
            print("->.Balance =",CustomerBalance[k])
            print("-/Rs")
            print("\n")
            k=k+1
            
        mainMenu=input("please press enter key to go back to main menu to perfoem another function or exit...")
    elif choiceNumber=="5":
        #   these statement would be just showed to the customer.
        print("Choice number 5 selected by the customer")
        print("Thank you for using our banking system")
        print("\n")
        print("Come Again")
        print("Bye Bye")
        break
    else:
        # this shows the wrong function is chosen
        print("Invalid option selected by the customer")
        print("Please Try Again")
        mainMenu=input("please enter key to go back to main menu to perform another function or exit....")
                            
                
                        
        
                               
        