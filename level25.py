def TransformTransform(a: list, n: int) -> bool:

    if n != len(a):
        return False

    keykey = sum(Transform(Transform(a)))

    if keykey % 2 == 0:
        return True
    return False


def Transform(a: list) -> list:
    b: list = []

    for i in range(len(a)):
        for j in range(len(a) - i):
            k = i + j
            b.append(max(a[j:k + 1]))

    return b
