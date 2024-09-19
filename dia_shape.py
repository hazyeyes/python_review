def int_input():
    # Function to get an odd integer input from the user.
    try:
        inp = int(input("Please enter an odd number: "))  # Prompt for an integer input
    except ValueError:
        # Handle case where input is not a valid integer
        print("Please enter an integer")
        print("--------------------------")
        print("")
        main()  # Restart the main function if input is invalid
    return inp  # Return the valid integer input

def additional():
    # Function to ask the user if they want to run the program again.
    ask_user = input("Do you want to convert again? (y/n): ")
    if ask_user.lower() == "y":
        print("______________________")
        print()
        main()  # Restart main function if the user wants to continue
    elif ask_user.lower() == "n":
        quit()  # Exit the program if the user does not want to continue
    else:
        print("Enter \"y\" or \"n\".")  # Prompt for valid input
        additional()  # Repeat the prompt if input is invalid

def main():
    # Main function to print a diamond shape based on user input.
    print("Print a Diamond.")    
    print("----------------")

    user_input = int_input()  # Get user input for the diamond size
    if (user_input % 2) != 0:  # Check if the input is an odd number
        # Print the upper part of the diamond
        for i in range(user_input):
            print(" " * (user_input - i - 1) + "*" * (2 * i + 1))  # Center and print stars
        # Print the lower part of the diamond
        for i in range(user_input - 2, -1, -1):
            print(" " * (user_input - i - 1) + "*" * (2 * i + 1))  # Center and print stars
        additional()  # Ask if the user wants to print another diamond
    else:
        print("Please enter an odd integer.")  # Handle case where input is not odd
        print("--------------------------")
        print("")
        main()  # Restart main function

# Start the program by calling main()
main()