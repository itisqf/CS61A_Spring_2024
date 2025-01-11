#Q4: Unique Digits
def has_digit(n, k):
    while n!=0:
        if k == (n % 10):
            return True
        else:
            n = n // 10
    return False

def unique_digits(n):
    """
    >>> unique_digits(8675309)
    7
    >>> unique_digits(13173131)
    3
    >>> unique_digits(101)
    2
    """
    unique = 0
    while n > 0:
        k = n % 10
        n = n // 10
        if not has_digit(n, k):
            unique = unique + 1
    return unique