def ask_temperature():
    # Prompt the user to enter a temperature and handle invalid input.
    try:
        temperature = float(input("Enter the temperature: "))  # Get temperature input from the user
    except ValueError:
        # Handle case where input is not a valid float
        print("Please enter an integer...")
        print("--------------------------")
        print()
        main()  # Restart the main function if input is invalid
    return temperature  # Return the valid temperature

def additional():
    # Ask the user if they want to convert another temperature.
    ask_user = input("Do you want to convert again? (y/n): ")  # Prompt for continuation
    if ask_user.lower() == "y":
        print("______________________")
        print()
        main()  # Restart the main function if the user wants to convert again
    elif ask_user.lower() == "n":
        quit()  # Exit the program if the user does not want to convert again
    else:
        # Handle case where input is neither 'y' nor 'n'
        print("Enter \"y\" or \"n\".")
        additional()  # Repeat the prompt

def main():
    # Main function to run the temperature conversion program.
    print("Temperature Converter")
    print("")
    temperature = ask_temperature()  # Get temperature input
    conversion_type = input("Select the conversion type \nA. Celsius to Fahrenheit \nB. Fahrenheit to Celsius \n(\"A\" or \"B\"): ")

    # Handle Celsius to Fahrenheit conversion
    if conversion_type.upper() == "A":
        temperature = "{:.2f}".format((temperature * (9/5)) + 32)  # Convert Celsius to Fahrenheit
        print("----------------------")
        print("Temperature: ", temperature, u"\u2109")  # Display temperature in Fahrenheit
        additional()  # Ask if the user wants to convert again

    # Handle Fahrenheit to Celsius conversion
    elif conversion_type.upper() == "B":
        temperature = "{:.2f}".format((temperature - 32) * (5/9))  # Convert Fahrenheit to Celsius
        print("----------------------")
        print("Temperature: ", temperature, u"\u2103")  # Display temperature in Celsius
        additional()  # Ask if the user wants to convert again

    else:
        # Handle case where conversion type input is invalid
        print("Please enter a valid input: ")
        print("----------------------------")
        print()
        main()  # Restart the main function

# Start the program by calling main()
main()