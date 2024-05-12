Alpha_Map="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext=input("Enter a Plaintext : ")
key=input("Enter a key : ")
cipher=""
for i, char in enumerate(plaintext):
    idxP = Alpha_Map.index(char)
    kChar = key[i % len(key)]
    idxK = Alpha_Map.index(kChar)
    cipher += Alpha_Map[(idxP + idxK) % 26]

print(f"Cipher: {cipher}")

Dcipher=""
for i, char in enumerate(cipher):
    idxP = Alpha_Map.index(char)
    kChar = key[i % len(key)]
    idxK = Alpha_Map.index(kChar)
    Dcipher += Alpha_Map[(idxP - idxK +26) % 26]

print(f"Cipher: {Dcipher}")