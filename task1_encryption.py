def caesar(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord('a') + key) % 26) + ord('a'))
            else:
                encrypted_char = chr(((ord(char) - ord('A') + key) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


mot = input("Ecris la phrase à crypter : ")
key = int(input("Ecris une clé de décalage (comprise entre 1 et 25) : "))

while key < 1 or key > 25:
    key = int(input("La clé doit être comprise entre 1 et 25 : "))

encrypted_text = caesar(mot, key)
print("Phrase cryptée : ", encrypted_text)