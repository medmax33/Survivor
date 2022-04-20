def Keymaker(k: int) -> str:
    trigger = ''.maketrans({'1': '0', '0': '1'})

    result = []
    for _ in range(k):
        result.append('0')

    for i in range(k):
        for _ in range(i, k, i + 1):
            result[_] = result[_].translate(trigger)

    return ''.join(result)
