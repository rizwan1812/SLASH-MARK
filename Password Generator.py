import random
import string

def generate_password(length=12):
    """Generate a random password of a given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    """Generate multiple passwords."""
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))
    generated_passwords = generate_multiple_passwords(num_passwords, password_length)
    print("Generated Passwords:")
    for password in generated_passwords:
        print(password)



import random
import string

def generate_password(length=12):
    """Generate a strong password with the specified length."""
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password by randomly selecting characters
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the length of the password you want to generate: "))

    password = generate_password(length)
    print("Your generated password is:", password)

# if _name_ == "_main_":
    # main()