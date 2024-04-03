import random
import string

def generate_password(length: int, character_list: str) -> str:
    password = []
    for _ in range(length):
        random_char = random.choice(character_list)
        password.append(random_char)
    return ''.join(password)

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter password length: "))
    character_list = ''
    while True:
        print("1. Uppercase Letters")
        print("2. Lowercase Letters")
        print("3. Digits")
        print("4. Symbols")
        print("5. Done")
        choice = int(input("Pick a number: "))
        if choice == 1:
            character_list += string.ascii_uppercase
        elif choice == 2:
            character_list += string.ascii_lowercase
        elif choice == 3:
            character_list += string.digits
        elif choice == 4:
            character_list += string.punctuation
        elif choice == 5:
            break
        else:
            print("Invalid choice")

    password = generate_password(length, character_list)
    print("The random password is:", password)

if __name__ == '__main__':
    main()
