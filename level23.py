def TreeOfLife(h: int, w: int, n: int, tree: list) -> list:

    new_tree = plus_to_years(tree, False)

    for _ in range(n):
        if _ % 2 == 0:
            new_tree = even(new_tree)
        else:
            new_tree = odd(h, w, new_tree)

    new_tree = plus_to_years(new_tree, True)

    return new_tree


def plus_to_years(tree: list, revert: bool) -> list:
    new_tree = []

    if revert:
        revert_table = ''.maketrans('1234567890', '++++++++++')
    else:
        revert_table = ''.maketrans('+', '1')

    for _ in tree:
        new_tree.append(_.translate(revert_table))

    return new_tree


def even(new_tree: list) -> list:
    even_tree = []

    even_table = ''.maketrans({'1': '2', '2': '3', '3': '4', '4': '5', '5': '6', '.': '1'})

    for _ in new_tree:
        even_tree.append(_.translate(even_table))

    return even_tree


def odd(h: int, w: int, new_tree: list) -> list:
    odd_tree = []
    odd_table = ''.maketrans({'1': '2', '2': '3', '3': '4', '4': '5', '5': '6'})
    coordinates = []

    for i in range(h):
        odd_tree.append(new_tree[i].translate(odd_table))
        for j in range(w):
            if int(odd_tree[i][j]) >= 3:
                coordinates.append([i, j])

    all_coordinates = coordinates.copy()

    for k in coordinates:
        for _ in [-1, 1]:
            if k[0] + _ < 0 or k[0] + _ >= h:
                continue
            else:
                if [k[0] + _, k[1]] not in all_coordinates:
                    all_coordinates.append([k[0] + _, k[1]])
        for _ in [-1, 1]:
            if k[1] + _ < 0 or k[1] + _ >= w:
                continue
            else:
                if [k[0], k[1] + _] not in all_coordinates:
                    all_coordinates.append([k[0], k[1] + _])

    for i, j in all_coordinates:
        array = list(odd_tree[i])
        array[j] = '.'
        odd_tree[i] = ''.join(array)

    return odd_tree
