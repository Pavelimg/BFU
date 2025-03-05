def check_brackets(input_string: str) -> bool:
    stack = list()  # импровизированный стек
    for i in input_string:
        if i in "({[":  # если скобка открывающаяся, то записываем её в стек
            stack.append(i)
        elif i in ")}]":  # если скобка закрывается
            if len(stack) == 0:  # проверяем на непустой стек
                return False
            if (i == ")" and stack[-1] == "(") or (i == "}" and stack[-1] == "{") or (
                    i == "]" and stack[-1] == "["):  # если скобка "правильно" закрылась, то удаляем её из стека
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False


print(check_brackets("1(FDS)32 2FDS F() }({}[][])()"))



