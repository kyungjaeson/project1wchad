#! /usr/bin/python3
import module.questions
import questions


def main():
    print("""
    This is the monthly mortgage calculator.
    Find out what you need to pay every month to go towards your mortgage
    Let's Begin. 
    """)
    principal = questions.question_principal()
    length = questions.question_mortgage_type() * 12
    rate = questions.question_mortgage_rate() * .01 / 12
    #use this to test rate.
    # print(rate)

    downpayment = questions.question_mortgage_downpayment(principal)
    print(principal,length, rate, downpayment)
    monthly_payment = (principal - downpayment) * (rate * (1 + rate) ** length) / (((1 + rate) ** length) - 1)

    print(f"\nYour monthly payment is ${monthly_payment:,.2f}. You also need to consider property taxes and homeowners insurance")


if __name__ == '__main__':
    main()
