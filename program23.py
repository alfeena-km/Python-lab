def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
num = int(input("Enter a number:"))
if num < 0:
    print("Factorial is not defined for negetive numbers.")
elif num == 0:
   print(F"{num}! = 1")
else:
  fact = factorial(num)
  print(f"{num} ! = {fact}")
 
