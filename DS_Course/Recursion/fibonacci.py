# Uses recursion to calculate the nth digit in a fibonacci sequence

def fibonacci(num):
    assert num >= 0 and int(num) == num, 'Invalid number for fibonacci sequence.'
    if num < 2 and num >= 0:
        return num
    return fibonacci(num -1) + fibonacci(num - 2)