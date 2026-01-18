import pytest

from nrkradio import BasePlug

def test_init():

    with pytest.raises(NotImplementedError):
        _ = BasePlug({})
