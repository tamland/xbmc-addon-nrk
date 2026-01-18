import pytest
from nrkradio import PodcastEpisodePlug


@pytest.fixture
def podcastepisode_plug_response():
    return {
        "type": "podcastEpisode",
        "_links": {
            "podcastEpisode": "/podcasts/podcastname/episodes/l_e491a7cb-af50-411f-b91a-a292021ec8cf",
            "podcast": "/podcasts/podcastname",
            "audioDownload": "https://example.com/fil/podcastname/e491a7cb-af50-411f-b91a-a292021ec8cf_1_ID192MP3.mp3",
        },
        "podcastEpisode": {
            "titles": {
                "title": "Podcast episode title",
                "subtitle": "Podcast episode subtitle",
            },
            "duration": "PT28M3S",
            "imageUrl": "https://example.com/019c39d5-f487-7d26-8550-f924592f8d9c",
            "podcast": {"titles": {"title": "Podcast Title"}},
        },
    }


@pytest.fixture
def podcastepisode_plug_only_subtitle_response():
    return {
        "type": "podcastEpisode",
        "_links": {
            "podcastEpisode": "/podcasts/podcastname/episodes/l_e491a7cb-af50-411f-b91a-a292021ec8cf",
            "podcast": "/podcasts/podcastname",
            "audioDownload": "https://example.com/fil/podcastname/e491a7cb-af50-411f-b91a-a292021ec8cf_1_ID192MP3.mp3",
        },
        "podcastEpisode": {
            "titles": {
                "subtitle": "Podcast episode subtitle",
            },
            "duration": "PT28M3S",
            "imageUrl": "https://example.com/019c39d5-f487-7d26-8550-f924592f8d9c",
            "podcast": {"titles": {"title": "Podcast Title"}},
        },
    }


def test_init(podcastepisode_plug_response):

    podcastepisode_plug: PodcastEpisodePlug = PodcastEpisodePlug(
        podcastepisode_plug_response
    )

    assert podcastepisode_plug.id == None
    assert podcastepisode_plug.title == "Podcast Title: Podcast episode title"
    assert (
        podcastepisode_plug.manifest_url
        == "/podcasts/podcastname/episodes/l_e491a7cb-af50-411f-b91a-a292021ec8cf"
    )
    assert (
        podcastepisode_plug.thumb
        == "https://example.com/019c39d5-f487-7d26-8550-f924592f8d9c"
    )
    assert (
        podcastepisode_plug.fanart
        == "https://example.com/019c39d5-f487-7d26-8550-f924592f8d9c"
    )


def test_init_only_subtitle(podcastepisode_plug_only_subtitle_response):

    podcastepisode_plug: PodcastEpisodePlug = PodcastEpisodePlug(
        podcastepisode_plug_only_subtitle_response
    )

    assert podcastepisode_plug.id == None
    assert podcastepisode_plug.title == "Podcast Title: Podcast episode subtitle"
    assert (
        podcastepisode_plug.manifest_url
        == "/podcasts/podcastname/episodes/l_e491a7cb-af50-411f-b91a-a292021ec8cf"
    )
