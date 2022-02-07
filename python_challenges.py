# Exercise 1: Calculator

calculation = input("What calculation would you like to do? (ex: add, sub, mult, div): ")

number1 = int(input("What is your first number?: "))

number2 = int(input("What is your second number?: "))

if calculation == "add":
    sum = number1 + number2
    print(sum)
elif calculation == "sub":
    difference = number1 - number2
    print(difference)
elif calculation == "mult":
    product = number1 * number2
    print(product)
elif calculation == "div":
    quotient = number1 / number2
    print(int(quotient))
else:
    print("Please enter valid calculation value")