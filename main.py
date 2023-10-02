import random
import string

def generate_password(length, include_letters=True, include_numbers=True, include_special_characters=True):
    characters = ''
    if include_letters:
        characters += string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_special_characters:
        characters += string.punctuation
    
    if len(characters) == 0:
        print("Error: Password cannot be generated without characters. Choose at least one type of character.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        length = int(input("Enter the desired length of the password: "))
        include_letters = input("Include letters in the password? (yes/no): ").lower() == 'yes'
        include_numbers = input("Include numbers in the password? (yes/no): ").lower() == 'yes'
        include_special_characters = input("Include special characters in the password? (yes/no): ").lower() == 'yes'
        
        password = generate_password(length, include_letters, include_numbers, include_special_characters)
        
        if password:
            print("Generated password:", password)
        else:
            print("Error generating password. Please try again.")
        
        generate_again = input("Generate another password? (yes/no): ").lower()
        if generate_again != 'yes':
            break

if __name__ == "__main__":
    main()

