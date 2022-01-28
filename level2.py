def odometer(oxana: list) -> int:

    # Check pair in oxana
    if len(oxana) % 2 != 0:
        oxana.append(oxana[-2])

    dist = oxana[0] * oxana[1]

    for n in range(2, len(oxana), 2):
        time_n = oxana[n + 1] - oxana[n - 1]
        if time_n < 0:
            return -1
        dist += oxana[n] * time_n

    return dist
