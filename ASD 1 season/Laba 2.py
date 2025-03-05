import re

OPERATORS = {
    '+': (1, lambda a, b: a + b),
    '-': (1, lambda a, b: a - b),
    '*': (2, lambda a, b: a * b),
    '/': (2, lambda a, b: a // b)  # Целочисленное деление
}


def infix_to_postfix(tokens):
    stack = []
    output = []
    for token in tokens:
        if token.isdigit():
            output.append(int(token))
        elif token == '(':
            stack.append(token)
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                output.append(top_token)
                top_token = stack.pop()
        else:
            while stack and stack[-1] != '(' and OPERATORS[stack[-1]][0] >= OPERATORS[token][0]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return output


def evaluate_postfix(postfix_expression):
    stack = []
    for token in postfix_expression:
        if isinstance(token, int):
            stack.append(token)
        else:
            arg2 = stack.pop()
            arg1 = stack.pop()
            operation = OPERATORS[token][1]
            result = operation(arg1, arg2)
            stack.append(result)

    return stack.pop()


def main():
    expression = input().strip()[:-1]  # Читаем ввод до символа '='
    tokens = list(expression.replace(" ", ""))
    postfix_expression = infix_to_postfix(tokens)
    result = evaluate_postfix(postfix_expression)
    print(result)


if __name__ == "__main__":
    main()
