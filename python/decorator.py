"""
A decorator is a callable object that takes another function as an argument. The decorator processes the function
to be decorated and then returns it or replaces it with another function or callable object
"""


def deco(func):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


if __name__ == '__main__':
    target()
