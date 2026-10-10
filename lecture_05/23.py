n = int(input("enter a number:"))
prod = 1
if n == 0:
    prod = 0
else:
    while n > 0:
        prod *= n % 10
        n //= 10
print(prod)
