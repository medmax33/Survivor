def LineAnalysis(line: str) -> bool:
    # fixing length of line
    ll = len(line)

    # check * in the beginning and end of line
    if line[0] != '*' or line[-1] != "*":
        return False

    # check line is 1 or 2 symbols
    if ll == 1 or ll == 2:
        return True

    # find repeating string
    for i in range(1, ll):
        if line[i] == '*':
            rep = i + 1
            break

    # check if repeating string equal line
    if rep == ll:
        return True

    repeating = line[0:rep]

    # check if line consist from some repeating string
    if (ll + 1) % rep != 0:
        return False

    # check every block equal repeating string
    j = rep - 1
    while j < ll - 1:
        if line[j: j + rep] != repeating:
            return False
        j += rep - 1

    return True
