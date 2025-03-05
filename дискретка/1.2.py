def stack_update(char, stack):
    print(stack)
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
    previous_char_multiply = "0"
    last_char = input_string[0]
    for i in input_string:
        if i.isdigit():
            previous_char_multiply += i
        else:
            previous_char_multiply = int(previous_char_multiply)
            while True:  # имитация цикла do while
                errors += stack_update(last_char, stack)
                if previous_char_multiply <= 0:
                    break
                previous_char_multiply -= 1
            previous_char_multiply = "1"
            last_char = i

    for _ in range(int(previous_char_multiply)): # проверка на число в конце записи
        errors += stack_update(last_char, stack)
    return True if errors + len(stack) == 0 else errors + len(
        stack)  # возвращаем True если всё верно, иначе количество ошибок


"""print(check_brackets("()((())){}({}[][])()"))
print(check_brackets(")()((())){}({}[][])()"))
print(check_brackets("()((())){}({}[][])())"))
print(check_brackets(")))))((((("))
print(check_brackets("()()10"))"""
print(check_brackets("(3)3"))
