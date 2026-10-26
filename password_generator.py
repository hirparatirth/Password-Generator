
import secrets
import string

def generate_password():
    print("\n===== PASSWORD GENERATOR =====")

    try:
        length = int(input("Enter password length (8-64): "))
        if not 8 <= length <= 64:
            print("Please enter a length between 8 and 64.")
            return

        characters = ""

        if input("Include uppercase letters? (y/n): ").lower() == "y":
            characters += string.ascii_uppercase

        if input("Include lowercase letters? (y/n): ").lower() == "y":
            characters += string.ascii_lowercase

        if input("Include numbers? (y/n): ").lower() == "y":
            characters += string.digits

        if input("Include symbols? (y/n): ").lower() == "y":
            characters += "!@#$%^&*()-_=+?"

        if not characters:
            print("Select at least one character type.")
            return

        password = "".join(
            secrets.choice(characters) for _ in range(length)
        )

        print("\nYour generated password:", password)
        print("Password length:", len(password))

    except ValueError:
        print("Please enter a valid number.")

while True:
    generate_password()

    again = input("\nGenerate another password? (y/n): ").lower()
    if again != "y":
        print("Thank you for using Password Generator!")
        break
