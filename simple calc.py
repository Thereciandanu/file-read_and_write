num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
operator = input("Enter a mathematical operation (+, -, *, /): ")

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/' and num2 != 0:
    result = num1 / num2
else:
    print("Invalid input or division by zero.")
    exit()

print(f"{num1} {operator} {num2} = {result}")



