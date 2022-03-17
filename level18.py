def MisterRobot(n: int, data: list) -> bool:

    # check length of data
    if n != len(data):
        return False

    # checking all n digits in data
    for _ in range(n):
        if _ + 1 in data:
            continue
        else:
            return False

    for i in range(1, n):
        # do rotation while i is in zero position
        while data[0] != i:
            # if length of data is 2 and we have ex. [5, 4] -> False
            if len(data) > 2:
                rotate(i, data)
            else:
                return False
        data.pop(0)

    return True


def rotate(i: int, data: list) -> list:
    final = data.index(i)
    if final >= 2:
        start = final - 2
    else:
        start = 0
    while data[start] != i:
        data.insert(start + 2, data.pop(start))

    return data
