import pytest
from unittest import mock
from enum import Enum
from nrkradio import Channel, Page, Podcast, PodcastEpisode, Season, Section, Series, StandaloneProgram, Type, map_type_to_class

@pytest.fixture
def mock_type():
    class Type(Enum):
        MISSINGTYPE = "missingtype"

    with mock.patch("nrkradio.Type", return_value=Type ) as mocked:
        yield mocked



@pytest.mark.parametrize(
    argnames="type,expected_plug_class",
    argvalues=[
        (Type.CHANNEL, Channel),
        (Type.PAGE, Page),
        (Type.PODCAST, Podcast),
        (Type.PODCASTEPISODE, PodcastEpisode),
        (Type.SEASON, Season),
        (Type.SECTION, Section),
        (Type.SERIES, Series),
        (Type.STANDALONEPROGRAM, StandaloneProgram)
    ],
    ids=["Channel", "Page", "Podcast", "PodcastEpisode", "Season", "Section", "Series", "StandaloneProgram"],
)
def test_map_type_to_class(type, expected_plug_class):
    item_class = map_type_to_class(type)

    assert item_class == expected_plug_class

def test_map_invalid_type_to_class():
    item_type = "invalid_type"
    with pytest.raises(ValueError, match=f"No type found for: {item_type}"):
        _ = map_type_to_class(item_type)

def test_map_missing_type_to_class(mock_type):
    item_type = "missingtype"
    with pytest.raises(ValueError, match=f"No class found for: {item_type}"):
        _ = map_type_to_class(item_type)