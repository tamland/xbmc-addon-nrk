import pytest
from unittest import mock

from requests import HTTPError
from nrk import get


@pytest.fixture
def mock_session_success():
    class _Response:
        def __init__(self, path: str):
            if len(path.split("&")) > 1:
                self.params = True
            else:
                self.params = False

        def raise_for_status(self):
            pass

        def json(self):
            if self.params:
                return {"C": "D"}
            else:
                return {"A": "B"}

    with mock.patch("nrk.session") as myclass_mocked:
        myclass_mocked.get.side_effect = _Response
        yield myclass_mocked


@pytest.fixture
def mock_session_failure():
    class _Response:
        def __init__(self, path: str):
            pass

        def raise_for_status(self):
            raise HTTPError

        def json(self):
            return None

    with mock.patch("nrk.session") as myclass_mocked:
        myclass_mocked.get.side_effect = _Response
        yield myclass_mocked


def test_get_success(mock_session_success):
    response = get("a/b/c")
    assert response == {"A": "B"}


def test_get_with_parameter_success(mock_session_success):
    response = get("a/b/c", "&c=true")
    assert response == {"C": "D"}


def test_get_httperror(mock_session_failure):
    with pytest.raises(HTTPError):
        response = get("a/b/c")


def test_get_invalid_argument(mock_session_success):
    with pytest.raises(ValueError, match="params must start with &"):
        response = get("a/b/c", "abc")
