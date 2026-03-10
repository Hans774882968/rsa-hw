from math import gcd


def mygcd(a, b):
    return a if b == 0 else mygcd(b, a % b)


def egcd(a, b):
    if b == 0:
        return a, 0, a
    x, y, g = egcd(b, a % b)
    return y, x - (a // b) * y, g


cases = [
    (114514, 1919810),
    (22233, 333444),
    (252, 105),
    (1071, 462),
    (32 * 32, 26 * 26),
    (103, 24),
]
for a, b in cases:
    print(egcd(a, b), mygcd(a, b), gcd(a, b))
