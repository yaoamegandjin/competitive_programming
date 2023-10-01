def three_n_plus_one(i, j):
    for n in range(-j):
        if n == 1:
            break
        elif n % 2 == 0:
            n/2
            print(n)
        else:
            n = 3 * n + 1
            print(n)
three_n_plus_one(1, 22)