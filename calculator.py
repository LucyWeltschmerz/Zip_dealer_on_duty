
def calculator():
    """
    A simple calculator program. It takes two numbers and an operator (+, -, *, /)
    as input and performs the corresponding arithmetic operation.
    :return:
    """
    nbr1 = int(input("Enter the first number: "))
    symb = input("Enter an operator (+, -, *, /): ")
    nbr2 = int(input("Enter the second number: "))
    if symb == '+':
        result = nbr1 + nbr2
    elif symb == '-':
        result = nbr1 - nbr2
    elif symb == '*':
        result = nbr1 * nbr2
    else:
        result = nbr1 / nbr2
    return result


print(calculator())
