import random


def random_list():
    rand_list = []
    n = 20
    for i in range(n):
        rand_list.append(random.randint(1, 100))
    print(rand_list)

    rand_list_average = sum(rand_list) / len(rand_list)
    print("Average of the list is: ", rand_list_average)

    largest = max(rand_list)
    print("The largest value is: ", largest)

    smallest = min(rand_list)
    print("The smallest value is: ", smallest)

    sorted_list = sorted(rand_list)
    print(sorted_list)

    second_largest = sorted_list[-2]
    second_smallest = sorted_list[1]
    print("Second largest entry in the list is: ", second_largest)
    print("Second smallest entry in the list is: ", second_smallest)

    even_count = 0
    for num in rand_list:
        if num % 2 == 0:
            even_count += 1
    print("The number of even numbers in the list: ")


random_list()
