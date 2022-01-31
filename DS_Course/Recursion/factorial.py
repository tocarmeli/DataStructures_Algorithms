# Recursive method to find factorial of a num

def factorial(num):
    assert num >= 0 and int(num) == num, 'Num must be positive'
    if num <= 1 and num >= 0:
        return 1
    return num * factorial(num - 1)