def Football(f: list, n: int) -> bool:
    if f:
        k: list = []
        m: list = []
        f_up: list = f.copy()
        f_up.sort()

        for i in range(n):
            if f[i] != f_up[i] and f[i] > f[i + (1 if i < n-1 else 0)]:
                k.append(i)
                m.append(1)
            elif f[i] != f_up[i]:
                k.append(i)
                m.append(0)
            else:
                m.append(0)

        if len(k) == 0:
            return False
        elif len(k) == 2:
            return True
        elif len(k) > 2 and 0 not in m[k[0]:k[-1]]:
            return True
        else:
            return False

    return False
