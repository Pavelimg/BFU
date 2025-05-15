def automate(commands, state="0"):  # По умолчанию состояние
    if len(commands) == 0:
        return ""
    elif state == "S":
        if commands[0] == "a":
            return "S" + automate(commands[1:], "P1")
        if commands[0] == "b":
            return "S" + automate(commands[1:], "P2")
    elif state == "P1":
        if commands[0] == "a":
            return "P1" + automate(commands[1:], "Q1")
        if commands[0] == "b":
            return "P1" + automate(commands[1:], "P1")
    elif state == "P2":
        if commands[0] == "a":
            return "P2" + automate(commands[1:], "Q2")
        if commands[0] == "b":
            return "P2" + automate(commands[1:], "P2")
    elif state == "Q1":
        if commands[0] == "a":
            return "Q1" + automate(commands[1:], "R")
        if commands[0] == "b":
            return "Q1" + automate(commands[1:], "Q1")
    elif state == "Q2":
        if commands[0] == "a":
            return "Q2" + automate(commands[1:], "P2")
        if commands[0] == "b":
            return "Q2" + automate(commands[1:], "Q2")
    elif state == "R":
        if commands[0] == "a":
            return "R" + automate(commands[1:], "Q1")
        if commands[0] == "b":
            return "R" + automate(commands[1:], "R")
    raise SyntaxError("Недопустимая команда")


print(automate(""))
