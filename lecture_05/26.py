n = int(input("enter a integer:"))
if n < 0:
    print("negative")
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(factorial)
