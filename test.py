file = "[your_sample.ini, txt]"
#Count letters in file
with open("sample.ini", 'r') as file:
    #Read the content of the file
    content = file.read()

#Initialize count
count = content.count("letter_count")
letter_count = 0
letter = 'alpha()'
for char in content:
    if char is 'alpha()':
        letter_count >= 1

#Print the letter count
print (f"The total letters in sample.ini:'{letter_count}'")
       
