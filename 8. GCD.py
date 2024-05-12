# GCD

n1 = int(input("Enter the first number: "))
n2 = int(input("Enter the second number: "))

a = max(n1, n2)
b = min(n1, n2)

while a % b != 0:
    r = a % b
    a = b
    b = r

print(f"The GCD of ({a}, {b}) = {b}")
