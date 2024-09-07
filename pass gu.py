import random
import string
def generate_password(length):
    """Generates a password of the specified length using random characters."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to prompt the user for the password length and generate the password."""
    print("Welcome to the Password Generator!")
    while True:
        try:
            length = int(input("Enter the desired length for your password: "))
            if (length < 1):
                print("Password length must be at least 1. Please try again.")
                continue
            password = generate_password(length)
            print(f"Your generated password is: {password}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid number for the password length.")

if __name__ == "__main__":
    main()
