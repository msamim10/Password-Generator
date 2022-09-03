# Import these as they are essential to this program
import string
import random

# Text color class to make it a bit fancy
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print('---------------------------------------------------------------------------------------------------------------------')
print(color.DARKCYAN + "Welcome to Password Generator!" + color.END)
print()
print(color.YELLOW + color.BOLD + "WARNING!!!! Despite being a random password generator, no password is totally safe." + color.END)
print()
while True:
    min_char = int(input('Minimum number of characters: '))
    num_cap = int(input('Number of capital letters: '))
    num_punc = int(input('Number of punctuations: '))
    num_digi = int(input('Number of digits: '))
    pass_len = int(input('Password length: '))

    if min_char <= num_cap + num_punc + num_digi and pass_len >= min_char:
        break
    else:
        print('\nThe number of minimum characters does not match the required components!\n')
        print('---------------------------------------------------------------------------------------------------------------------')
        print()
    
caps = []
for i in range(0, num_cap):
    caps.append(random.choice(string.ascii_letters).upper())

puncts = []
for i in range(0, num_punc):
    puncts.append(random.choice(string.punctuation))

digits = []
for i in range(0, num_digi):
    digits.append(random.choice(string.digits))
    
pass_req = caps + puncts + digits
pass_len = pass_len - min_char
password = []
for i in range(0, pass_len):
    password.append(random.choice(string.ascii_letters).lower())
    
for char in pass_req:
    password.append(char)
random.shuffle(password)
password_str = ''
for i in password:
    password_str+=i
print("\nYour new generated password: " + color.GREEN + color.BOLD + password_str + color.END)
option = str(input("\nWould you like to save your password under an account?(y/n)? "))
if(option == 'y' or option == 'Y'):
    filename = str(input("Please enter the name of the application for the newly made password: "))
    username = str(input("Please enter the username of your account: "))
    f = open('accounts.txt', 'a')
    f.writelines(filename)
    f.writelines('\n-----------------------------')
    f.writelines('\nUsername: ' + username + '\n')
    f.writelines('Password: ' + password_str + '\n\n')
    print(color.GREEN + color.BOLD + "\nFile accounts.txt has been created successfully!" + color.END)
    print('---------------------------------------------------------------------------------------------------------------------')
    f.close()
else:
    print(color.DARKCYAN + "\nGoodbye!" + color.END)
    print('---------------------------------------------------------------------------------------------------------------------')