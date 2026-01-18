import pytest
from nrk import deep_get, deep_get_str, deep_get_list, deep_get_dict


@pytest.fixture(scope="module")
def nested_dict():
    """A moderately deep dictionary used by many tests."""
    return {
        "a": {
            "b": {
                "c": {"d": "A"},
                "x": 42,
            },
            "y": "leaf",
        },
        "b": [[{"e": "f", "g": [10, 11, 12]}], [[20, 30, 40]]],
    }


@pytest.mark.parametrize(
    "keys,expected",
    [
        (("a", "b", "c", "d"), "A"),
        (("a", "b", "c"), {"d": "A"}),
        (("a", "y"), "leaf"),
        (("a", "b", "x"), 42),
        (("b", 0, 0, "e"), "f"),
        (("b", 0, 0, "g"), [10, 11, 12]),
        (("b", 0, 0, "g", 1), 11),
        (("b", 1, 0, 2), 40),
        (("b", -2, -1, "g",  -3), 10),
    ],
)
def test_deep_get_happy_path(nested_dict, keys, expected):
    """Verify that deep_get returns the expected value for valid key chains."""
    assert deep_get(nested_dict, *keys) == expected


def test_deep_get_none_input():
    """Calling with ``None`` as the mapping should return ``None``."""
    assert deep_get(None) is None


def test_deep_get_missing_key(nested_dict):
    """Missing intermediate keys must short‑circuit to ``None``."""
    assert deep_get(nested_dict, "a", "missing", "key") is None


def test_deep_get_non_mapping_intermediate():
    """If an intermediate value isn’t a mapping, the function should stop."""
    # Here "x" resolves to an int (42); further traversal is impossible.
    assert deep_get({"root": {"x": 42}}, "root", "x", "anything") is None


def test_deep_get_index_out_of_bound(nested_dict):
    """If an index is larger than the list, deep_get should return None"""
    assert deep_get(nested_dict, "b", 2) is None

def test_deep_get_negative_index_out_of_bound(nested_dict):
    """If an index is larger than the list, deep_get should return None"""
    assert deep_get(nested_dict, "b", -3) is None

def test_deep_get_str_return_str_on_success(nested_dict):
    assert deep_get_str(nested_dict, "a", "y") == "leaf"

def test_deep_get_str_return_none_on_failure(nested_dict):
    assert deep_get_str(nested_dict, "c", "y") == None

def test_deep_get_list_return_list_on_success(nested_dict):
    assert deep_get_list(nested_dict, "b", 0, 0, "g", ) == [10, 11, 12]

def test_deep_get_list_return_empty_list_on_failure(nested_dict):
    assert deep_get_list(nested_dict, "c" ) == []

def test_deep_get_dict_return_dict_on_success(nested_dict):
    assert deep_get_dict(nested_dict, "a", "b", "c" ) == {"d": "A"}

def test_deep_get_dict_return_empty_dict_on_failure(nested_dict):
    assert deep_get_dict(nested_dict, "c" ) == {}