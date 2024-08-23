import random
import string

def generate_password(length, include_uppercase, include_digits, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_digits:
        password.append(random.choice(string.digits))
    if include_special:
        password.append(random.choice(string.punctuation))

    password += random.choices(characters, k=length - len(password))
    random.shuffle(password)
    
    return ''.join(password)

def main():
    try:
        length = int(input("Enter the desired password length: "))
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_special = input("Include special characters? (y/n): ").lower() == 'y'
        
        if length < 1:
            raise ValueError("Password length must be at least 1.")
        
        password = generate_password(length, include_uppercase, include_digits, include_special)
        print(f"Generated password: {password}")
    
    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
