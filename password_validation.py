digits = 0
special_character = 0
print('A valid password should have atleast 1 digit')
print('A valid password should have 6-16 charecters')
print('A valid password should contain any special characters from(@!#$%^)')
password = input('Create a valid password:   ')

characters = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
if int(len(password)) in characters:
    pass   
else:
    print('Inappropriate charecters')

special_characters = ['!', '@', '#', '$', '%', '^']
for character in password:
    if character in special_characters:
        special_character = special_character + 1
if special_character == 0:
    print('None of the special charecters have been included')

for x in password:
    if x.isdigit():
        digits = digits + 1
if digits == 0:
    print('There are no digits')
    
"""
if 6 < int(len(password)) < 16:
    print("It has appropriate characters") # my sugesstion to the code
"""
