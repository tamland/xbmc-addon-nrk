from unittest import mock
import pytest

from nrkradio import StandaloneProgram


@pytest.fixture
def standalone_program_manifest():
    return {
        "_links": {
            "self": {"href": "/playback/manifest/program/QWERT12345678"},
            "metadata": {
                "href": "/playback/metadata/program/QWERT12345678",
                "name": "metadata",
            },
        },
        "id": "QWERT12345678",
        "playability": "playable",
        "streamingMode": "onDemand",
        "availability": {
            "information": "",
            "isGeoBlocked": False,
            "onDemand": {
                "from": "2026-02-05T06:00:00+01:00",
                "to": "2100-01-01T23:59:59+01:00",
                "hasRightsNow": True,
            },
            "live": None,
            "externalEmbeddingAllowed": True,
        },
        "statistics": {
            "scores": {
                "springStreamSite": "nrkradio",
                "springStreamStream": "programspiller/odm/nrk_online/drama/program-title/s01e01.program-title.QWERT12345678",
                "springStreamContentType": "other/generic_hls",
                "springStreamProgramId": "QWERT12345678",
                "springStreamDuration": 764,
            },
            "ga": {
                "dimension1": "prf:QWERT12345678",
                "dimension2": "program-title",
                "dimension3": "2008",
                "dimension4": "01",
                "dimension5": "01",
                "dimension10": "prf:QWERT12345678",
                "dimension21": "program-title",
                "dimension22": "1",
                "dimension23": "drama",
                "dimension25": "audio",
                "dimension26": "ondemand",
                "dimension29": "other/generic_hls",
                "dimension36": "other-generichls|notapplicable|none|ondemand|world|akamai-cdn|europeaneconomicarea|notapplicable|none|notapplicable",
            },
            "conviva": None,
            "luna": {
                "config": {
                    "beacon": "https://some-none-existing-alias.example.com/akamai-beacon.xml"
                },
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
                "mediaId": "QWERT12345678",
                "title": "Program Title: 1. episode",
                "clientName": "other-generichls",
                "cdnName": "akamai-cdn",
                "npawCdnName": "AKAMAI",
                "streamingFormat": "hlsv3",
                "segmentLength": "notapplicable",
                "assetType": "ondemand",
                "correlationId": "0d91c871e930b00ff64b2ed85c1b08d6",
                "live": False,
                "npawCustomDimensions": {
                    "1": "other-generichls",
                    "2": "0d91c871e930b00ff64b2ed85c1b08d6",
                },
            },
            "snowplow": {"source": "prf"},
            "kantar": {
                "trackingType": "onDemand",
                "site": "nrkradio",
                "contentType": "other/generic_hls",
                "stream": "programspiller/odm/nrk_online/drama/program-title/s01e01.program-title.QWERT12345678",
                "duration": 764,
                "contentId": "QWERT12345678",
            },
        },
        "playable": {
            "endSequenceStartTime": None,
            "duration": "PT12M44S",
            "assets": [
                {
                    "url": "https://example.com/open/ps/mktt/QWERT12345678/6882926e-2.smil/muxed.m3u8?adap=audio&aco=aac",
                    "format": "HLS",
                    "mimeType": "application/vnd.apple.mpegurl",
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


def test_init():
    title = "Dummy title"
    program_id = "ABCD123456789"
    standalone_program = StandaloneProgram(title, program_id, [])
    assert standalone_program.id == program_id
    assert standalone_program.title == title
    assert standalone_program.manifest_url == f"/playback/manifest/program/{program_id}"
    assert standalone_program.thumb == None
    assert standalone_program.fanart == None

def test_from_url_from_season_success():

    program_id = "ABCDEF12345678"
    standalone_program: StandaloneProgram = StandaloneProgram.from_url(
        f"/playback/manifest/program/{program_id}"
    )

    assert standalone_program.id == program_id
    assert standalone_program.manifest_url == f"/playback/manifest/program/{program_id}"


def test_from_url_from_plug_success():

    program_id = "ABCDEF12345678"
    standalone_program: StandaloneProgram = StandaloneProgram.from_url(
        f"/programs/{program_id}"
    )

    assert standalone_program.id == program_id
    assert standalone_program.manifest_url == f"/playback/manifest/program/{program_id}"


def test_from_url_wrong_format():
    with pytest.raises(ValueError, match="Wrong format of url"):
        StandaloneProgram.from_url("/ABCDEFG1234567")


def test_get_media_url(standalone_program_manifest):
    with mock.patch("nrk.get", return_value=standalone_program_manifest) as mocked_get:
        program_id = "QWERT12345678"
        standalone_program = StandaloneProgram("Dummy title", program_id, [])

        assert (
            standalone_program.media_url
            == "https://example.com/open/ps/mktt/QWERT12345678/6882926e-2.smil/muxed.m3u8?adap=audio&aco=aac"
        )

        mocked_get.assert_called_once_with(f"/playback/manifest/program/{program_id}")


def test_get_media_url_multiple_calls(standalone_program_manifest):
    with mock.patch("nrk.get", return_value=standalone_program_manifest) as mocked_get:
        program_id = "QWERT12345678"
        standalone_program = StandaloneProgram("Dummy title", program_id, [])

        assert (
            standalone_program.media_url
            == "https://example.com/open/ps/mktt/QWERT12345678/6882926e-2.smil/muxed.m3u8?adap=audio&aco=aac"
        )
        _ = standalone_program.media_url
        _ = standalone_program.media_url
        _ = standalone_program.media_url
        mocked_get.assert_called_once_with(f"/playback/manifest/program/{program_id}")
