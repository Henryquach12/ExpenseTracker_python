import random
import string

chars = ""+ string.punctuation + string.digits + string.ascii_letters + string.whitespace
chars = list(chars)
key = chars.copy()
random.shuffle(key)
password = input("Enter your password: ")
encrypted_password = ""
#Encrypt
for word in password:
    chars_index = chars.index(word)
    encrypted_password += key[chars_index]
print(f"Your password is {password}")
print(f"Your encrypted password is {encrypted_password}")

#Decrypt
decrypted_password = ""
decrypt = input("Do you want to decrypt your password? (y/n): ").lower()
if decrypt == "y" or decrypt == "yes":
    for word in encrypted_password:
        key_index = key.index(word)
        decrypted_password += chars[key_index]
    print(f"Your decrypted password is {decrypted_password}") 


