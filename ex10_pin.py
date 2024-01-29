import getpass

# Correct PIN
correct_pin = "1278"

# Maximum number of attempts
max_attempts = 3

for attempt in range(max_attempts):
    # Ask the user to supply the PIN
    supplied_pin = input("Please enter your PIN: ")

    # Check if the supplied PIN matches the correct PIN
    if supplied_pin == correct_pin:
        print("PIN verification successful")
        break
    else:
        attempts_remaining = max_attempts - attempt - 1
        if attempts_remaining > 0:
            print(f"Incorrect PIN. {attempts_remaining} attempts remaining.")
        else:
            print("No remaining attempts. Access denied.")



