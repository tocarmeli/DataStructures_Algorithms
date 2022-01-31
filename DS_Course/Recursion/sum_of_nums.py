# Calculates the sum of the digits of a positive number using a recursive method

def sum(n):
    assert n >= 0 and int(n) == n, 'Not a valid positive integer'
    if n < 10 and n >= 0:
        return n
    return sum(n // 10) + (n % 10)