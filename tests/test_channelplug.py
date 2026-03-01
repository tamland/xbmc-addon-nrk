import pytest

from nrkradio import ChannelPlug


@pytest.fixture
def channel_plug_response():
    return {
        "type": "channel",
        "_links": {"channel": "/mediaelement/channelname"},
        "channel": {
            "titles": {"title": "Channel title"},
            "image": {
                "id": "019c39da-d036-70f5-9c30-9c7179f233ff",
                "webImages": [
                    {
                        "uri": "https://example.com/019c39da-d036-70f5-9c30-9c7179f233ff7H9WHy0d_QEvZ41HevX4tQ",
                        "width": 300,
                    },
                    {
                        "uri": "https://example.com/019c39da-d036-70f5-9c30-9c7179f233ffnptQAWmTl0QvZ41HevX4tQ",
                        "width": 600,
                    },
                    {
                        "uri": "https://example.com/019c39da-d036-70f5-9c30-9c7179f233ffNE58lEqQAswvZ41HevX4tQ",
                        "width": 960,
                    },
                    {
                        "uri": "https://example.com/019c39da-d036-70f5-9c30-9c7179f233ffktYCmVGM_QUvZ41HevX4tQ",
                        "width": 1280,
                    },
                    {
                        "uri": "https://example.com/019c39da-d036-70f5-9c30-9c7179f233ffBdvbxUqgPHYvZ41HevX4tQ",
                        "width": 1600,
                    },
                    {
                        "uri": "https://example.com/019c39da-d036-70f5-9c30-9c7179f233ff1ean57gyYhQvZ41HevX4tQ",
                        "width": 1920,
                    },
                ],
            },
        },
    }


def test_init(channel_plug_response):

    channel_plug = ChannelPlug(channel_plug_response)

    assert channel_plug.id == None
    assert channel_plug.title == "Channel title"
    assert channel_plug.manifest_url == "/mediaelement/channelname"
    assert (
        channel_plug.thumb
        == "https://example.com/019c39da-d036-70f5-9c30-9c7179f233ff7H9WHy0d_QEvZ41HevX4tQ"
    )
    assert (
        channel_plug.fanart
        == "https://example.com/019c39da-d036-70f5-9c30-9c7179f233ff1ean57gyYhQvZ41HevX4tQ"
    )
