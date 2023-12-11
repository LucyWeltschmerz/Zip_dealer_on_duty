def number():
    total = 0
    count = 0

    while True:
        user_input = input("Enter a number (type 'done' to finish): ")

        if user_input.lower() == 'done':
            break

        try:
            nbr = int(user_input)
            total += nbr
            count += 1
        except ValueError:
            print("Invalid input. Please enter a valid integer or 'done'.")

    if count > 0:
        average = total // count
        print(f"\nTotal: {total}")
        print(f"Count: {count}")
        print(f"Average: {average}")
    else:
        print("\nNo valid integers entered.")


number()
