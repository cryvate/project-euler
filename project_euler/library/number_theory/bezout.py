def bezout(a: int, b: int) -> int:
    x, y = 0, 1
    u, v = 1, 0

    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q

        b, a = a, r
        x, y = u, v
        u, v = m, n

    return x, y
