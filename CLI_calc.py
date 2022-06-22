#taking input
operations = ['Addition', 'Subtraction', 'Division', 'Multliplication', 'Modulus'] 
choice = input("\nWhich Operation do you wish to carry out?['Addition', 'Subtraction', 'Division', 'Multliplication', 'Modulus'] \n")

#CHECKING IF CHOICE IS ONE OF THE FIVE OPTIONS
if choice in operations:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    #conditions for each operation
    if choice == "Addition":
        result = num1+ num2

    elif choice == "Subtraction":
        result = int(num1) - int(num2)
    elif choice == "Division":
       result = int(num1) / int(num2)
    elif choice == "Multliplition":
        result = int(num1) * int(num2)
    elif choice == "Modulus":
       result = int(num1) % int(num2)
       
    print("Your answer is: ",result)

else: print("Invalid Input! Sorry, Input one of the operation above!")   