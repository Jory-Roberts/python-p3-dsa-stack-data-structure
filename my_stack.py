def reverse_string(string):
    stack = []

    for char in string:
        stack.append(char)

    reversed = ""
    while stack:
        reversed += stack.pop()

    return reversed


print(reverse_string("hello"))


def evaluate_keystrokes(string):
    stack = []

    for char in string:
        stack.pop() if char == "<" else stack.append(char)

    result = ""
    while stack:
        result = stack.pop() + result

    return result


print(evaluate_keystrokes("abcde<fg<h"))
