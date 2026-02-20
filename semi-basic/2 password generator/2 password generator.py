import random
import string

def pwgen(length, with_digits=True, with_uppercase=True):
    """
    Generate a random password with specified characteristics.
    
    Args:
        length (int): The length of the generated password
        with_digits (bool): To allow or disallow digits
        with_uppercase (bool): To allow or disallow capital letters
    
    Returns:
        str: Generated password
    """

    lowercase = string.ascii_lowercase
    digits = string.digits
    uppercase = string.ascii_uppercase
    

    char_pool = lowercase

    required_chars = []
    
    if with_digits:
        char_pool += digits
        required_chars.append(random.choice(digits))
    
    if with_uppercase:
        char_pool += uppercase
        required_chars.append(random.choice(uppercase))
    

    required_chars.append(random.choice(lowercase))

    remaining_length = length - len(required_chars)
    

    if remaining_length > 0:
        for _ in range(remaining_length):
            required_chars.append(random.choice(char_pool))
    elif remaining_length < 0:

        required_chars = required_chars[:length]

    random.shuffle(required_chars)
    
    return ''.join(required_chars)


def get_user_input():
    """Get password parameters from user."""
    print("=== Password Generator ===\n")
    

    while True:
        try:
            length = int(input("Enter password length: "))
            if length < 1:
                print("Password length must be at least 1. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    

    while True:
        digits_input = input("Include digits? (yes/no, default=yes): ").strip().lower()
        if digits_input in ['', 'yes', 'y']:
            with_digits = True
            break
        elif digits_input in ['no', 'n']:
            with_digits = False
            break
        else:
            print("Please answer 'yes' or 'no' (or press Enter for default 'yes').")
    

    while True:
        upper_input = input("Include uppercase letters? (yes/no, default=yes): ").strip().lower()
        if upper_input in ['', 'yes', 'y']:
            with_uppercase = True
            break
        elif upper_input in ['no', 'n']:
            with_uppercase = False
            break
        else:
            print("Please answer 'yes' or 'no' (or press Enter for default 'yes').")
    
    return length, with_digits, with_uppercase


def main():
    """Main program function."""
 
    length, with_digits, with_uppercase = get_user_input()
    

    password = pwgen(length, with_digits, with_uppercase)
    
 
    print("\n" + "=" * 40)
    print("GENERATED PASSWORD")
    print("=" * 40)
    print(f"Length: {length}")
    print(f"Include digits: {'Yes' if with_digits else 'No'}")
    print(f"Include uppercase: {'Yes' if with_uppercase else 'No'}")
    print("-" * 40)
    print(f"Password: {password}")
    print(f"Password length: {len(password)} characters")
    print("=" * 40)
    

    has_lower = any(c.islower() for c in password)
    has_digits = any(c.isdigit() for c in password)
    has_upper = any(c.isupper() for c in password)
    
    print("\nPassword composition:")
    print(f"✓ Lowercase letters: {'Yes' if has_lower else 'No'}")
    print(f"✓ Digits: {'Yes' if has_digits else 'No'}")
    print(f"✓ Uppercase letters: {'Yes' if has_upper else 'No'}")



if __name__ == "__main__":
    main()
    

    while True:
        again = input("\nGenerate another password? (yes/no): ").strip().lower()
        if again in ['yes', 'y']:
            print("\n" + "-" * 40)
            main()
        elif again in ['no', 'n']:
            print("\nThank you for using the Password Generator. Goodbye!")
            break
        else:
            print("Please answer 'yes' or 'no'.")
