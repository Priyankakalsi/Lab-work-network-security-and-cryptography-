Alpha_Map="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
plaintext=input("Enter a Plaintext : ")
key=input("Enter a key 26 Characters long: ")

cipher=""
for char in plaintext:
    Pidx=Alpha_Map.index(char)
    cipher+=key[Pidx]
print(f" cipher {cipher}")

Dcipher=""
for char in cipher:
    Pidx=key.index(char)
    Dcipher+=Alpha_Map[Pidx]
print(f" Dcipher {Dcipher}")