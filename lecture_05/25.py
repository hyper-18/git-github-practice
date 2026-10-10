n = int(input("Enter a non-negative integer: "))
original = n
reversed_number = 0
while n > 0:
    reversed_number = reversed_number * 10 + n % 10
    n //= 10
if original >= 0 and original == reversed_number:
    print("Palindrome")
else:
    print("Not a palindrome")
