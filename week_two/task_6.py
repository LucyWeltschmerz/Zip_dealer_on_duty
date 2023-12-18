def is_power_within_interval():
    try:
        x = int(input("Enter a non-negative integer x: "))
        y = int(input("Enter a non-negative integer y: "))
        l = int(input("Enter the lower bound (l): "))
        r = int(input("Enter the upper bound (r): "))
    except ValueError:
        return "Invalid input. Please enter valid integers for x,y,l,r."

    if x < 0 or y < 0:
        return "x and y must be non-negative integers."

    if l == r:
        return False

    if l >= r:
        return "Error: the lower bound (l) must be less than the upper bound (r)."

    result = l <= x ** y <= r

    if result:
        return f'{x}^{y} is within the interval [{l}, {r}].'
    else:
        return f'{x}^{y} is NOT within the interval [{l}, {r}].'


print(is_power_within_interval())
