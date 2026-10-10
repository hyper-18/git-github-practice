n = int(input("Enter a positive integer: "))
i = 1
while i <= n:
    if n % i == 0:
        print(i)
    i += 1
