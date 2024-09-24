import pytest
from primo import primo

@pytest.mark.parametrize("num, res", [(2, True), (3, True), (4, False), (5, True), (6, False), (7, True), (8, False)])
def test_primo(num, res):
    assert primo(num) == res
    