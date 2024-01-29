# Optional - hide the characters you type
import getpass
# Correct PIN
correct_pin = "1278"

# Maximum number of attempts
max_attempts = 3

for attempt in range(max_attempts):
    # Ask the user to supply the PIN
    # Instead of using input, getpass.getpass is part of Python library module that hides sensitive information
    supplied_pin = getpass.getpass("Please enter your PIN: ")

    # Check if the supplied PIN matches the correct PIN
    # Added one more if statement if the attempt is less than max_attempt
    # This if statement will print a warning if supplied_pin is not equal to 4
    if len(supplied_pin) != 4:
        print("Please enter a valid 4-digit number.")

    if supplied_pin == correct_pin:
        print("PIN verification successful")
        break
    else:
        attempts_remaining = max_attempts - attempt - 1
        if attempts_remaining > 0:
            print(f"Incorrect PIN. {attempts_remaining} attempts remaining.")
        else:
            print("No remaining attempts. Access denied.")




