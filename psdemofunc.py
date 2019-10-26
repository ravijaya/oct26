"""demo for the function"""


def power(x, n=0):   # default arguments
    """function definition"""
    return x ** n


if __name__ == '__main__':
    result = power(4, 5)  # function call
    print(result)
