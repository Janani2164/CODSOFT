import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    if length < 1:
        raise ValueError("Password length must be at least 1.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, filename="passwords.txt"):
    with open(filename, 'a') as file:
        file.write(password + '\n')
    print("Password saved to file.")

def load_passwords_from_file(filename="passwords.txt"):
    try:
        with open(filename, 'r') as file:
            passwords = file.read().splitlines()
        return passwords
    except FileNotFoundError:
        return []

def password_generator():
    print("Password Generator")

    while True:
        print("\nOptions:")
        print("1. Generate Password")
        print("2. Save Password to File")
        print("3. Load Passwords from File")
        print("4. Quit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            password_length = int(input("Enter the desired password length: "))
            include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            include_digits = input("Include digits? (y/n): ").lower() == 'y'
            include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
            generated_password = generate_password(
                length=password_length,
                use_uppercase=include_uppercase,
                use_digits=include_digits,
                use_special_chars=include_special_chars
            )
            print(f"\nGenerated Password: {generated_password}")
        elif choice == '2':
            password = input("Enter the password to save: ")
            save_password_to_file(password)
        elif choice == '3':
            passwords = load_passwords_from_file()
            if passwords:
                print("Loaded Passwords:")
                for idx, password in enumerate(passwords, start=1):
                    print(f"{idx}. {password}")
            else:
                print("No passwords found in the file.")
        elif choice == '4':
            print("Exiting the password generator. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    password_generator()

