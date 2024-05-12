def main():
  p = int(input("Enter a Prime Number (p): "))
  if not isPrime(p):
    print("p must be a Prime Number")

  g = int(input("Enter a Prime Number (g): "))
  if not isPrime(g):
    print("g must be a Prime Number")

  privateKey = int(input("Enter Your Private Key: "))
  if not validatePrivateKey(p, privateKey):
    print("Private Key must be between 1 and p-1")

  publicKey = getPublicKey(p, g, privateKey)

  theirPublicKey = int(input("Enter their Public Key: "))

  secret = getSecret(p, theirPublicKey, privateKey)

  print(f"\n\nPublic Key: {publicKey}")
  print(f"Secre: {secret}")


def isPrime(n: int) -> bool:
  for i in range(2, int(n**0.5)):
    if n % i == 0:
      return False
  return True


def validatePrivateKey(p: int, key: int) -> bool:
  return 1 <= key <= p


def getPublicKey(p: int, g: int, privateKey: int) -> int:
  return g**privateKey % p


def getSecret(p: int, theirPublicKey: int, privateKey: int) -> int:
  return theirPublicKey**privateKey % p


main()
