def automate(commands, state="S"):  # По умолчанию состояние
    if state == "F":
        return "F"
    elif state == "S":
        if commands[0] == "a":
            return "S" + automate(commands[1:], "A")
        if commands[0] == "b":
            return "S" + automate(commands[1:], "F")
    elif state == "A":
        if commands[0] == "a":
            return "A" + automate(commands[1:], "B")
        if commands[0] == "b":
            return "A" + automate(commands[1:], "C")
    elif state == "B":
        if commands[0] == "a":
            return "B" + automate(commands[1:], "F")
        if commands[0] == "b":
            return "B" + automate(commands[1:], "B")
        if commands[0] == "c":
            return "B" + automate(commands[1:], "A")
    elif state == "C":
        if commands[0] == "a":
            return "C" + automate(commands[1:], "F")
        if commands[0] == "b":
            return "C" + automate(commands[1:], "A") + "C"
    raise SyntaxError("Недопустимая команда")


print(automate("abbbbacba"))  # SACACABACFCC
