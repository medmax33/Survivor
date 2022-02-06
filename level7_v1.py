def wordsearch(line_width: int, s: str, subs: str) -> list:
    # create array of '0' and '1' for lines with 'subs'
    res = []

    # begin format with 0 position
    start = 0

    while len(s) - start > 0:
        # delete space in beginning of line
        if s[start] == ' ':
            start += 1

        # check if in 'len' line is more of one word
        if s.count(' ', start, start + line_width) == 0:
            finish = start + line_width
        else:
            finish = s.rfind(' ', start, start + line_width)

        if finish > len(s):
            finish = len(s)

        # check if subs
        if s[start:finish + 1].count(subs + ' '):
            res.append(1)
        else:
            res.append(0)

        start = finish

    return res
