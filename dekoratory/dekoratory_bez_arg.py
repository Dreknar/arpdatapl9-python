def line_decorator(func):
    def wrapper():
        print(f"**********************************************")
        func()
        print(f"**********************************************")
    return wrapper


@line_decorator
def my_date() -> None:
    print(f"Dzisiaj jest: 19-03-2023")


@line_decorator
def my_course() -> None:
    print(f"Kurs to: ARPDataPL9")


my_date()
my_course()
