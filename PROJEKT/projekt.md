# Zadanie 01

Napisz program który pozwoli wygenerować dowolną liczbę (wierszy) danych według poniższego schematu

* godzina:minuta
* wartość od 0 do 100
* wartość od 0.1 do 1.0

Każde wartości powinny być oddzielone średnikami ```czas;war1;war2```

W przypadku losowości wartości użyjecie randint oraz uniform (obie znajdują się w random)
Natomiast godzina:minuta ma być również losowana
(do funkcji timedelta wykorzystać randint)

nazwa pliku: ```dane_dzienmiesiacrok```

# Zadanie 02

Wykorzystując dane z ```Zadanie 01```:

Dodać nową kolumnę do pliku (można do nowego), która będzie wynikiem 
operacji matematycznej: kol2 * kol3, natomiast pierwsza kolumna ma posiadać informacje tylko o godzinie.

Ostatecznie:

* Godzina
* war1 (0-100)
* war2 (0.1-1.0)
* war1 * war2

# Zadanie 03

Z utworzonego pliku w ```zadaniu nr 2``` znajdźcie największą wartość ostatniej kolumny dla każdej godziny 