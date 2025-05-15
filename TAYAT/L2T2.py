def automate(commands, state="0"):  # По умолчанию состояние
    if len(commands) == 0:
        return ""
    elif state == "0":
        if commands[0] == "a":
            return "0" + automate(commands[1:], "1")
    elif state == "1":
        if commands[0] == "b":
            return  "1" +automate(commands[1:], "2")
    elif state == "2":
        if commands[0] == "a":
            return "2" + automate(commands[1:], "3")
        if commands[0] == "b":
            return "2" + automate(commands[1:], "(0,1)")
    elif state == "3":
        if commands[0] == "b":
            return "3" + automate(commands[1:], "1")
    elif state == "(0,1)":
        if commands[0] == "a":
            return "(0,1)" + automate(commands[1:], "1")
        if commands[0] == "b":
            return "(0,1)" + automate(commands[1:], "2")
    raise SyntaxError("Недопустимая команда")


print(automate("ababbbba")) # 012312(0,1)2
