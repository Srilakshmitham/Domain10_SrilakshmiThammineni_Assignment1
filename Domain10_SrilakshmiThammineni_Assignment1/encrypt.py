def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key % 26
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

def decrypt(cipher_text, key):
    return encrypt(cipher_text, -key)

message = input("Enter your message: ")
key = int(input("Enter encryption key (integer): "))

encrypted = encrypt(message, key)
print("Encrypted Message:", encrypted)

decrypted = decrypt(encrypted, key)
print("Decrypted Message:", decrypted)
