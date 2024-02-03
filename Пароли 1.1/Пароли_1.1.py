import random

def generate_password(length):
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+"
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

length = int(input("Enter the length of the password: "))
password = generate_password(length)
print("Your password is:", password)
