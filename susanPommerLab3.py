###########################################################
# Course:  CS 21A Python Programming: Lab #3
# Name:  Susan Pommer
# Description:  Loops and Functions
#   Request a password
#   Request to re-enter a password
#   Confirm both entries match
#   Validate that password meets defined criteria
#
#  File name:  SusanPommerLab3.py
# Date:  July 23, 2017
###########################################################

# Define password requirements as constants
# So can easily be changed if requirements change
MIN_LENGTH = 8
MIN_NUMBER_DIGITS = 1
MIN_NUMBER_LOWERCASE = 1
MIN_NUMBER_UPPERCASE = 1

# Define Main Program ##
def main():
# Set defaults for loop variables
    meet_length_criteria = 'n'
    meet_uppercase_criteria = 'n'
    meet_lowercase_criteria = 'n'
    meet_digit_criteria = 'n'

# Outer loop:
# Continue to:
# * ask user to input password (2x)
# * check if password meets requirements

    while meet_length_criteria == 'n' or meet_uppercase_criteria == 'n' \
    or meet_lowercase_criteria == 'n' or meet_digit_criteria =='n':

        # Inner Loop 1:  request and validate user input
        # * Display password rules
        # * Request user input of password (2x)
        # * Compare 1st and 2nd password strings
        # * Continue or error message and reloop

        # Create a variable to control the loop
        match = 'n'

        while match == 'n':
            # Display password rules
            password_rules()

            # Prompt user for 1st password input
            password_1 = password_input_1()
            
            # Prompt user for 2nd password input
            password_2 = password_input_2()

            # Compare password strings 
            match = compare_strings(password_1, password_2)

            # Issue error message
            if match == 'n':
                password_match_error()   


        # Inner Loop 2:  Validate password meets required criteria

        # Check password for requirements
        # Note:  only have to check password_1
        #   as have already validated password match
        meet_length_criteria = check_password_length(password_1)
        meet_uppercase_criteria = check_password_uppercase(password_1)
        meet_lowercase_criteria = check_password_lowercase(password_1)
        meet_digit_criteria = check_password_digit(password_1)

        # Loop:  Check if password meets all requirements
        # Provide user confirmation or error message and reloop
        if meet_length_criteria == 'y' and meet_uppercase_criteria == 'y' \
        and meet_lowercase_criteria == 'y' and meet_digit_criteria =='y':
            password_criteria_confirmation()
        else:
            password_criteria_error()

###-----

# Functions
# Function:  Display password rules to user
def password_rules(): 
    print("\nYour password must meet these requirements: ")
    print("* must be at least", MIN_LENGTH, "characters long ")
    print("* must have at least", MIN_NUMBER_LOWERCASE, "lowercase letter ")
    print("* must have at least", MIN_NUMBER_UPPERCASE, "uppercase letter ")
    print("* must have at least", MIN_NUMBER_DIGITS, "digit \n")

# Function:  Prompt user for 1st password input
def password_input_1():
    password = input("Enter your password: ")
    return password

# Function:  Prompt user for 2nd password input
def password_input_2(): 
    password = input("Re-enter your password: ")
    return password

# Function:  Print password input error message
def password_match_error(): 
    print ("\nYour passwords did not match; please try again.")

# Function:  Compare password 1 and password 2
def compare_strings(password_1, password_2): 
    if password_1 == password_2:
        match = 'y'
    else:
        match = 'n'
    return match

# Function:  Check password for length
def check_password_length(password):
    if len(password) >= MIN_LENGTH:
        meet_length_criteria = 'y'
    else:
        meet_length_criteria = 'n'
    return meet_length_criteria
        
# Function:  Check password for uppercase letters
def check_password_uppercase(password):
    #Initialize counter
    count = 0 

    # Check for uppercase letters
    for char in password: 
        if char.isupper() == True:
            count +=1
            
    # Check uppercase letter criteria
    if count >= MIN_NUMBER_UPPERCASE:
        meet_uppercase_criteria = 'y'
    else:
        meet_uppercase_criteria = 'n'
    return meet_uppercase_criteria

# Function:  Check password for lowercase letter
def check_password_lowercase(password):
    #Initialize counter
    count = 0 

    # Check for lowercase letters
    for char in password:
        if char.islower() == True:
            count += 1
            
    # Check lowercase letter criteria
    if count >= MIN_NUMBER_LOWERCASE:
        meet_lowercase_criteria = 'y'
    else:
        meet_lowercase_criteria = 'n'
    return meet_lowercase_criteria

# Function:  Check password for digits
def check_password_digit(password):
    #Initialize counter
    count = 0 

    # Check for digits
    for char in password:
        if char.isdigit() == True:
            count += 1
            
    # Check digit letter criteria
    if count >= MIN_NUMBER_DIGITS:
        meet_digit_criteria = 'y'
    else:
        meet_digit_criteria = 'n'
    return meet_digit_criteria

# Function:  Print password error message - requirements
def password_criteria_error(): 
    print ("\nYour password did not meet requirements.")

# Function:  Print password confirmation message - requirements
def password_criteria_confirmation(): 
    print ("\nThat pair of passwords will work!")


# Call Main function
main()


##################### SAMPLE RUNS #########################
#>>> 
# RESTART: C:/Pommer Files/CLASSES/FHC CS21A/Assignments/SusanPommerLab3-2.py 

#Your password must meet these requirements: 
#* must be at least 8 characters long 
#* must have at least 1 lowercase letter 
#* must have at least 1 uppercase letter 
#* must have at least 1 digit 

#Enter your password: asd123
#Re-enter your password: asd124

#Your passwords did not match; please try again.

#Your password must meet these requirements: 
#* must be at least 8 characters long 
#* must have at least 1 lowercase letter 
#* must have at least 1 uppercase letter 
#* must have at least 1 digit 

#Enter your password: iW2giW3
#Re-enter your password: iw2giw3

#Your passwords did not match; please try again.

#Your password must meet these requirements: 
#* must be at least 8 characters long 
#* must have at least 1 lowercase letter 
#* must have at least 1 uppercase letter 
#* must have at least 1 digit 

#Enter your password: 1h2j3k5l6
#Re-enter your password: 1h2j3k5l6

#Your password did not meet requirements.

#Your password must meet these requirements: 
#* must be at least 8 characters long 
#* must have at least 1 lowercase letter 
#* must have at least 1 uppercase letter 
#* must have at least 1 digit 

#Enter your password: abcdEFGH
#Re-enter your password: abcdEFGH

#Your password did not meet requirements.

#Your password must meet these requirements: 
#* must be at least 8 characters long 
#* must have at least 1 lowercase letter 
#* must have at least 1 uppercase letter 
#* must have at least 1 digit 

#Enter your password: A1B2C3D4E5F6G7H8
#Re-enter your password: A1B2C3D4E5F6G7H8

#Your password did not meet requirements.

#Your password must meet these requirements: 
#* must be at least 8 characters long 
#* must have at least 1 lowercase letter 
#* must have at least 1 uppercase letter 
#* must have at least 1 digit 

#Enter your password: iW2FtPb4T
#Re-enter your password: iW2FtPb4t

#Your passwords did not match; please try again.

#Your password must meet these requirements: 
#* must be at least 8 characters long 
#* must have at least 1 lowercase letter 
#* must have at least 1 uppercase letter 
#* must have at least 1 digit 

#Enter your password: iW2FtPb4T
#Re-enter your password: iW2FtPb4T

#That pair of passwords will work!

###########################################################

