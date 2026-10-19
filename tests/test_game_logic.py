import pytest

from game_logic import add_gold


def test_add_gold_increases_balance():
    assert add_gold(100, 25) == 160


def test_zero_reward_keeps_balance():
    assert add_gold(100, 0) == 100


@pytest.mark.parametrize("current_gold,reward", [(-1, 25), (100, -1)])
def test_negative_values_raise_error(current_gold, reward):
    with pytest.raises(ValueError):
        add_gold(current_gold, reward)