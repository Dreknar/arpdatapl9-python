def summary(*args) -> int:
    print(f"Elements: {args}")
    result = 0
    for i in args:
        result += i

    return result


def fun_with_option(**kwargs):
    if kwargs.get("power", -1) == -1:
        print("Nie opcji potęgi")
    else:
        print(2 ** kwargs.get("power", -1))

    if kwargs.get("sqrt", False):
        print("Chciałeś pierwiastkować?")
    else:
        print("Opcja sqrt jest na false")


fun_with_option(power=3, alamakota=True)


def roar_value(prefix: str, *args) -> None:
    for i in args:
        print(f"{prefix} -> {i}")


roar_value("Krzyczę!", 2, 3, 4, 6, 1, 0, 9)

