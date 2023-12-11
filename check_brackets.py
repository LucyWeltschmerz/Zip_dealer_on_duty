def check_brackets(s):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    return not stack


print(check_brackets("()"))
print(check_brackets("{}"))
print(check_brackets("[{}]"))
print(check_brackets("([)]"))
