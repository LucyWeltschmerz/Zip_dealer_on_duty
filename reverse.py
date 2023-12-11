
def reverse_string():
    """
    Python program that takes a string as input from the user and then reverses and prints
    the reversed string. The program should the following:
    1. Ask the user to input a string.
    2. Reverse the string.
    3. Display the reversed string to the user.
    """
    user_input = input("Please input a string you want to reverse: ")
    reversed_user_input = user_input[::-1]
    print(f"The original string was: {user_input} \nThe reversed string is: {reversed_user_input}")

reverse_string()
