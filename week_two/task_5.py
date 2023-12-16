def is_prime():

    user_input = input("Enter a positive integer greater than 1: ")

    if user_input.isdigit():
        user_input = int(user_input)

        if isinstance(user_input, int) and user_input > 1:
            is_prime = True
            for i in range(2, int(user_input ** 0.5) + 1):
                if user_input % i == 0:
                    is_prime = False
                    break

            if is_prime:
                print(f"{user_input} is a prime number")
            else:
                print(f"{user_input} is not a prime number")
    else:
        return False


print(is_prime())