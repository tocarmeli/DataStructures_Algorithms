# Finds gcf between 2 numbers, where n1 > n2 using recursion

def gcf(n1, n2):
    assert n1 > n2 and int(n1) == n1 and int(n2) == (n2), 'First # must be > than second #. Both # must be int'
    if n1 < 0:
        n1 *= -1
    if n2 < 0:
        n2 *= -1
    if n2 == 0:
        return n1
    return gcf(n2, n1 % n2)