Alpha_Map="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key=int(input("Enter a key : "))
Plaintext=input("Enter a plaintext : ")
cipher=""
for char in Plaintext:
    Pidx=Alpha_Map.index(char)
    cipher+=Alpha_Map[(Pidx+key)%26]
print(f"cipher {cipher}")

Dcipher=""
for char in cipher:
    Pidx=Alpha_Map.index(char)
    Dcipher+=Alpha_Map[(Pidx-key)%26]
print(f"Dcipher {Dcipher}")
