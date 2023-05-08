#Name : Logie A. Mendiola | BSCPE 1-5 | Object Oriented Programming | Assignment #5

#Creating a Simple App Calculator:
# 1.  The application will ask the user to choose one of the 
#     four math operations (Addition, Subtraction, Multiplication and Division)
# 2.  The application will ask the user for two numbers
# 3.  Display the result
# 4. The application will ask if the user wants to try again or not.
# 5. If yes, repeat Step 1.
# 6. If no, Display “Thank you!” and the program will exit 
# 7. Use Python Function and appropriate Exceptions to capture errors during   
#    runtime

def operation():
    print("\nPlease choose among the math operation you would like to try")
    print("\nOPERATION I: ADDITION \nOPERATION II: SUBTRACTION \nOPERATION III: MULTIPLICATION \nOPERATION IV: DIVISION")
    operation_decision = int(input("\n\nPlease type in the following to choose: \n'1' - ADDITION \n'2' - SUBTRACTION \n'3' - MULTIPLICATION \n'4' - DIVISION \nYour choice is: "))

    if operation_decision == 1:
        print("C O M M E N C I N G . . . . .  A D D I T I O N  O P E R A T I O N . . . . .")
        first_digit = float(input("Please enter a digit as your first number: "))
        second_digit = float(input("Please enter a digit as your second number: "))
        add_computation = first_digit + second_digit
        print("The answer is:",add_computation)
    
    elif operation_decision == 2:
        print("C O M M E N C I N G . . . . .  S U B T R A C T I O N  O P E R A T I O N . . . . .")
        first_digit = float(input("Please enter a digit as your first number: "))
        second_digit = float(input("Please enter a digit as your second number: "))
        minus_computation = first_digit - second_digit
        print("The answer is:",minus_computation)
    
    elif operation_decision == 3:
        print("C O M M E N C I N G . . . . .  M U L T I P L I C A T I O N  O P E R A T I O N . . . . .")
        first_digit = float(input("Please enter a digit as your first number: "))
        second_digit = float(input("Please enter a digit as your second number: "))
        multiply_computation = first_digit * second_digit
        print("The answer is:",multiply_computation)
    
    elif operation_decision == 4:
        print("C O M M E N C I N G . . . . .  D I V I S I O N  O P E R A T I O N . . . . .")
        first_digit = float(input("Please enter a digit as your first number: "))
        second_digit = float(input("Please enter a digit as your second number: "))
        divide_computation = first_digit / second_digit
        print("The answer is:",divide_computation)

    else:
        print("")

operation()
