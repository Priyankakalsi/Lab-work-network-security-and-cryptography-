def main():
    while True:
        p = int(input("\nEnter a Prime Number (P): "))
        if not isPrime(p):
            print(f"{p} is not Prime")
            continue

        q = int(input("Enter a Prime Number (Q): "))
        if not isPrime(q):
            print(f"{q} is not Prime")
            continue

        message = int(input("Enter M: "))

        n = p * q
        np = (p - 1) * (q - 1)

        e = getE(np)
        d = getD(e, np)

        cipher = encrypt(message, e, n)
        print(f"\nCipher: {cipher}")

        decipher = decrypt(cipher, d, n)
        print(f"Decipher: {decipher}")

        if input("\nEnter q/Q to Quit: ").lower() == "q":
            print("Bye!!")
            break


def encrypt(msg: int, e: int, n: int) -> int:
    return (msg ** e) % n


def decrypt(cipher: int, d: int, n: int) -> str:
    return (cipher ** d) % n


def getE(np: int) -> int:
    e = 2
    while gcd(e, np) != 1:
        e += 1
    return e


def getD(e: int, np: int) -> int:
    d = 2
    while (e * d) % np != 1:
        d += 1
    return d


def isPrime(n: int) -> bool:
    for i in range(2, int(n ** 0.5)):
        if n % i == 0:
            return False
    return True


def gcd(n1: int, n2: int) -> int:
    a = max(n1, n2)
    b = min(n1, n2)

    while a % b != 0:
        r = a % b
        a = b
        b = r

    return b


main()