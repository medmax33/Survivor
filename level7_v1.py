def WordSearch(line_width: int, s: str, subs: str) -> list:

    # split s array in list
    s_list: list = list(s.split())

    line: list = []
    result: list = []
    average: str = ''

    # split all words in array that more than line_width
    for i in range(len(s_list)):
        if len(s_list[i]) > line_width:
            k = s_list[i]
            s_list.insert(i, k[line_width:])
            s_list.insert(i, k[:line_width] + '-')
            s_list.remove(k)

    # join words into lines and check subs
    for i in range(len(s_list)):
        if len(average + s_list[i]) <= line_width + 1:
            average += s_list[i] + ' '
        else:
            line.append(average)
            average = s_list[i] + ' '
    line.append(average)

    # find subs only separated by spaces, or/and in beginning
    # all subs check in lowercase
    for li in line:
        if li.lower().startswith(subs.lower() + ' ') or ' ' + subs.lower() + ' ' in li:
            result.append(1)
        else:
            result.append(0)

    return result
