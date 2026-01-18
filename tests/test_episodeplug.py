import pytest

from nrkradio import EpisodePlug


@pytest.fixture
def episode_plug_response():
    return {
        "type": "episode",
        "_links": {
            "episode": "/programs/ABCDEFG12345678",
            "mediaelement": "/mediaelement/ABCDEFG12345678",
            "series": "/series/seriesname",
            "season": "/series/seriesname/seasons/0/episodes",
        },
        "episode": {
            "titles": {
                "title": "Episode title",
                "subtitle": "Episode subtitle",
            },
            "image": {
                "id": "019c39ec-1deb-7ec7-989d-e11ad4024165",
                "webImages": [
                    {
                        "uri": "https://example.com/019c39ec-1deb-7ec7-989d-e11ad4024165fmIQECFtGh-Z6FOsEAclhA",
                        "width": 300,
                    },
                    {
                        "uri": "https://example.com/019c39ec-1deb-7ec7-989d-e11ad4024165xFzIdgDHG7yZ6FOsEAclhA",
                        "width": 600,
                    },
                    {
                        "uri": "https://example.com/019c39ec-1deb-7ec7-989d-e11ad4024165g7wscWA5W0SZ6FOsEAclhA",
                        "width": 960,
                    },
                    {
                        "uri": "https://example.com/019c39ec-1deb-7ec7-989d-e11ad4024165g-lYjMeaUq6Z6FOsEAclhA",
                        "width": 1280,
                    },
                    {
                        "uri": "https://example.com/019c39ec-1deb-7ec7-989d-e11ad4024165JcUtlKdzziiZ6FOsEAclhA",
                        "width": 1600,
                    },
                    {
                        "uri": "https://example.com/019c39ec-1deb-7ec7-989d-e11ad4024165Wlj7LVBuuqOZ6FOsEAclhA",
                        "width": 1920,
                    },
                ],
            },
            "duration": "PT57M",
            "series": {"titles": {"title": "Series title"}},
        },
    }


def test_init(episode_plug_response):

    episode_plug: EpisodePlug = EpisodePlug(episode_plug_response)

    assert episode_plug.id == None
    assert episode_plug.title == "Series title: Episode title: Episode subtitle"
    assert episode_plug.manifest_url == "/programs/ABCDEFG12345678"
    assert (
        episode_plug.thumb
        == "https://example.com/019c39ec-1deb-7ec7-989d-e11ad4024165fmIQECFtGh-Z6FOsEAclhA"
    )
    assert (
        episode_plug.fanart
        == "https://example.com/019c39ec-1deb-7ec7-989d-e11ad4024165Wlj7LVBuuqOZ6FOsEAclhA"
    )
