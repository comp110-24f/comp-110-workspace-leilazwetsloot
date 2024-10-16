"""practicing unit tests in class with list function module"""

from lists_fns import get_first, remove_first


def test_get_first() -> None:
    assert get_first(input=["Leila", "Calvin", "Kevin", "Jennifer"]) == "Leila"


def test_remove_first() -> None:
    my_family: list[str] = ["Leila", "Calvin", "Kevin", "Jennifer"]
    remove_first(my_family)
    assert my_family == ["Calvin", "Kevin", "Jennifer"]


# quadruple check that the test function is looking for the
# correct thing (spelling, syntax, etc.)

# also make sure to include entire file pathway when calling test
# example: lessons/unit_tests/lists_fns_test.py
