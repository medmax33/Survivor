def TheRabbitsFoot(s: str, encode: bool) -> str:

    if encode:
        return encrypting(s)
    else:
        return decrypting(s)


def encrypting(s: str) -> str:

    # delete all spaces
    s = s.replace(' ', '')

    # define length of array
    s_len = len(s)
    line = int(s_len ** 0.5 + 0.5)
    column = int(s_len ** 0.5 + 1)

    # add one line if all characters doesn't fit array
    if line * column < s_len:
        line += 1

    # add spaces in empty cells
    s += ' ' * (line * column - s_len)

    # rebuild string in array
    array = []
    start = 0
    for _ in range(line):
        finish = start + column
        array.append(s[start:finish])
        start = finish

    # encrypting string
    encrypt = ''
    for j in range(column):
        for i in range(line):
            if array[i][j] == ' ':
                continue
            encrypt += array[i][j]
        if j != column - 1:
            encrypt += ' '

    return encrypt


def decrypting(s: str) -> str:
    # split string into words
    s = s.split()

    # define length of array
    line: int = len(s)
    column: int = len(s[0])

    # add spaces in empty cells
    for i in range(line):
        if len(s[i]) < column:
            s[i] += ' '

    # decrypting
    decrypt: str = ''
    for j in range(column):
        for i in range(line):
            if s[i][j] == ' ':
                continue
            decrypt += s[i][j]
    return decrypt
