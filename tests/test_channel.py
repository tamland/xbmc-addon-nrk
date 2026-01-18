import pytest
from unittest import mock
from nrkradio import Channel


@pytest.fixture
def channel_manifest():
    return {
        "_links": {
            "self": {"href": "/playback/manifest/channel/channel-123"},
            "metadata": {
                "href": "/playback/metadata/channel/channel-123",
                "name": "metadata",
            },
        },
        "id": "channel-123",
        "playability": "playable",
        "streamingMode": "live",
        "availability": {
            "information": "",
            "isGeoBlocked": False,
            "onDemand": None,
            "live": {
                "type": "channel",
                "isOngoing": True,
                "transmissionInterval": None,
            },
            "externalEmbeddingAllowed": True,
        },
        "statistics": {
            "scores": {
                "springStreamSite": "nrkradio",
                "springStreamStream": "programspiller/live/nrk_channel-123",
                "springStreamContentType": "other/generic_hls",
                "springStreamProgramId": "",
                "springStreamDuration": None,
            },
            "ga": {
                "dimension1": "",
                "dimension2": "channel-123",
                "dimension3": "",
                "dimension4": "",
                "dimension5": "",
                "dimension10": "live:channel-123",
                "dimension21": "",
                "dimension22": "",
                "dimension23": "",
                "dimension25": "audio",
                "dimension26": "live",
                "dimension29": "other/generic_hls",
                "dimension36": "other-generichls|notapplicable|sliding|live|world|akamai-cdn|europeaneconomicarea|notapplicable|none|stereo|notapplicable|sd",
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
                    "cdnName": "Akamai-Cdn",
                },
            },
            "qualityOfExperience": {
                "mediaId": "channel-123",
                "channelId": "channel-123",
                "title": "Channel 123",
                "clientName": "other-generichls",
                "cdnName": "akamai-cdn",
                "npawCdnName": "AKAMAI",
                "streamingFormat": "hlsv3",
                "segmentLength": "notapplicable",
                "assetType": "live",
                "correlationId": "019c497a-3b48-7af0-90e6-6cd4b2653c0a",
                "live": True,
                "npawCustomDimensions": {
                    "1": "other-generichls",
                    "2": "019c497a-3b48-7af0-90e6-6cd4b2653c0a",
                },
            },
            "snowplow": {"source": "prf"},
            "kantar": {
                "trackingType": "live",
                "site": "nrkradio",
                "contentType": "other/generic_hls",
                "stream": "programspiller/live/nrk_channel-123",
                "duration": 0,
                "contentId": "channel-123",
            },
        },
        "playable": {
            "endSequenceStartTime": None,
            "duration": None,
            "assets": [
                {
                    "url": "https://example.com/channel-123/muxed.m3u8?adap=audio&aco=aac",
                    "format": "HLS",
                    "mimeType": "application/vnd.apple.mpegurl",
                    "encrypted": False,
                    "encryptionScheme": "none",
                }
            ],
            "liveBuffer": {
                "bufferStartTime": None,
                "bufferDuration": "PT3H",
                "bufferType": "sliding",
            },
            "subtitles": [],
            "thumbnails": [],
        },
        "nonPlayable": None,
        "displayAspectRatio": None,
        "sourceMedium": "audio",
    }


def test_init(channel_manifest):
    channel_id = "channel-123"
    manifest_url = f"/playback/manifest/channel/{channel_id}"

    with mock.patch("nrk.get", return_value=channel_manifest) as mocked_get:
        channel = Channel(channel_id)

        mocked_get.assert_called_once_with(manifest_url)

        assert channel.id == channel_id
        assert channel.manifest_url == manifest_url
        assert channel.media_url == "https://example.com/channel-123/muxed.m3u8?adap=audio&aco=aac"
        assert channel.thumb == None
        assert channel.fanart == None

def test_from_url_success(channel_manifest):
    channel_id = "channel-123"
    manifest_url = f"/playback/manifest/channel/{channel_id}"

    with mock.patch("nrk.get", return_value=channel_manifest) as mocked_get:
        channel = Channel.from_url(f"/mediaelement/{channel_id}")

        mocked_get.assert_called_once_with(manifest_url)

        assert channel.id == channel_id
        assert channel.manifest_url == manifest_url
        assert channel.media_url == "https://example.com/channel-123/muxed.m3u8?adap=audio&aco=aac"

def test_from_url_wrong_format():
    with pytest.raises(ValueError, match="Wrong format of url"):
        _ = Channel.from_url("/radio/medialement/channel-123")