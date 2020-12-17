# тесты для PyTest


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


# этот тест должен упасть
def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"
