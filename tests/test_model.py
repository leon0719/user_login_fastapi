def add(num1, num2):
    return num1 + num2


def test_add():
    assert add(1, 2) == 3
    assert add("space", "ship") == "spaceship"
