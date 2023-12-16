def triangle_type(x, y, z):
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or x == z or y == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"


print(triangle_type(6, 8, 12))