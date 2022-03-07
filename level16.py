def MaximumDiscount(n: int, price: list) -> int:

    # check price length integrity
    if n != len(price):
        return -1

    disc_block = n // 3
    if disc_block == 0:
        return 0

    # sorting price descending
    price.sort(reverse=True)

    # split price by discount groups in 3
    price_discount: list = []
    for _ in range(0, n, 3):
        price_discount.append(price[_:_ + 3])

    # calculate sum of discount

    discount: int = 0
    for _ in range(disc_block):
        discount += price_discount[_][2]

    return discount
