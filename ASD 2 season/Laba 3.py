def build_finite_automaton(pattern):
    m = len(pattern)
    alphabet = set(pattern)  # Получаем уникальные символы
    transition_table = [{} for _ in range(m + 1)]

    for state in range(m + 1):
        for char in alphabet:
            # Находим максимальный префикс, который является суффиксом pattern[:state] + char
            next_state = min(m, state + 1)
            while next_state > 0 and pattern[:next_state] != (pattern[:state] + char)[-next_state:]:
                next_state -= 1
            transition_table[state][char] = next_state

    return transition_table


def finite_automaton_search(text, pattern):
    if len(pattern) == 0:
        return [0]  #

    transition_table = build_finite_automaton(pattern)
    state = 0
    results = []

    for i in range(len(text)):
        char = text[i]
        # Переход по таблице (используем char, если он есть в таблице, иначе 0)
        state = transition_table[state].get(char, 0)
        if state == len(pattern):
            results.append(i - len(pattern) + 1)  # Найденное вхождение

    return results


tests = [
    ("ABABDABACDABABCABAB", "ABABCABAB"),
    ("hello world", "world"),
    ("hello world", "hello"),
    ("aaaaa", "aa"),
    ("abcde", ""),
    ("a", "a"),
    ("a", "b"),
    ("", "abc"),
    ("", ""),
    ("ababababab", "aba"),
    ("mississippi", "issi"),
    ("aaaabaaaab", "aaaab"),
    ("abcabcabc", "abcabc"),
]

for a, b in tests:
    print(f'Вхожение строки "{a}" в строку "{b}"  на позициях {finite_automaton_search(a, b)}')
