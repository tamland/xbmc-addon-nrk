import pytest

from nrkradio import SeriesPlug


@pytest.fixture
def series_plug_response():
    return {
        "type": "series",
        "_links": {"series": "/series/seriesname"},
        "series": {
            "titles": {
                "title": "Series title",
                "subtitle": "Series subtitle",
            },
            "image": {
                "id": "019c39ea-f0b7-7463-9aa3-9b63639053ec",
                "webImages": [
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ecPMwQEKDdQrtaBbEZIzo36w",
                        "width": 300,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ecQpyYH7B0NsZaBbEZIzo36w",
                        "width": 600,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053eccDtEveYObMJaBbEZIzo36w",
                        "width": 960,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ec1EaKbUK3LLNaBbEZIzo36w",
                        "width": 1280,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053eczZtNkmL5zmZaBbEZIzo36w",
                        "width": 1600,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ecmkrwoQ1iInxaBbEZIzo36w",
                        "width": 1920,
                    },
                ],
            },
            "numberOfEpisodes": 1,
        },
    }


@pytest.fixture
def series_plug_only_subtitle_response():
    return {
        "type": "series",
        "_links": {"series": "/series/seriesname"},
        "series": {
            "titles": {
                "subtitle": "Series subtitle",
            },
            "image": {
                "id": "019c39ea-f0b7-7463-9aa3-9b63639053ec",
                "webImages": [
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ecPMwQEKDdQrtaBbEZIzo36w",
                        "width": 300,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ecQpyYH7B0NsZaBbEZIzo36w",
                        "width": 600,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053eccDtEveYObMJaBbEZIzo36w",
                        "width": 960,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ec1EaKbUK3LLNaBbEZIzo36w",
                        "width": 1280,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053eczZtNkmL5zmZaBbEZIzo36w",
                        "width": 1600,
                    },
                    {
                        "uri": "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ecmkrwoQ1iInxaBbEZIzo36w",
                        "width": 1920,
                    },
                ],
            },
            "numberOfEpisodes": 1,
        },
    }


def test_init(series_plug_response):

    series_plug: SeriesPlug = SeriesPlug(series_plug_response)

    assert series_plug.id == None
    assert series_plug.title == "Series title: Series subtitle"
    assert series_plug.manifest_url == "/series/seriesname"
    assert (
        series_plug.thumb
        == "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ecPMwQEKDdQrtaBbEZIzo36w"
    )
    assert (
        series_plug.fanart
        == "https://example.com/019c39ea-f0b7-7463-9aa3-9b63639053ecmkrwoQ1iInxaBbEZIzo36w"
    )


def test_init_only_subtitle(series_plug_only_subtitle_response):

    series_plug: SeriesPlug = SeriesPlug(series_plug_only_subtitle_response)

    assert series_plug.id == None
    assert series_plug.title == "Series subtitle"
    assert series_plug.manifest_url == "/series/seriesname"
