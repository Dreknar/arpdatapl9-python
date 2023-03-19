def trigger_info(func):
    def wrapper(*args, **kwargs):
        print(f"Wywołano funkcję {func}")
        return func(*args, **kwargs)
    return wrapper


@trigger_info
def my_add(a: float, b: float) -> float:
    return a + b


@trigger_info
def my_sub(a: float, b: float) -> float:
    return a - b


print(my_sub(10, 2))
print(my_add(10, 2))