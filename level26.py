def white_walkers(village: str) -> bool:
    ind = []

    for i in range(len(village)):
        if '1' <= village[i] <= '9':
            ind.append(i)
    if len(ind) < 2:
        return False

    for i in range(len(ind) - 1):
        if int(village[ind[i]]) + int(village[ind[i + 1]]) == 10 and village[ind[i]:ind[i + 1] + 1].count('=') != 3:
            return False
    return True
