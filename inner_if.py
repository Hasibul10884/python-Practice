num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 > num2:
    if num1 > num3:
        print("num1 is the largest")
    else:
        print("num3 is the largest")
if num2 > num1:
    if num2 > num3:
        print("num2 is the largest")
    else:
        print("num3 is the largest")