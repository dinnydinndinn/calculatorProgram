# Addition
def add(n1, n2):
    return n1 + n2


# Substraction
def subtract(n1, n2):
    return n1 - n2


# Multiplication
def multiply(n1, n2):
    return n1 * n2


# Division
def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():

    num1 = float(input("What is the first number?: "))
    for symbol in operations:
        print(symbol)

    calculation_continue = True

    while calculation_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        response = input(
            (f"Type 'y' if to continue calculating with {answer}, or type 'n' to start a new calculation: "))
        if response.lower() == "n":
            calculation_continue = False
            calculator()
        else:
            num1 = answer


calculator()


