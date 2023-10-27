# simple calculator with function

def calculator(num1, num2, eq):
    if eq == '+':
        return num1 + num2
    elif eq == '-':
        return num1 - num2
    elif eq == '*':
        return num1 * num2
    elif eq == '/':
        return num1 / num2
    else:
        print('Invalid operator')


num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
eq = input('Enter operator: ')

print(calculator(num1, num2, eq))
