from math import sqrt


def quadratic_function(a: int, b: int, c: int) -> list:
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        return []
    elif delta == 0:
        x0 = -b / (2 * a)
        return [x0]
    else:
        # x1 = (-b - (delta ** 0.5)) / (2 * a)
        x1 = (-b - sqrt(delta)) / (2 * a)
        # x2 = (-b + (delta ** 0.5)) / (2 * a)
        x2 = (-b + sqrt(delta)) / (2 * a)
        return [x1, x2]


def my_sqrt(number: int) -> float:
    return number ** 0.5


def harmonic_element(n: int) -> float:
    return 1 / n
