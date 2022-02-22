def UFO(n: int, data: list, octal: bool) -> list:
    try:
        # check data length
        if n != len(data):
            return [0]

        result: list = []
        for _ in data:
            if octal:
                result.append(int(str(_), 8))
            else:
                result.append(int(str(_), 16))

        return result

    except TypeError:
        return [0]
