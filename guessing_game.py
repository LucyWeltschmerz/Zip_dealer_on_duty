import random


def guess_the_nbr():
    number = random.randint(1, 100)
    # print(f"random number is: {number}")
    count = 0
    while True:
        guess = int(input("Try Guessing The Number: "))
        count += 1
        if guess == number:
            print(f'You managed to guess the number correctly! It was {guess}')
            if count == 1:
                print(f"It took you {count} attempt to guess the number correctly")
            else:
                print(f"It took you {count} attempts to guess the number correctly")
            break

        difference = abs(guess - number)

        if difference <= 10:
            if guess > number:
                print("You are very close, but the number you've entered is bigger than the actual number")
            else:
                print("You are very close, but the number you've entered is less than the actual number")
        else:
            if guess > number:
                print("The number you've entered is bigger than the actual number")
            else:
                print("The number you've entered is less than the actual number")


guess_the_nbr()
