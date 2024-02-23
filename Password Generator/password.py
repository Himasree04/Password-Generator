import random
import string

def generate_password(length):
    # Define character sets for password generation
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    try:
        # Prompt user for password length
        length = int(input("Enter desired password length: "))

        # Generate and display the password
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
