def demo(*args):
    """variable len parameter"""
    print(args)


if __name__ == '__main__':
    # demo()
    # demo(123)
    # demo(1, 2, 'iii', 4, 5)

    items = [11, 22, 33] * 3
    demo(items)
    demo(*items)  # content of the object as arguments
    print()

    items = (11, 22, 33)
    demo(items)
    demo(*items)
