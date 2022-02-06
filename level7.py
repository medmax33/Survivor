def WordSearch(len: int, s: str, subs: str) -> list:
    # create array for formated lines
    lines = []
    # create array of '0' and '1' for lines with 'subs'
    res = []

    # begin format with 0 position
    start = 0
    finish = start

    while (s.count('') - 1) - start >= len:
        start = finish

        # delete space in beginning of line
        if s[start] == ' ':
            start += 1

        # check if in 'len' line is more of one word
        if s.count(' ', start, start + len) == 0:
            finish = start + len
        else:
            finish = s.rfind(' ', start, start + len)

        # add new formatted line
        lines.append(s[start:finish])

        # check if subs
        if s[start - 1:finish + 1].count(' ' + subs + ' '):
            res.append(1)
        else:
            res.append(0)

    return res
