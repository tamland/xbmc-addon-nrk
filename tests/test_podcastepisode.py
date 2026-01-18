from unittest import mock
import pytest

from nrk import deep_get_list
from nrkradio import PodcastEpisode


@pytest.fixture
def podcastepisode_manifest():
    return {
        "_links": {
            "self": {
                "href": "/playback/manifest/podcast/l_019c3d5f-c860-7fa8-9f53-801dfafeec85"
            },
            "metadata": {
                "href": "/playback/metadata/podcast/l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
                "name": "metadata",
            },
        },
        "id": "l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
        "playability": "playable",
        "streamingMode": "onDemand",
        "availability": {
            "information": "",
            "isGeoBlocked": False,
            "onDemand": {
                "from": "2023-05-03T04:04:00Z",
                "to": "9999-12-31T23:59:59.9999999Z",
                "hasRightsNow": True,
            },
            "live": None,
            "externalEmbeddingAllowed": True,
        },
        "statistics": {
            "scores": None,
            "ga": {
                "dimension1": "podcast:l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
                "dimension2": "Podcastepisode Title",
                "dimension3": "",
                "dimension4": "",
                "dimension5": "",
                "dimension10": "podcast:l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
                "dimension21": "podcast_episode_title",
                "dimension22": "",
                "dimension23": "",
                "dimension25": "audio",
                "dimension26": "ondemand",
                "dimension29": "other/generic_hls",
                "dimension36": "other-generichls|mp3|notapplicable|notapplicable|podcast|telenor|world|podcast-cdn|europeaneconomicarea|notapplicable|none|notapplicable|notapplicable",
            },
            "conviva": None,
            "luna": {
                "config": {"beacon": "https://example.com/akamai-beacon.xml"},
                "data": {
                    "title": "",
                    "device": "",
                    "playerId": "",
                    "deliveryType": "",
                    "playerInfo": "",
                    "cdnName": "Podcast-Cdn",
                },
            },
            "qualityOfExperience": {
                "clientName": "other-generichls",
                "cdnName": "podcast-cdn",
                "streamingFormat": "mp3",
                "segmentLength": "n/a",
                "assetType": "ondemand",
                "correlationId": "019c3d64-585c-75fc-bda2-3cc5e43202be",
            },
            "snowplow": {"source": "podcast"},
        },
        "playable": {
            "endSequenceStartTime": None,
            "duration": "PT35M10S",
            "assets": [
                {
                    "url": "https://example.com/fil/podcast_series_name/019c3d61-c741-7d7f-bb99-84d17abd0a70_0_ID192MP3.mp3",
                    "format": "MP3",
                    "mimeType": "audio/mp3",
                    "encrypted": False,
                    "encryptionScheme": "none",
                }
            ],
            "liveBuffer": None,
            "subtitles": [],
            "thumbnails": [],
        },
        "nonPlayable": None,
        "displayAspectRatio": None,
        "sourceMedium": "audio",
    }


