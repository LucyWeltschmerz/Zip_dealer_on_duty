def nbr_length_and_sum(num):
    length = 0
    digit_sum = 0

    while num > 0:
        length += 1
        digit_sum += num % 10
        num //= 10

    print("Length is: ", length)
    print("The sum of the digits is: ", digit_sum)


nbr_length_and_sum(12345)

