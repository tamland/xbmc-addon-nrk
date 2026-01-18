import pytest

from nrkradio import PodcastPlug


@pytest.fixture
def podcast_plug_response():
    return {
        "type": "podcast",
        "_links": {"podcast": "/podcasts/podcastname"},
        "podcast": {
            "titles": {
                "title": "Podcast title",
                "subtitle": "Podcast subtitle",
            },
            "imageUrl": "https://example.com/019c39e9-8c1f-7476-b536-8a300dd9554d",
            "numberOfEpisodes": 9,
        },
    }

@pytest.fixture
def podcast_plug_only_subtitle_response():
    return {
        "type": "podcast",
        "_links": {"podcast": "/podcasts/podcastname"},
        "podcast": {
            "titles": {
                "subtitle": "Podcast subtitle",
            },
            "imageUrl": "https://example.com/019c39e9-8c1f-7476-b536-8a300dd9554d",
            "numberOfEpisodes": 9,
        },
    }


def test_init(podcast_plug_response):

    podcast_plug: PodcastPlug = PodcastPlug(podcast_plug_response)

    assert podcast_plug.id == None
    assert podcast_plug.title == "Podcast title: Podcast subtitle"
    assert podcast_plug.manifest_url == "/podcasts/podcastname"
    assert (
        podcast_plug.thumb
        == "https://example.com/019c39e9-8c1f-7476-b536-8a300dd9554d"
    )
    assert (
        podcast_plug.fanart
        == "https://example.com/019c39e9-8c1f-7476-b536-8a300dd9554d"
    )

def test_init_only_subtitle(podcast_plug_only_subtitle_response):

    podcast_plug: PodcastPlug = PodcastPlug(podcast_plug_only_subtitle_response)

    assert podcast_plug.id == None
    assert podcast_plug.title == "Podcast subtitle"
    assert podcast_plug.manifest_url == "/podcasts/podcastname"
