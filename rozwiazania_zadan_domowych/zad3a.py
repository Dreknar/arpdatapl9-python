def trigger_base(func):
    def wrapper(*args):
        func(*args)
        count_of_star = 0
        for i in range(1, args[0] + 1):
            count_of_star += i
        print("-" * count_of_star)
        print(f"Suma gwiazdek: {count_of_star}")
    return wrapper


@trigger_base
def print_asterix(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(i):
            print("*", end="")
        print()


print_asterix(3)
