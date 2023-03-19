# Napisać dekorator, dla funkcji która nie przyjmuje żadnych argumentów
# oraz niczego nie zwraca, którego zadaniem jest wyświetlenie po wywołaniu
# funkcji napisu "--- KONIEC ---"

# Sprawdzić w praktyce dla dowolnej utworzonej przez Was funkcji.

def line_decorator(func):
    def wrapper():
        func()
        print("--- KONIEC ---")
    return wrapper


@line_decorator
def my_func():
    print("Funkcja")


my_func()
