def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    n1 = x % 10
    n2 = x // 10 % 10
    n3 = x // 100
    return (x%11==0) or (x == (n1*100 + n2*10 + n3))