@pytest.fixture
def podcastepisode_metadata():
    return {
        "_links": {
            "self": {
                "href": "/playback/metadata/podcast/l_019c3d5f-c860-7fa8-9f53-801dfafeec85"
            },
            "manifests": [
                {
                    "href": "/playback/manifest/podcast/l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
                    "name": "default",
                }
            ],
            "next": None,
            "nextLinks": None,
            "progress": {
                "templated": True,
                "href": "/radio/userdata/{userId}/progress/podcastepisode/podcast_series_name|l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
            },
            "personalizedNext": {
                "templated": True,
                "href": "/radio/userdata/{userId}/upnext/podcastepisode/podcast_series_name|l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
            },
        },
        "id": "l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
        "playability": "playable",
        "streamingMode": "onDemand",
        "duration": "PT35M10S",
        "legalAge": {
            "legalReference": "LOV2015-02-06-7",
            "body": {
                "status": "rated",
                "rating": {
                    "code": "A",
                    "displayAge": "A",
                    "displayValue": "Tillatt for alle",
                },
            },
        },
        "availability": {
            "information": "",
            "isGeoBlocked": False,
            "onDemand": {
                "from": "2023-05-03T04:04:00Z",
                "to": "9999-12-31T23:59:59.9999999Z",
                "hasRightsNow": True,
            },
            "live": None,
            "externalEmbeddingAllowed": True,
        },
        "preplay": {
            "titles": {
                "title": "Podcastepisode title",
                "subtitle": "Podcastepisode subtitle",
            },
            "description": "",
            "poster": {
                "images": [
                    {
                        "url": "https://example.com/019c3d64-ef42-7cfb-953c-1bda48e2e3b9oo1D8Cc8qQobqnXx559TCA",
                        "pixelWidth": 300,
                    },
                    {
                        "url": "https://example.com/019c3d64-ef42-7cfb-953c-1bda48e2e3b9Okb-AJQoJ28bqnXx559TCA",
                        "pixelWidth": 600,
                    },
                    {
                        "url": "https://example.com/019c3d64-ef42-7cfb-953c-1bda48e2e3b9dcYN6hp4DCobqnXx559TCA",
                        "pixelWidth": 960,
                    },
                    {
                        "url": "https://example.com/019c3d64-ef42-7cfb-953c-1bda48e2e3b9dmcl-jCds8kbqnXx559TCA",
                        "pixelWidth": 1280,
                    },
                    {
                        "url": "https://example.com/019c3d64-ef42-7cfb-953c-1bda48e2e3b9BdL8MC7rWP8bqnXx559TCA",
                        "pixelWidth": 1920,
                    },
                ]
            },
            "squarePoster": {
                "images": [
                    {
                        "url": "https://example.com/019c3d65-5181-7a79-a986-346df9fad9395krhowpl_K75AFgevbkifA",
                        "pixelWidth": 300,
                    },
                    {
                        "url": "https://example.com/019c3d65-5181-7a79-a986-346df9fad939VklepdyTHWH5AFgevbkifA",
                        "pixelWidth": 600,
                    },
                    {
                        "url": "https://example.com/019c3d65-5181-7a79-a986-346df9fad939sDGDFSs5ejX5AFgevbkifA",
                        "pixelWidth": 960,
                    },
                    {
                        "url": "https://example.com/019c3d65-5181-7a79-a986-346df9fad939GqLg4BBTM2D5AFgevbkifA",
                        "pixelWidth": 1280,
                    },
                ]
            },
            "indexPoints": [],
        },
        "displayAspectRatio": None,
        "playable": {
            "resolve": "/playback/manifest/podcast/l_019c3d5f-c860-7fa8-9f53-801dfafeec85"
        },
        "nonPlayable": None,
        "interactionPoints": None,
        "sourceMedium": "audio",
        "skipDialogInfo": None,
        "interaction": None,
        "_embedded": {
            "manifests": [
                {
                    "_links": {
                        "self": {
                            "href": "/playback/manifest/podcast/l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
                            "name": "default",
                        }
                    },
                    "id": "l_019c3d5f-c860-7fa8-9f53-801dfafeec85",
                    "availabilityLabel": "Av",
                }
            ],
            "next": None,
            "podcast": {
                "_links": {
                    "podcast": {
                        "href": "/podcasts/podcast_series_name",
                        "name": "podcast",
                    }
                },
                "titles": {
                    "title": "Podcastepisode title",
                    "subtitle": "Podcastepisode subtitle",
                },
                "imageUrl": "https://example.com/019c3d64-ef42-7cfb-953c-1bda48e2e3b9PSkx2dkPf9UbqnXx559TCA",
                "rssFeed": "https://example.com/program/podcast_series_name.rss",
                "episodeCount": 7,
            },
            "podcastEpisode": {"clipId": None},
        },
    }


def test_init(podcastepisode_metadata):
    title = "Dummy title"
    podcast_series_id = "podcast_series_name"
    podcast_episode_id = "l_019c3d5f-c860-7fa8-9f53-801dfafeec85"
    images = deep_get_list(podcastepisode_metadata, "preplay", "poster", "images")
    podcastepisode = PodcastEpisode(title, podcast_series_id, podcast_episode_id, images)
    assert podcastepisode.id == podcast_episode_id
    assert podcastepisode.title == title
    assert (
        podcastepisode.manifest_url
        == f"/playback/manifest/podcast/{podcast_series_id}/{podcast_episode_id}"
    )
    assert podcastepisode.thumb == "https://example.com/019c3d64-ef42-7cfb-953c-1bda48e2e3b9oo1D8Cc8qQobqnXx559TCA"
    assert podcastepisode.fanart == "https://example.com/019c3d64-ef42-7cfb-953c-1bda48e2e3b9BdL8MC7rWP8bqnXx559TCA"


