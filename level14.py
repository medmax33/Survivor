def Unmanned(total_l: int, n: int, track: list) -> int:

    try:
        # check data integrity
        if Data_Integrity(total_l, n, track):
            return -1

        # if no traffic light (TL) or total_l less than distance to first TL
        if n == 0 or total_l < track[0][0]:
            return total_l

        # count traffic stops
        distance = 0  # time to drive total_l

        for i in range(n):

            if i == 0:
                distance += track[i][0]
            else:

                # if current TL distance more than total_l
                if track[i][0] > total_l:
                    distance += total_l - track[i-1][0]
                    return distance

                # normal mode
                else:
                    distance += track[i][0] - track[i-1][0]

            # calculate what light now on current TL
            red_or_green = distance % (track[i][1] + track[i][2])

            # if TL red, wait for green light
            if red_or_green < track[i][1]:
                distance += track[i][1] - red_or_green

        # last traffic time
        distance += total_l - track[n-1][0]

        return distance

    except IndexError:
        return -1


def Data_Integrity(total_l: int, n: int, track: list) -> int:

    # check if total_l negative or zero, check n <-> track integrity
    if total_l <= 0 or n != len(track):
        return 1

    for i in range(len(track)):

        # check red and green time is positive
        if track[i][1] <= 0 or track[i][2] <= 0:
            return 1

        # check distance to previous TL less than current
        if i != len(track) - 1:
            if track[i][0] > track[i+1][0]:
                return 1

    return 0
