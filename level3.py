def fill_field(N: int, M: int, battalion_pair: list) -> list:
    # fill whole field with '0' and '1' - where battalion fall
    state_square = []  # whole field M*N
    for x in range(M):
        row = []
        for y in range(N):
            if (y, x) in battalion_pair:
                row.append(1)
            else:
                row.append(0)
        state_square.append(row)
    return state_square


def refactor_battalion(battalion: list) -> list:
    # split battalion by pair
    battalion_pair = []  # battalion array split by pair of coordinate

    for k in range(0, len(battalion), 2):
        battalion_pair.append((battalion[k] - 1, battalion[k + 1] - 1))

    return battalion_pair


def ConquestCampaign(N: int, M: int, L: int, battalion: list) -> int:
    # N is a vertical, equal y
    # M is a horizontal, equal x
    neighbor = [0, 1, 0, -1, 0, 1, 0]  # service array for capture cells

    # check if battalion fit L
    if len(battalion) / L != 2:
        return -1

    battalion_pair = refactor_battalion(battalion)

    state_square = fill_field(N, M, battalion_pair)

    flag = 1  # flag for checking empty cells
    day = 1  # var to count days of capture

    # main cycle
    while flag:
        flag = 0
        day += 1

        # enumeration of whole field for uncaptured cells
        for x in range(M):
            for y in range(N):
                if state_square[x][y] == 0:
                    flag += 1  # count zero cells
                if state_square[x][y] == day - 1:  # find shaded cells
                    for nei in range(4):  # cycle to find cells to capture
                        xi = x + neighbor[nei]
                        yi = y + neighbor[nei + 3]
                        if xi < 0 or yi < 0 or xi >= M or yi >= N:  # only in field
                            continue
                        elif state_square[xi][yi] == 0:  # capture zero cell
                            state_square[xi][yi] = day

    return day - 1
