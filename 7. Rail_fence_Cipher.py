import re


def main():
    key = int(input("Enter Key: "))
    plaintext = input("Enter Plaintext: ")

    cipher = encode(plaintext, key)
    print(f"Cipher: {cipher}")

    decipher = decode(cipher, key)
    print(f"Decipher: {decipher}")


def encode(msg: str, n: int) -> str:
    msg = re.sub(r'[^a-zA-Z0-9]', '', msg)
    rails = ['' for _ in range(n)]

    i = 0
    j = 0
    down = False
    while i < len(msg):
        rails[j] += msg[i]
        if j == 0 or j == n - 1:
            down = not down
        if down:
            j += 1
        else:
            j -= 1
        i += 1

    return " ".join(rails)


def decode(msg: str, n: int) -> str:
    clean_msg = re.sub(r'[^a-zA-Z0-9]', '', msg)
    rails = [['' for _ in range(len(clean_msg))] for _ in range(n)]
    decipher = ""

    i = 0
    j = 0
    down = False
    while i < len(clean_msg):
        rails[j][i] = '?'
        if j == 0 or j == n - 1:
            down = not down
        if down:
            j += 1
        else:
            j -= 1
        i += 1

    rows = msg.split(' ')

    for i, row in enumerate(rows):
        j = 0
        while j < len(row):
            charIdx = rails[i].index('?')
            rails[i][charIdx] = row[j]
            j += 1

    i = 0
    j = 0
    down = False
    while i < len(clean_msg):
        decipher += rails[j][i]
        if j == 0 or j == n - 1:
            down = not down
        if down:
            j += 1
        else:
            j -= 1
        i += 1

    return decipher


main()
