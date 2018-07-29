###########################################################
# Course:  CS 21A Python Programming: Lab #4
# Name:  Susan Pommer
# Description:  Reads a filename provided by user
#   Opens file and read each line
#   Each line checked for letters, digits and underscores
#   If line meets criteria, create dictionary entry to hold
#      valid identifiers and associated line 
#   If valid identifier already recorded in the dictionary
#       append dictionary to add the line number 

# File name:  SusanPommerLab4.py
# Date:  July 31, 2017
###########################################################


## -------Define Main Program ------- ##

def main():

    # Ask user to input file name
    filename = input("Enter the Python file name you'd like to process: ")
    
    # Open the file to read 
    input_file = open(filename, 'r')

    # Read the first line from the file
    line = input_file.readline()

    # Initialize the valid identifiers dictionary
    valid_identifier_dictionary = {}

    # Initialize the row of code being reviewed
    row = 1

    # Loop to evaluate strings in the file
    # Evaluating that string is not empty 
    while line != '':
        
        # Strip string of leading and trailing characters
        stripped_string = line.strip()

        # Count number of digits in the stripped string
        number_digits = check_digits(stripped_string)

        # Count number of letters in stripped string
        number_letters = check_letter(stripped_string)

        # Count number of underscores in stripped string
        number_underscores = check_underscores(stripped_string)

        # Total the number of valid characters
        total_valid = number_letters + number_digits + number_underscores

        # Validate if string meets criteria to added to dictionary
        should_save = validate_criteria(total_valid, stripped_string)


        # Add valid entries to dictionary     
        # Check to see if valid entry is already in dictionary
        if should_save == True: 
            # Create or add to list of lines for valid identifier
            stripped_string_list = create_or_add_to_list(stripped_string, row, valid_identifier_dictionary)

            # Update the valid identifier dictionary 
            # Stripped string is key; value is list of line numbers  
            valid_identifier_dictionary[stripped_string] = stripped_string_list

        # Advance to next line in file
        row += 1

        # Read the next line
        line = input_file.readline()
    
    # Close the file
    input_file.close()

    # Print the contents of the dictionary  
    dictionary_output(valid_identifier_dictionary)
    

# ----- FUNCTIONS -------

# Function to identify and count digits
def check_digits(stripped_value): 
    # Initialize the counter
    digit_count = 0

    # Loop to check if each character is a digit
    for ch in stripped_value:
        if ch.isdigit():
            digit_count += 1        
    return digit_count


# Function to identify and count letters
def check_letter(stripped_value):
    # Initialize the counter
    letter_count = 0

    # Loop to check if each character is a letter
    for ch in stripped_value:
        if ch.isalpha():     
            letter_count += 1
    return letter_count


# Function to identify and count underscores
def check_underscores(stripped_value):
    # Initialize the counter
    underscore_count = 0

    # Loop to check if each character is an underscore
    for ch in stripped_value:
        if ch == "_": 
            underscore_count += 1

    return underscore_count


# Function to validate if string meets criteria
# String must contain only digits, letters or underscores
# Total valid characters = length of stripped string if valid

def validate_criteria(total_valid, stripped_value):
    if total_valid == len(stripped_value):
        save_to_dictionary = True
    else:
        save_to_dictionary = False

    return(save_to_dictionary)
        

# Function to create, or add to, a list of lines for a valid identifier
def create_or_add_to_list(stripped_string, row, valid_identifier_dictionary):
    # Check to see if the valid identifier is already in dictionary

    # If valid identifer is not already in dictionary
    if stripped_string not in valid_identifier_dictionary:
        # Create a list for the row numbers for that string
        stripped_string_list = [row]
                
    # If valid identifier is already added to the dictionary
    # Add the new row number to the existing list of rows (value)
    else:
        # Get the list for that string
        stripped_string_list = valid_identifier_dictionary.get(stripped_string, "error")

        # Add the line number to the existing list of line numbers for that string
        stripped_string_list.append(row)

    return stripped_string_list


# Function to print dictionary contents in desired output format
# Loop to print each element in the dictionary 
def dictionary_output(dictionary):
    for keys, values in dictionary.items():
        print (keys, ': ', values, sep='')
    

# Call main function
main()

## --------------------Sample Run --------------------------- ##
# Test run used provided input file t4.py

#= RESTART: C:\Pommer Files\CLASSES\FHC CS21A\Assignments\SusanPommerLab4.py =
# Enter the Python file name you'd like to process: t4.py
# apple: [1, 11]
# 1: [2, 3]
# ball: [4, 19]
# art: [5]
# dog: [6]
# pen: [8, 21]
# rat: [9]
# 4: [10]
# carrot: [13]
# orange: [15]
# ant: [16, 17, 18]
# stick: [20]
# _: [22]
# goodbye: [25]
