def print_diamond(n):
    if n % 2 == 0:
        print("Please enter an odd integer.")
        return

    for i in range(1, n + 1, 2):
        spaces = " " * ((n - i) // 2)
        asterisks = "*" * i
        print(spaces + asterisks)

    for i in range(n - 2, 0, -2):
        spaces = " " * ((n - i) // 2)
        asterisks = "*" * i
        print(spaces + asterisks)


n = int(input("Enter an odd integer 'n': "))
print_diamond(n)
