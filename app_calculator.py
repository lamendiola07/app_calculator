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

import pyfiglet
from simple_colors import *
from pyfiglet import figlet_format

import datetime

def operation():

    print(red("\nHere are the Mathematical Operations to be utilized in this program ~", ['italic','underlined']))
    print(blue("\nOPERATION I: ADDITION", ['bold']))
    print(green("\nOPERATION II: SUBTRACTION", ['bold']))
    print(yellow("\nOPERATION III: MULTIPLICATION", ['bold']))
    print(magenta("\nOPERATION IV: DIVISION", ['bold']))

    operation_decision = int(input("\n\nPlease type in the following to choose: \n'1' - ADDITION \n'2' - SUBTRACTION \n'3' - MULTIPLICATION \n'4' - DIVISION \nYour choice is: "))


    if operation_decision == 1:
        try:
            print(green("\nC O M M E N C I N G . . . . .  A D D I T I O N  O P E R A T I O N . . . . ."))
            first_digit = float(input("Please enter a digit as your first number: "))
            second_digit = float(input("Please enter a digit as your second number: "))
            add_computation = first_digit + second_digit
            print("The answer is:",add_computation)
        except:
            print(red("\nAn error occured"))
        else:
            print(yellow("\nNo error has occured"))
        finally:
            print(green("Program is finished"))

    

    elif operation_decision == 2:
        try:
            print(green("\nC O M M E N C I N G . . . . .  S U B T R A C T I O N  O P E R A T I O N . . . . ."))
            first_digit = float(input("Please enter a digit as your first number: "))
            second_digit = float(input("Please enter a digit as your second number: "))
            minus_computation = first_digit - second_digit
            print("The answer is:",minus_computation)
        except:
            print(red("\nAn error occured"))
        else:
            print(yellow("\nNo error has occured"))
        finally:
            print(green("Program is finished"))


    elif operation_decision == 3:
        try:
            print(green("\nC O M M E N C I N G . . . . .  M U L T I P L I C A T I O N  O P E R A T I O N . . . . ."))
            first_digit = float(input("Please enter a digit as your first number: "))
            second_digit = float(input("Please enter a digit as your second number: "))
            multiply_computation = first_digit * second_digit
            print("The answer is:",multiply_computation)
        except:
            print(red("\nAn error occured"))
        else:
            print(yellow("\nNo error has occured"))
        finally:
            print(green("Program is finished"))

    
    elif operation_decision == 4:
        try:
            print("\nC O M M E N C I N G . . . . .  D I V I S I O N  O P E R A T I O N . . . . .")
            first_digit = float(input("Please enter a digit as your first number: "))
            second_digit = float(input("Please enter a digit as your second number: "))
            divide_computation = first_digit / second_digit
            print("The answer is:",divide_computation)
        except:
            print(red("\nAn error occured"))
        else:
            print(yellow("\nNo error has occured"))
        finally:
            print(green("Program is finished"))

    else:
        print("")

date_and_time = datetime.datetime(2023, 5, 8, 7, 2)
print("\n\nTime created:")
print(date_and_time)

print("\n\nGreetings User! Welcome back to another program simulation in Object Oriented Programming!")
print("\nIn this program, we will ask you to choose from one of the four math operations, by asking for two digits")
print("\nwhile also being able to repeat the program and keeping and capturing errors during our runtime")
print("\nNow let's get started.\n")

operation()

while True:
    repeat_operation = input("\nWould you like to repeat the program? \nPlease type 'Y' for Yes or 'N' for No: ")
    if repeat_operation == "Y":
        print(magenta("\n- - - - - - - - - - - - - - - R E S T A R T I N G      P R O G R A M     S E Q U E N C E - - - - - - - - - - - - - - - - - - - - -", ['bold']))
        operation()
    
    else:
        print(yellow("\n\nThank you for participating with us, the program will now exit."))
        print("      ╱|、")
        print("     (˚u 。7  ")
        print("      |、˜〵")         
        print("      じしˍ,)ノ")
        break