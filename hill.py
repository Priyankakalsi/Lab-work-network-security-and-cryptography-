# Hill Cipher
key = [[0, 0], [0, 0]]

alpha = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

for x in range(2):
    for y in range(2):
        key[x][y] = int(input("Enter numeric value : "))

def find_determinant(key):
    val = (key[0][0] * key[1][1] - key[0][1] * key[1][0]) % 26
    return val

def inverse_key(key):
    key[0][0], key[1][1] = key[1][1], key[0][0]
    key[0][1], key[1][0] = -1 * key[0][1], -1 * key[1][0]
    return key

def matrix_multiplication(mtrx1, mtrx2):
    result = []
    result.append(mtrx1[0] * mtrx2[0][0] + mtrx1[1] * mtrx2[1][0])
    result.append(mtrx1[0] * mtrx2[0][1] + mtrx1[1] * mtrx2[1][1])
    
    for i in range(2):
        result[i] = result[i] % 26

    return result

# Encryption
values = []

for i in range(2):
    values.append(input("Enter alphabets: ").upper())

indexes = []

for x in values:
    for char in x:
        indexes.append(alpha.index(char))

enc_index = matrix_multiplication(indexes, key)
enc_txt = ""
for i in enc_index:
    enc_txt += f"{alpha[i]}"

print("Encrypted text:", enc_txt)

# Decryption
print("---------Decryption Start ---------------------")

det = find_determinant(key)
mtrx_inverse = inverse_key(key)

val = 0

for n in range(100):
    if (det * n) % 26 == 1:
        val = n
        break

key_decrypt = mtrx_inverse

for row in range(2):
    for col in range(2):
        key_decrypt[row][col] *= val

for i in range(2):
    for j in range(2):
        key_decrypt[i][j] = key_decrypt[i][j] % 26

dec_txt = []

for n in range(2):
    dec_txt.append(input("Enter text: ").upper())

dec_index = []

for letter in dec_txt:
    dec_index.append(alpha.index(letter))

enc_text_index = matrix_multiplication(dec_index, key_decrypt)

for i in range(2):
    enc_text_index[i] = enc_text_index[i] % 26

final_txt = ""

for i in enc_text_index:
    final_txt += f"{alpha[i]}"

print("Decrypted text:", final_txt)