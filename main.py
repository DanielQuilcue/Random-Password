# Python 3.10.8
# UTF-8

# Small script to generate secure passwords and store them locally. 
# By Daniel Quilcue

# Import modules.
import secrets
import string

# Alphabet definition.
lettering = string.ascii_letters 
digits = string.digits
specialChars = string.punctuation


# Concatenate the previous string variables to obtain the alphabet.add().
alphabet = lettering + digits + specialChars

# We ask the user which site the password will be for.
sitePassaword = input("The password will be for which site: ")

# Set password length.
lonPassword = int(input("Please enter the password length: "))


# Generating the password.
pwd = ''
for i in range(lonPassword):
    pwd += ''.join(secrets.choice(alphabet))

# Generate a password that complies with the given parameters.
while True:
    pwd = ''
    for i in range(lonPassword):
        pwd += ''.join(secrets.choice(alphabet))

    if (any(char in specialChars for char in pwd) and 
        sum(char in digits for char in pwd) >=2):
        break

# We open file.txt and send it the password and lonPassword variables.
with open("saving-passwords.txt", "a") as file:
    file.write('\n')
    file.write('\n')
    file.write("Site: ")
    file.write(sitePassaword)
    file.write('\n')
    file.write("Password: ")
    file.write(pwd)
file.close()

# Verify password security.
# https://www.security.org/how-secure-is-my-password/