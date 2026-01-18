from typing import Any


import pytest

from nrkradio import (
    BasePlug,
    ChannelPlug,
    EpisodePlug,
    PodcastEpisodePlug,
    PodcastPlug,
    SeriesPlug,
    StandaloneProgramPlug,
    plug_factory,
)


@pytest.fixture
def response(request) -> dict[str, Any]:
    data = request.param

    return {"type": data}


class PlugStub(object):
    def __init__(self, response) -> None:
        self.response = response


@pytest.mark.parametrize(
    argnames="response,expected_plug_class",
    argvalues=[
        ("channel", ChannelPlug),
        ("podcastEpisode", PodcastEpisodePlug),
        ("standaloneProgram", StandaloneProgramPlug),
        ("podcast", PodcastPlug),
        ("episode", EpisodePlug),
        ("series", SeriesPlug),
    ],
    ids=["channel", "podcastEpisode", "standaloneProgram", "podcast", "episode", "series"],
    indirect=["response"],
)
def test_plug_factory_success(response: dict[str, Any], expected_plug_class):

    plug: BasePlug = plug_factory(response)
    assert isinstance(plug, expected_plug_class), (
        f"Expected {expected_plug_class.__name__}, " f"but got {type(plug).__name__}"
    )

def test_plug_factory_no_type():
    response = {}
    with pytest.raises(ValueError, match="No type found in plug"):
        _ = plug_factory(response)

def test_plug_factory_unsupported_plug():
    response = { "type": "unsupported"
    }
    with pytest.raises(ValueError, match="Unsupported plug type: unsupported"):
        _ = plug_factory(response)