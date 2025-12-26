import random
import string

length = 16

password = [
    random.choice(string.ascii_lowercase),
    random.choice(string.ascii_uppercase),
    random.choice(string.digits),
    random.choice(string.punctuation)
]

characters = string.ascii_letters + string.digits + string.punctuation

for i in range(length - 4):
    password.append(random.choice(characters))

random.shuffle(password)

print("Generated Password:", "".join(password))
# This script generates a random password of specified length (16 characters by default)
# including at least one lowercase letter, one uppercase letter, one digit, and one punctuation character for enhanced security.
