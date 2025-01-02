import re

def count_characters(input_string):
    # Regular expressions for different types of characters
    uppercase_pattern = r'[A-Z]'
    lowercase_pattern = r'[a-z]'
    numeric_pattern = r'[0-9]'
    special_pattern = r'[^A-Za-z0-9]'

    # Using re.findall() to find all matches
    uppercase_count = len(re.findall(uppercase_pattern, input_string))
    lowercase_count = len(re.findall(lowercase_pattern, input_string))
    numeric_count = len(re.findall(numeric_pattern, input_string))
    special_count = len(re.findall(special_pattern, input_string))

    # Print the results
    print(f"Uppercase letters: {uppercase_count}")
    print(f"Lowercase letters: {lowercase_count}")
    print(f"Numeric values: {numeric_count}")
    print(f"Special characters: {special_count}")

# Input from the user
input_string = input("Enter a string: ")
count_characters(input_string)
