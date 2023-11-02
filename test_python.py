import math

# Тесты для функции filter
def test_filter():
    assert list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])) == [2, 4, 6]
    assert list(filter(lambda x: x > 0, [-1, 2, -3, 4, -5, 6])) == [2, 4, 6]
    assert list(filter(lambda x: len(x) > 3, ["cat", "dog", "elephant", "bird"])) == ["elephant", "bird"]

# Тесты для функции map
def test_map():
    assert list(map(lambda x: x * 2, [1, 2, 3, 4, 5])) == [2, 4, 6, 8, 10]
    assert list(map(lambda x: x.upper(), ["cat", "dog", "elephant", "bird"])) == ["CAT", "DOG", "ELEPHANT", "BIRD"]
    assert list(map(lambda x: len(x), ["cat", "dog", "elephant", "bird"])) == [3, 3, 8, 4]

# Тесты для функции sorted
def test_sorted():
    assert sorted([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert sorted(["cat", "dog", "elephant", "bird"]) == ["bird", "cat", "dog", "elephant"]
    assert sorted(["cat", "Dog", "elephant", "bird"], key=str.lower) == ["bird", "cat", "Dog", "elephant"]

# Тесты для функции pi из библиотеки math
def test_pi():
    assert math.isclose(math.pi, 3.141592653589793, rel_tol=1e-9, abs_tol=0.0)
    assert math.pi > 0

# Тесты для функции sqrt из библиотеки math
def test_sqrt():
    assert math.isclose(math.sqrt(4), 2.0, rel_tol=1e-9, abs_tol=0.0)
    assert math.isclose(math.sqrt(2), 1.4142135623730951, rel_tol=1e-9, abs_tol=0.0)

# Тесты для функции pow из библиотеки math
def test_pow():
    assert math.isclose(math.pow(2, 3), 8.0, rel_tol=1e-9, abs_tol=0.0)
    assert math.isclose(math.pow(2, -3), 0.125, rel_tol=1e-9, abs_tol=0.0)

# Тесты для функции hypot из библиотеки math
def test_hypot():
    assert math.isclose(math.hypot(3, 4), 5.0, rel_tol=1e-9, abs_tol=0.0)
    assert math.isclose(math.hypot(1, 1), 1.4142135623730951, rel_tol=1e-9, abs_tol=0.0)
