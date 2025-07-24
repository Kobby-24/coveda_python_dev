alphabet = 'abcdefghijklmnopqrstuvwxyz'
def caesar_cipher(text, shift):
    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            new_char = chr((ord(char.lower()) - ord('a') + shift_amount) % 26 + ord('a'))
            if char.isupper():
                new_char = new_char.upper()
            encrypted_text += new_char
        else:
            encrypted_text += char
    return encrypted_text
def decrypt_caesar_cipher(text, shift):
    return caesar_cipher(text, -shift)

def encrypt_message(filename, shift):
    try:
        with open(f'{filename}.txt', 'r') as file:
            data = file.readlines()
            print("Original data:", data)
            data = [caesar_cipher(line.strip(),shift) for line in data]
            print("Encrypted data:", data)
            
            with open(f'encrypted_{filename}_message.txt', 'w') as encrypted_file:
                encrypted_file.write('\n'.join(data))
                print(f"Message encrypted and saved to encrypted_{filename}_message.txt")
    except FileNotFoundError:
        print(f"File {filename}.txt not found. Please ensure the file exists.")

def decrypt_message(filename, shift):
    try:
        with open(f'{filename}.txt', 'r') as file:
            data = file.readlines()
            data = [decrypt_caesar_cipher(line.strip(), shift) for line in data]

            with open(f'decrypted_{filename}_message.txt', 'w') as decrypted_file:
                decrypted_file.write('\n'.join(data))
                print(f"Message decrypted and saved to decrypted_{filename}_message.txt")
    except FileNotFoundError:
        print(f"File {filename}.txt not found. Please ensure the file exists.")

def main():
    choice = input("Do you want to encrypt or decrypt a message? (e/d): ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
        main()
    filename = input("Enter the filename (without extension): ")
    while True:
        try:
            shift = int(input("Enter the shift value: "))
            if shift < 0:
                print("Shift value must be a non-negative integer.")
                continue
            if shift > 25:
                print("Shift value must be less than or equal to 25.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")
    

    if choice == 'e':
        encrypt_message(filename, shift)
        
    elif choice == 'd':
        decrypt_message(filename, shift)
        
    

if __name__ == "__main__":
    main()
