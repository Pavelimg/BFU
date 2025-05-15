def automate(actions):
    output = ""
    for action in actions:
        if len(action) == 1:
            output += "ba" + "c" * action[0]
        if len(action) == 2:
            output += "a" + "b" * action[0] + "a" * action[1] + "b"
    return output


print(automate([(1, 4), (5,), (2, 3)]))  #abaaaabbacccccabbaaab
