def MadMax(N: int, Tele: list) -> list:
    if N != len(Tele):
        return [0, 0, 0]

    Tele.sort()
    mid = len(Tele) // 2

    Tele_impuls = []

    for i in range(mid):
        Tele_impuls.append(Tele[i])

    Tele_impuls.append(Tele[N - 1])

    for i in range(-2, mid - N - 1, -1):
        Tele_impuls.append(Tele[i])

    return Tele_impuls
