def split_string(a):
    mult = list(map(lambda x: int(x) if x else None,
                    a.replace("(", "*").replace(")", "*").replace("[", "*").replace("]", "*").split("*")[1:]))
    brackets = list(filter(lambda x: True if x in "()[]" else False, a))
    res = ""
    for i in range(len(brackets)):

        if mult[i]:
            multiplier = mult[i]
        else:
            multiplier = 1
        res += multiplier * brackets[i]
    return res


def stack_update(char, stack):
    if char in "([":  # если скобка открывающаяся, то записываем её в стек
        stack.append(char)
        return 0
    elif char in ")]":  # если скобка закрывается
        if len(stack) == 0:  # проверяем на непустой стек
            return 1
        elif (char == ")" and stack[-1] == "(") or (
                char == "]" and stack[-1] == "["):  # если скобка "правильно" закрылась, то удаляем её из стека
            stack.pop()
            return 0
        else:
            return 1  # иначе считаем ошибку
    return 0


def check_brackets(input_string: str):
    stack = list()  # импровизированный стек
    errors = 0

    for i in split_string(input_string):
        errors += stack_update(i, stack)

    return True if errors + len(stack) == 0 else errors + len(
        stack)  # возвращаем True если всё верно, иначе количество ошибок


print(check_brackets("()((()))([][])()"))
print(check_brackets(")()((()))([][])()"))
print(check_brackets(")))))((((("))
print(check_brackets("()()10"))
print(check_brackets("(3)3"))
print(check_brackets("(2025)2024"))
