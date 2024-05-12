num = int(input("Enter a number: "))
is_Prime=True
for i in range(2,num//2):
    if num%i==0:
        is_Prime = False
        break

if is_Prime:
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")
    