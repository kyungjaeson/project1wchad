def question_principal():
    while True:
        user_answer = input(
            "\nWhat is the total value of the house you want to purchase. This is known as your principal. i.e. 500000 ")
        if user_answer.isdigit():
            return int(user_answer)
        else:
            print("\nInvalid input. Please format like so 500000")


def question_mortgage_type_length():
    while True:
        user_answer = input("\n How long is the term of this mortgage? i.e. 15, 20, 30, 45")
        if user_answer.isdigit() and int(user_answer) > 0:
            return int(user_answer)
        else:
            print("\nNot a valid length")


def question_mortgage_type():
    while True:
        user_answer = input(
            """\nAre you dealing with a 
1) fixed term mortgage 
or 
2)adjustable rate mortgage 
Enter 1 or 2""")
        if int(user_answer) == 1:
            return question_mortgage_type_length()
        elif int(user_answer) == 2:
            print(
                "\nARM requires more specialized calculation please reference \"https://www.usbank.com/home-loans/mortgage/mortgage-calculators/arm-calculator.html\"")
            quit()
        else:
            print('\nPlease enter 1 or 2')


def question_mortgage_rate():
    while True:
        user_answer = input("\nWhat is the annual interest rate you will pay on your principal i.e. 5.375")
        if float(user_answer) > 10.0:
            print("\nYou're being robbed, try a different loan agent")
        elif float(user_answer) > 0:
            return float(user_answer)
        elif float(user_answer) <= 0:
            print("\nCan't have negative interest")
        else:
            print("\nInvalid input. Please format like so 1.2 ")


def question_mortgage_downpayment(principal):
    while True:
        user_answer = input(
            "\nHow much downpayment are you going to put down? (This is the amount you pay to lower your principal i.e. 150000")
        if 0 <= int(user_answer) < principal:
            return int(user_answer)
        else:
            print("\nPlease adjust your downpayment amount to the format 150000 between 0 and your principal")


