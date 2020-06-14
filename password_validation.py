digits = 0
special_charecter = 0
print('A valid password should have atleast 1 digit')
print('A valid password should have 6-16 charecters')
print('A valid password should contain any special characters from(@!#$%^)')
password = input('Create a valid password:   ')

charecters = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
if int(len(password)) in charecters:
    pass   
else:
    print('Inappropriate charecters')

special_charecters = ['!', '@', '#', '$', '%', '^']
for charecter in password:
    if charecter in special_charecters:
        special_charecter = special_charecter + 1
if special_charecter == 0:
    print('None of the special charecters have been included')

for x in password:
    if x.isdigit():
        digits = digits + 1
if digits == 0:
    print('There are no digits')
    
