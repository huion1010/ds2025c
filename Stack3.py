def is_valid_brackets(expression : str) -> bool:
    stack = []
    brackets = {')' : '(', '{' : '}', ']' : '['}

    for i in expression:
        if i in brackets.values():
            stack.append(i)
        if i in brackets.keys():
            if not stack or stack.pop() != brackets[i]:
                return False
    return len(stack) == 0

print(is_valid_brackets("(]2+3)["))
print(is_valid_brackets("(2+{3*9})"))
print(is_valid_brackets("(2+(3+9))"))
