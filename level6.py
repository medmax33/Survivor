def PatternUnlock(N: int, hits: list) -> str:
    if N != len(hits):
        return 'error'

    d1: list = [2, 4, 6, 7, 9]
    d2: list = [1, 3, 5, 8]
    digits: float = 0

    for i in range(N - 1):
        if hits[i] in d1 and hits[i + 1] in d1:
            digits += 1.414214
        elif hits[i] in d2 and hits[i + 1] in d2:
            digits += 1.414214
        else:
            digits += 1.0
    digits = round(digits, 5)

    code = str(digits)
    code = code.replace('0', '').replace('.', '')

    return code
