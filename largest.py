num1 = float(input("Enter the first number:"))
num2 = float(input("Enter secound number:"))
num3 = float(input("Enter third number:"))
if(num1 >= num2) and (num1 >= num3):
    max = num1
elif(num2 >= num1) and (num2 >= num3):
     max = num2
else:
     max = num3
print("The largest number is",max)
