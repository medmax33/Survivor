def MatrixTurn(Matrix: list, m: int, n: int, t: int) -> type(None):

    for _ in range(t):
        Matrix = matrix_rotation(m, n, Matrix)

    # return None


def matrix_rotation(h: int, w: int, tree: list) -> list:

    new_tree = []
    for i in range(h):
        new_tree.append(list(tree[i]))

    for i in range(h):
        for j in range(w):
            if i < h / 2 and i <= j < (w - 1) - i:
                new_tree[i + 0][j + 1] = tree[i][j]
            elif i >= h / 2 and (h - 1) - i < j <= w + (i - h):
                new_tree[i + 0][j - 1] = tree[i][j]
            elif j <= i <= (h - 1) - j and j < w / 2:
                new_tree[i - 1][j + 0] = tree[i][j]
            elif (w - 1) - j <= i <= h + (j - w) and j >= w / 2:
                new_tree[i + 1][j + 0] = tree[i][j]

    for i in range(h):
        new_tree[i] = ''.join(new_tree[i])

    return new_tree
