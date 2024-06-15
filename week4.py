import random
import string

def generate_password(length=12):
    # Define the character sets
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Combine all the characters
    all_chars = lower_case + upper_case + digits + special_chars
    
    # Ensure the password has at least one character from each set
    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle the list to ensure randomness
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Generate a password of the desired length
password_length = 16  # You can change this value to your desired password length
password = generate_password(password_length)
print(f"Generated Password: {password}")