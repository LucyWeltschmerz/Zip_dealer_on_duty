def find_min_value_key(s):
    d = {}
    for char in s:
        if char.isalpha():
            d[char] = d.get(char, 0) + 1
    min_value = min(d, key=d.get)
    print(f"The key with the lowest value is: {min_value}")

sentence = "Beaches are cool places to visit in spring however the Mackinaw Bridge is  near. Most people visit Mackinaw later since the island is a cool place to explore."

find_min_value_key(sentence)
