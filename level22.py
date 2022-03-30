def SherlockValidString(s: str) -> bool:
    array = []
    while s:
        array.append(s.count(s[0]))
        s = s.replace(s[0], '')

    k = 0
    sr_ar = int(sum(array) / len(array) + 0.5)
    for i in array:
        k += abs(i - sr_ar)

    if k <= 1:
        return True
    else:
        return False
