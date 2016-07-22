def sqrt_func(x):
    '''compute square roots using the method of Heron of Alexandria.

    Args:
        x: The number for which the square root is to be computed
    Returns:
        The square root of x.
    '''

    if x < 0:
        raise ValueError("Cannot comoute square root of negative number {}".format(x))

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x/guess) / 2.0
        i += 1
    return guess

def main():
    print(sqrt_func(9))
    print(sqrt_func(2))
    try:
        print(sqrt_func(-1))
    except ZeroDivisionError:
        print("Cannot compute square root of a negative number.")

    print("Program executioon continues normally here.")

if __name__ == '__main__':
    main()