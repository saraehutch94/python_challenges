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

# Exercise 2: Reverse a string

string = input("Enter a string: ")

string_length = len(string)

reversed_string = ""

for letter in range(string_length - 1, -1, -1):
    reversed_string += string[letter]

print(reversed_string)

# Exercise 3: Bank Transactions

def bankTransactions():

    global balance
    balance = 5000

    def display_balance():
        print(f'Your current balance is {balance}')

    def withdraw():
        global balance
        withdraw_amount = input("How much would you like to deposit?: ")
        balance -= int(withdraw_amount)
        display_balance()

    def deposit():
        global balance
        deposit_amount = input("How much would you like to deposit?: ")
        balance += int(deposit_amount)
        display_balance()

    def done():
        done = input("Are you done?: ")
        if done == "yes":
            print("Thank you!")
            return
        # else: done == "no"
        else:
            return introPrompt()

    def introPrompt():
        display_balance()
        user_choice = input("Which of these actions would you like to accomplish: display, withdraw, or deposit?: \n")

        if user_choice == "display":
            display_balance()
            done()
        elif user_choice == "withdraw":
            withdraw()
            done()
        elif user_choice == "deposit":
            deposit()
            done()
        # else: user_input is not one of the provided choices
        else:
            print("* PLEASE ENTER A VALID ACTION *")
            introPrompt()
    
    introPrompt()

bankTransactions()

# Exercise 4: Sort a String

def alphabetizeString():

    entered_string = input("Give me a string to alphabetize: ")

    def sort_string():
        sorted_string = sorted(entered_string)
        joined_string = "".join(sorted_string)
        print(f'Alphabetized: {joined_string}')

    if (entered_string.isalpha()):
        sort_string()
    else:
        print("* PLEASE ENTER ONLY LETTER CHARACTERS *")

alphabetizeString()