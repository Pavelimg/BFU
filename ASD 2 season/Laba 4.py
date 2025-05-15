def kmp_search(pattern, text):
    """
    Реализация алгоритма Кнута-Морриса-Пратта для поиска подстроки.
    Возвращает список индексов начала вхождений pattern в text.
    """

    def compute_lps_array(pat):
        """Вычисляет массив longest proper prefix which is also suffix"""
        lps = [0] * len(pat)
        length = 0  # длина предыдущего longest prefix suffix
        i = 1

        while i < len(pat):
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    if not pattern:
        return []

    lps = compute_lps_array(pattern)
    result = []
    i = 0  # индекс для text
    j = 0  # индекс для pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

            if j == len(pattern):
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result


# Пример использования
if __name__ == "__main__":
    text = "ABABDABACDABABCABAB"
    pattern = "ABABCABAB"
    matches = kmp_search(pattern, text)
    print(f"Образец найден на позициях: {matches}")
