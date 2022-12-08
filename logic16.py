def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a > 9999 and a < 100000 and type(a) == int
print(main(10087))
print(main(1008))

