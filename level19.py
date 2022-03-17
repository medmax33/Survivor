def ShopOLAP(n: int, items: list) -> list:
    # check length of items
    if n != len(items):
        return [0, 0]

    split_items = []
    for _ in range(n):
        split_items.append(items[_].split())
        split_items[_][1] = int(split_items[_][1])

    split_items.sort()
    i = 1
    while i < len(split_items):
        if split_items[i - 1][0] == split_items[i][0]:
            split_items[i - 1][1] += split_items[i][1]
            split_items.remove(split_items[i])
        else:
            i += 1

    split_items = sorted(reverse_items(split_items), reverse=True)

    for i in range(1, len(split_items)):
        if split_items[i - 1][0] == split_items[i][0] and split_items[i - 1][1] > split_items[i][1]:
            split_items.insert(i - 1, split_items.pop(i))

    split_items = reverse_items(split_items)

    final = []
    for i in range(len(split_items)):
        final.append(f'{split_items[i][0]} {split_items[i][1]}')

    return final


def reverse_items(items: list) -> list:
    rev_item = []
    for i in range(len(items)):
        rev_item.append([items[i][1], items[i][0]])

    return rev_item
