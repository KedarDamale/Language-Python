# Importing required libraries
import random   # For shuffling the key (used in encryption)
import string   # For generating a character set of all printable characters

# Step 1: Create a list of characters that can be used in encryption
# string.punctuation => !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# string.digits => 0123456789
# string.ascii_letters => abc...xyzABC...XYZ
# " " => explicitly adding space character so that spaces are also encrypted
chars = string.punctuation + string.digits + string.ascii_letters + " "

# Convert the combined string of characters into a list
chars = list(chars)  # This makes it easier to manipulate by index

# Step 2: Create a shuffled version of the original characters list to use as the encryption key
key = chars.copy()  # Make a shallow copy so the original `chars` remains unchanged
random.shuffle(key) # Randomly shuffle the `key` list to map original chars to encrypted chars

# ------------------------------------------
# ENCRYPTION
# ------------------------------------------

# Get user input to encrypt
plain_text = input("Enter a message to encrypt: ")

# Initialize an empty string to store the encrypted version
cipher_text = ""

# Encrypt each character by finding its index in `chars` and replacing with the corresponding index in `key`
for letter in plain_text:
    index = chars.index(letter)   # Find the position of the original character
    cipher_text += key[index]     # Use that index to find the corresponding encrypted character from `key`

# Display the encrypted message
print(f"\nOriginal text : {plain_text}")    
print(f"Cipher text   : {cipher_text}")

# ------------------------------------------
# DECRYPTION
# ------------------------------------------

# Get user input to decrypt (should be previously encrypted message)
cipher_text = input("\nEnter a message to decrypt: ")

# Initialize an empty string to store the decrypted version
plain_text = ""

# Decrypt each character by reversing the encryption mapping
for letter in cipher_text:
    index = key.index(letter)     # Find the index of the encrypted character in the `key` list
    plain_text += chars[index]    # Use that index to retrieve the original character from `chars`

# Display the decrypted message
print(f"Cipher text   : {cipher_text}")
print(f"Original text : {plain_text}")
