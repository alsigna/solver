import pytest

from main import calculate_sum


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 7),
        (4, 5, 9),
        (6, 5, 11),
    ],
)
def test_sum(a, b, expected):
    assert calculate_sum(a, b) == expected
