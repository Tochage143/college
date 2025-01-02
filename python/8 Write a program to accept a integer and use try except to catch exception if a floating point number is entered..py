try:
    user_input = input("Enter an integer: ")
    number = int(user_input)
    print(f"You entered the integer: {number}")
except ValueError:
    print("Error: You must enter a valid integer. A floating point number was entered.")
