def BigMinus(s1: str, s2: str) -> str:
    if s1 == s2:
        return '0'

    if s2 > s1:
        s1, s2 = s2, s1
    index: int = len(s1)
    s2 = s2.rjust(index, '0')

    result: str = ''
    ostatok = 0
    for i in range(index - 1, -1, -1):
        if int(s1[i]) < int(s2[i]):
            digit = 10 + int(s1[i]) - int(s2[i]) - ostatok
            ostatok = 1
        else:
            digit = int(s1[i]) - int(s2[i]) - ostatok
            ostatok = 0
        result = str(digit) + result

    return result
