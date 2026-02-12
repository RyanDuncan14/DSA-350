from planet import *
import pytest


earth = planet("Earth", 4.26e-5, "blue")
jupiter = planet("Jupiter", 0.00046, "brown")
saturn = planet("Saturn", 0.000389, "yellow")

luna = moon("Moon", 1.16e-5, planet_companion = earth)
io = moon("Io", 2, planet_companion = jupiter)
europa = moon("Europa", 1.5, planet_companion = jupiter)


def test_update_planet():
    io.update_planet()
    europa.update_planet()

    assert io in jupiter.moon_list
    assert europa in jupiter.moon_list
    assert len(jupiter.moon_list) == 2


