"""
Unit-tests for the ``better_dict.core`` module.

"""
import pytest
import pandas as pd
from better_dict.core import BetterDict


@pytest.fixture
def simple_dict() -> dict:
    return {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}


@pytest.fixture
def simple_better_dict(simple_dict) -> BetterDict:
    return BetterDict(simple_dict)


def check_first_two_keys(better_dict_sample: BetterDict):
    assert better_dict_sample["a"] == 1
    assert better_dict_sample["b"] == 2


def test_better_dict_init(simple_dict: dict):
    """Test that ``BetterDict`` can be initialized with a dict."""
    d = BetterDict(simple_dict)
    assert isinstance(d, BetterDict)
    check_first_two_keys(d)


def test_better_dict_get_multiple_values(simple_better_dict: BetterDict):
    """Test that ``BetterDict`` can get multiple values at once."""
    result = simple_better_dict["a", "b"]
    assert isinstance(result, BetterDict)
    check_first_two_keys(result)


def test_better_dict_set_multiple_values(simple_better_dict: BetterDict):
    """Test that ``BetterDict`` can set multiple values at once."""
    simple_better_dict["a", "b"] = 3, 4
    assert simple_better_dict["a"] == 3
    assert simple_better_dict["b"] == 4


def test_better_dict_iloc_get(simple_better_dict: BetterDict):
    """Test that ``BetterDict`` can access values using index notation."""

    assert simple_better_dict.iloc[0] == 1
    assert simple_better_dict.iloc[1] == 2


def test_better_dict_iloc_set(simple_better_dict: BetterDict):
    """Test that ``BetterDict`` can set multiple values using index notation."""
    simple_better_dict.iloc[0, 1] = [5, 6]
    assert simple_better_dict.iloc[:] == [5, 6, 3, 4, 5]


def test_better_dict_keys_values(simple_better_dict: BetterDict):
    """Test that ``BetterDict`` can get keys and values as lists."""
    assert simple_better_dict.keys() == ["a", "b", "c", "d", "e"]
    assert simple_better_dict.values() == [1, 2, 3, 4, 5]


def test_better_dict_close_match():
    """Test that ``BetterDict`` can get close matches to key names."""
    d = BetterDict({"apple": 1, "banana": 2})
    assert d.close_match("apl", cutoff=0.5) == "apple"
    with pytest.raises(KeyError):
        d.close_match("xyz")


def test_better_dict_rename(simple_better_dict: BetterDict):
    """Test that ``BetterDict`` can rename keys."""
    simple_better_dict.rename({"a": "A", "b": "B"})
    assert sorted(simple_better_dict.keys()) == ["A", "B", "c", "d", "e"]
    assert sorted(simple_better_dict.values()) == [1, 2, 3, 4, 5]


def test_better_dict_dtypes(simple_better_dict: BetterDict):
    """
    Test that ``BetterDict`` can get the dtypes of its values.
    """
    dtypes = simple_better_dict.dtypes()
    assert dtypes["a"] == int
    assert dtypes["b"] == int


def test_better_dict_select_dtypes():
    """Test that ``BetterDict`` can select values based on their dtypes."""
    d = BetterDict({"a": 1, "b": "2", "c": [3], "d": {"e": 4}})
    result = d.select_dtypes(include=["number", "string"])
    assert result == BetterDict({"a": 1, "b": "2"})


def test_better_dict_from_frame():
    """Test that ``BetterDict`` can be initialized from ``pandas.DataFrame``."""
    df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
    d = BetterDict.from_frame(df)
    assert isinstance(d, BetterDict)


def test_better_dict_from_series():
    """Test that ``BetterDict`` can be initialized from ``pandas.Series``."""
    series = pd.Series({"a": 1, "b": 2})
    result = BetterDict.from_series(series)
    assert isinstance(result, BetterDict)
    assert result == {"a": 1, "b": 2}


def test_better_dict_apply(simple_better_dict):
    """Test method ``BetterDict.apply``."""
    result = simple_better_dict.apply(lambda x: x + 1)
    assert result == {"a": 2, "b": 3, "c": 4, "d": 5, "e": 6}


def test_better_dict_apply_keys(simple_better_dict):
    """Test method ``BetterDict.apply`` for the dictionary keys."""
    result = simple_better_dict.apply(lambda k: str(k).upper(), axis=0)
    assert result.keys() == ["A", "B", "C", "D", "E"]


def test_better_dict_vloc(simple_better_dict):
    """Test method ``BetterDict.vloc``."""
    result = simple_better_dict.vloc[1]
    assert result == ["a"]
    simple_better_dict["f"] = 1
    result = simple_better_dict.vloc[1]
    assert result == ["a", "f"]
