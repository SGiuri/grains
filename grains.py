def square(number):
    if 0 < number < 65 and number == int(number):
        return 2 ** (number - 1)

    raise ValueError("Not positive natural number")


def total():
    return 2 ** (64) - 1
