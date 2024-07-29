def encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_message, shift):
    decrypted = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.islower():
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted += char
    return decrypted

def cipher():
    print()
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value (0-25): "))
    encrypted_message = encrypt(message, shift)
    print("Encrypted message:", encrypted_message)
    decrypted_message = decrypt(encrypted_message, shift)
    print("Decrypted message:", decrypted_message)

cipher()
