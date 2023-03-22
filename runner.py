from figures.flat import *

aliases = {
    "ra": rectangle_area,
    "rc": rectangle_circuit
}

# rectangle_area(10, 10)
aliases.get("XX", print)(10, 10)