import os
import string


# Function to count letters [a-z, A-Z] and numbers [0-9] in the input string 
def count_letters_numbers_and_vowels(text):
    letter_count = 0
    number_count = 0
    vowel_count = 0

    for char in text:
        if char.isalpha():
            letter_count += 1
            if char.lower() in "aeiou":
                vowel_count += 1
        elif char.isnumeric():
            number_count += 1
    
    return letter_count, number_count, vowel_count

# Read the content of "sample.ini" file
file_path = "sample.ini"
with open("sample.ini","r") as file:
        content = file.read() 

# Count letters, numbers and vowels in the content 
letter_count, number_count, vowel_count = count_letters_numbers_and_vowels ("content")


# Print the counts
print(f"Letter count: {letter_count}")
print(f"Number count: {number_count}")
print(f"Vowel count: {vowel_count}")

