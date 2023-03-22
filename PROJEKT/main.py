from datetime import datetime as dt, timedelta as td
from random import randint, uniform

now = dt.now()
file_name = f"dane_{now.strftime('%Y%m%d')}.txt"

for _ in range(10):
    with open(file_name, "a", encoding="utf-8") as file:
        for _ in range(100):
            time = now - td(hours=randint(-24, 24), minutes=randint(-60, 60))
            # time = f"{randint(0,23):2d}:{randint(0,59):2d}".replace(" ", "0")
            first_value = str(randint(0, 100))
            second_value = str(round(uniform(0.1, 1.0), 2))
            row = time.strftime("%H:%M") + ";" + first_value + ";" + second_value + "\n"
            file.write(row)
