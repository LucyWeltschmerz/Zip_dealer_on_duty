def is_pangram(sentence):

    unique_letters = set()

    for char in sentence.lower():
        if char.isalpha():
            unique_letters.add(char)
    return len(unique_letters) == 26

print(is_pangram("The quick brown fox jumps over the lazy dog"))