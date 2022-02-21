def MassVote(n: int, votes: list) -> str:

    # check if n equal len votes
    if n != len(votes) or n < 1:
        return 'n doesn\'t fit length of votes'

    # try to calculate total votes
    try:
        total_votes = 0
        for _ in votes:
            total_votes += _
    except TypeError:
        return 'check data in votes'

    # calculate list of percentage of each candidate
    percentage = []
    for _ in votes:
        percentage.append(round((_ / total_votes) * 100, 3))

    # make sorted list of percentage
    percent: list = sorted(percentage, reverse=True)

    # we have a winner?
    if percent[0] == percent[1]:
        return 'no winner'

    # find number of winner
    k: str = ''
    for i in range(n):
        if max(percentage) == percentage[i]:
            k = str(i + 1)

    # majority or minority?
    if percent[0] > 50:
        return 'majority winner ' + k
    else:
        return 'minority winner ' + k
