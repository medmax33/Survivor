def SumOfThe(n: int, data: list) -> int:

    # test if n equal length data
    if n != len(data):
        return -1000000000000000000000000

    summ: int = 0  # summa of data

    try:
        for x in data:
            summ += x
        summ = int(summ / 2)  # summa of all data is 2 * answer

        # check if answer in data array
        if summ in data:
            return summ
        else:
            return 1000000000000000000000000

    except TypeError:
        return -1000000000000000000000000
    except ZeroDivisionError:
        return -1000000000000000000000000
