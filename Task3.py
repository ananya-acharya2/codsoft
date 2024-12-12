import random
import string

def generate_password(length, complexity):
   
    characters = {
        1: string.ascii_lowercase,
        2: string.ascii_lowercase + string.ascii_uppercase + string.digits,
        3: string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation,
    }

    if complexity not in characters:
        raise ValueError("Invalid complexity level. Choose 1, 2, or 3.")

    return ''.join(random.choices(characters[complexity], k=length))

def main():
    print("Welcome to the Password Generator!")

    try:

        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be a positive number.")
            return

       
        print("Choose complexity level:")
        print("1: Low (lowercase letters only)")
        print("2: Medium (lowercase, uppercase, digits)")
        print("3: High (includes special characters)")
        complexity = int(input("Enter complexity level (1, 2, or 3): "))


        password = generate_password(length, complexity)
        print(f"Your generated password: {password}")

    except ValueError:
        print("Invalid input. Please enter numbers for length and complexity.")

if __name__ == "__main__":
    main()
