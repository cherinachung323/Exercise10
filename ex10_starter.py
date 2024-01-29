import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    hdir = os.environ['HOMEPATH']
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir,'*')

# Step 5: Use the glob.glob() function to obtain the list of filenames
file_list = glob.glob(pattern)

# Step 6: Use os.path.getsize() to find each file's size
# Step 7: Add a test to only display files that are not zero length
# I am using a for statement here to check every single file in my file_list
for file_name in file_list:
    if os.path.getsize(file_name) != 0:
        # Step 8: Use os.path.basename() to remove the leading directory name(s)
        file_name = os.path.basename(file_name)
        print(file_name)

# Hard-coded password
# I set the correct pin by passing the value 1234 to correct_pin
correct_pin = "1234"

# Set maximum number of attempts to 3,I will compare the attempt value with this max number.
max_attempts = 3

# Initialize attempt counter
attempts = 0

# Loop to take input and check PIN
while attempts < max_attempts:
    # Prompt for PIN input
    entered_pin = input("Enter your PIN: ")

    # Check if entered PIN matches correct PIN
    if entered_pin == correct_pin:
        print("Success! PIN accepted.")
        break  # Exit loop on success
    else:
        attempts = attempts + 1
        remaining_attempts = max_attempts - attempts
        print("Incorrect PIN. Please try again. Attempts remaining:", remaining_attempts)

# Check if maximum attempts reached, if it is attempt 3 then show this following message
if attempts == max_attempts:
    print("You have exceeded the maximum number of attempts. Access denied.")
