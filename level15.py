def TankRush(h1: int, w1: int, s1: str, h2: int, w2: int, s2: str) -> bool:

    try:

        # check integrity
        if h1 < h2 or w1 < w2:
            return False

        # make list from string
        array1 = list(s1.split())
        array2 = list(s2.split())

        # check assertion in arrays
        assert h1 == len(array1), 'h1 not equal len s1'
        assert h2 == len(array2), 'h2 not equal len s2'
        assert w1 == len(array1[0]), 'w1 not equal len s1'
        assert w2 == len(array2[0]), 'w2 not equal len s2'

        # if h2 == 0 or w2 == 0:
        #     return True

        # find indexes of first line array2 in array1
        for i in range(len(array1) - len(array2) + 1):
            if array2[0] in array1[i]:
                j = array1[i].index(array2[0])
                if DefArray(i, j, array1, array2):
                    return True
            else:
                continue

        return False

    except IndexError:
        return False


def DefArray(i: int, j: int, array1: list, array2: list) -> bool:
    for _ in range(len(array2)):
        if array2[_] != array1[i + _][j:j + len(array2[_])]:
            return False
    return True


print(TankRush(3, 4, '1234 2345 0987', 2, 2, '34 98'))