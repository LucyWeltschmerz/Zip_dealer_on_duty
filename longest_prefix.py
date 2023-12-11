def longest_common_prefix(s):
    if not s:
        return " "

    s.sort()
    first_s = s[0]
    last_s = s[-1]

    common_prefix = []

    for i in range(len(first_s)):
        if i < len(last_s) and first_s[i] == last_s[i]:
            common_prefix.append(first_s[i])
        else:
            break

    return "".join(common_prefix)


input_1 = ["freedom", "freeze", "freesia"]
input_2 = ["fog", "car", "foot"]

print("longest common prefix is: ", longest_common_prefix(input_1))
print("longest common prefix is: " ,longest_common_prefix(input_2))
