import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        password_length = int(input("Enter the desired password length: "))
        if password_length <= 0:
            raise ValueError("Password length must be a positive integer.")
        break
    except ValueError as e:
        print(f"Invalid input: {e}")

generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
