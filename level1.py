def squirrel(n: int) -> int:
    f = 1

    if n == 0:
        return f

    for i in range(1, n + 1):
        f *= i
    s = str(f)
    f = int(s[0])

    return f
