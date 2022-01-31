# Calculates a number to the 'exp' power using recursion

def power(base, exp):
    assert int(exp) == exp and exp >= 0, 'Exponent must be of type int and positive'
    if exp == 0:
        return 1

    if exp == 1:
        return base

    return base * power(base, exp - 1)

print(power(7,3))