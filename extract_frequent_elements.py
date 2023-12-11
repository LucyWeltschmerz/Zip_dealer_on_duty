def extract_frequent_elements(elements, k):
    d = {}
    for element in elements:
        d[element] = d.get(element, 0) + 1

    result = []
    for element, frequency in d.items():
        if frequency > k:
            result.append(element)
    return result


example_1 = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k1 = 3
example_2 = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
k2 = 2

print("Output is: ", extract_frequent_elements(example_1, k1))
print("Output is: ", extract_frequent_elements(example_2, k2))