def test_from_url_from_season_success(podcastepisode_metadata):

    podcast_series_id = "podcast_series_name"
    podcast_episode_id = "l_019c3d5f-c860-7fa8-9f53-801dfafeec85"

    with mock.patch("nrk.get", return_value=podcastepisode_metadata) as mocked_get:
        podcastepisode: PodcastEpisode = PodcastEpisode.from_url(
            f"/playback/manifest/podcast/{podcast_series_id}/{podcast_episode_id}"
        )

        mocked_get.assert_called_once_with(f'/playback/metadata/podcast/{podcast_series_id}/{podcast_episode_id}')

        assert podcastepisode.id == podcast_episode_id
        assert podcastepisode.title == "Podcastepisode title: Podcastepisode subtitle"
        assert (
            podcastepisode.manifest_url
            == f"/playback/manifest/podcast/{podcast_series_id}/{podcast_episode_id}"
        )


def test_from_url_from_plug_success(podcastepisode_metadata):

    podcast_series_id = "podcast_series_name"
    podcast_episode_id = "l_019c3d5f-c860-7fa8-9f53-801dfafeec85"

    with mock.patch("nrk.get", return_value=podcastepisode_metadata) as mocked_get:
        podcastepisode = PodcastEpisode.from_url(
        f"/podcasts/{podcast_series_id}/episodes/{podcast_episode_id}"
    )

        mocked_get.assert_called_once_with(f'/playback/metadata/podcast/{podcast_series_id}/{podcast_episode_id}')

        assert podcastepisode.id == podcast_episode_id
        assert podcastepisode.title == "Podcastepisode title: Podcastepisode subtitle"
        assert (
            podcastepisode.manifest_url
            == f"/playback/manifest/podcast/{podcast_series_id}/{podcast_episode_id}"
        )



def test_from_url_wrong_format():
    with pytest.raises(ValueError, match="Wrong format of url"):
        PodcastEpisode.from_url("/ABCDEFG1234567")


def test_get_media_url(podcastepisode_manifest):
    title = "Dummy title"
    podcast_series_id = "podcast_series_name"
    podcast_episode_id = "l_019c3d5f-c860-7fa8-9f53-801dfafeec85"
    
    with mock.patch("nrk.get", return_value=podcastepisode_manifest) as mocked_get:
        podcastepisode: PodcastEpisode = PodcastEpisode(title, podcast_series_id, podcast_episode_id, [])

        assert (
            podcastepisode.media_url
            == "https://example.com/fil/podcast_series_name/019c3d61-c741-7d7f-bb99-84d17abd0a70_0_ID192MP3.mp3"
        )

        mocked_get.assert_called_once_with(f"/playback/manifest/podcast/{podcast_series_id}/{podcast_episode_id}")


def test_get_media_url_multiple_calls(podcastepisode_manifest):
    title = "Dummy title"
    podcast_series_id = "podcast_series_name"
    podcast_episode_id = "l_019c3d5f-c860-7fa8-9f53-801dfafeec85"
    
    with mock.patch("nrk.get", return_value=podcastepisode_manifest) as mocked_get:
        podcastepisode: PodcastEpisode = PodcastEpisode(title, podcast_series_id, podcast_episode_id, [])

        assert (
            podcastepisode.media_url
            == "https://example.com/fil/podcast_series_name/019c3d61-c741-7d7f-bb99-84d17abd0a70_0_ID192MP3.mp3"
        )
        _ = podcastepisode.media_url
        _ = podcastepisode.media_url
        _ = podcastepisode.media_url
        mocked_get.assert_called_once_with(f"/playback/manifest/podcast/{podcast_series_id}/{podcast_episode_id}")
