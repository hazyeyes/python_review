def user_inp():
    # Function to get user input for the desired calculation (Voltage, Current, or Resistance).
    comp = {"V", "I", "R"}  # Set of valid options
    user_input = input("What do you want to solve?\n(\"V\" for Voltage | \"I\" for Current | \"R\" for Resistance)\n: ")
    user_input = user_input.upper()  # Convert input to uppercase for consistency

    # Check if the user input is valid
    if user_input not in comp:
        print("Please enter a valid value.")
        print("--------------------------")
        print("")
        main()  # Restart main function if input is invalid
    
    return user_input  # Return the valid user input

def multiply(x, y):
    # Function to multiply two numbers.
    answer = x * y
    return answer  # Return the multiplication result

def divide(x, y):
    # Function to divide two numbers, ensuring the divisor is not zero.
    if y != 0:         
        answer = x / y
        return answer  # Return the division result
    else:
        print(f"Please enter a valid given")
        print("--------------------------")
        print("")
        main()  # Restart main function if division by zero occurs

def additional():
    # Function to ask the user if they want to perform another calculation.
    ask_user = input("Do you want to convert again? (y/n): ")
    if ask_user.lower() == "y":
        print("______________________")
        print()
        main()  # Restart main function if the user wants to continue
    elif ask_user.lower() == "n":
        quit()  # Exit the program if the user does not want to continue
    else:
        print("Enter \"y\" or \"n\".")
        additional()  # Repeat the prompt if input is invalid

def main():
    # Main function to run the Ohm's Law Calculator.
    print("Ohm's Law Calculator")
    print("     / \\     ")
    print("    / V \\    ")
    print("   /-----\\   ")
    print("  / I | R \\  ")
    print(" ----------- ")

    user_input = user_inp()  # Get the user's choice of calculation

    # Calculate Voltage (V = I * R)
    if user_input == "V":
        print("Enter the necessary values")
        current = float(input("Current (I): "))  # Get current from the user
        resistance = float(input("Resistance (R): "))  # Get resistance from the user
        result = "{:.2f}".format(multiply(current, resistance))  # Calculate voltage
        print("--------------------------")
        print("The Voltage is ", result, f"Volts \n(Current: {current} Amperes, Resistance: {resistance} Ohms)")
        additional()  # Ask if the user wants to calculate again

    # Calculate Current (I = V / R)
    elif user_input == "I":
        print("Enter the necessary values")
        voltage = float(input("Voltage (V): "))  # Get voltage from the user
        resistance = float(input("Resistance (R): "))  # Get resistance from the user
        result = "{:.2f}".format(divide(voltage, resistance))  # Calculate current
        print("--------------------------")
        print("The Current is ", result, f"Amperes \n(Voltage: {voltage} Volts, Resistance: {resistance} Ohms)")  
        additional()  # Ask if the user wants to calculate again

    # Calculate Resistance (R = V / I)
    elif user_input == "R":
        print("Enter the necessary values")
        voltage = float(input("Voltage (V): "))  # Get voltage from the user
        current = float(input("Current (I): "))  # Get current from the user
        result = "{:.2f}".format(divide(voltage, current))  # Calculate resistance
        print("--------------------------")
        print("The Resistance is ", result, f"Ohms \n(Voltage {voltage} Volts, Current: {current} Amperes)")  
        additional()  # Ask if the user wants to calculate again
    else:
        print("Please enter a valid value.")
        main()  # Restart main function if input is invalid

# Start the program by calling main()
main()