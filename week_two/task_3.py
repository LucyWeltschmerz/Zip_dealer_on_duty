def color_invert(rgb_tuple):

    inverted_color = tuple(255 - value for value in rgb_tuple)
    return inverted_color


print(color_invert((255, 255, 255)))
print(color_invert((0, 0, 0)))
print(color_invert((165, 170, 221)))