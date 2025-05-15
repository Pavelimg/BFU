def run_context_free(n, string="S"):
    string = string.replace("S", "AB")  # S → AB
    for _ in range(n - 1):  # A → 0A1
        string = string.replace("A", "0A1")
    string = string.replace("A", "0.1")  # A → 0.1
    string = string.replace("B", "001")  # B → 001
    return string


def run_normal_homski(n, string="S"):
    string = string.replace("S", "AB")  # S → AB
    for _ in range(n - 1):  # A → CA
        string = string.replace("A", "CA")
    string = string.replace("A", "CF")  # A → CF
    string = string.replace("F", "ED")  # F → ED

    string = string.replace("B", "CG")  # B → 001
    return string


print(run_context_free(1))
