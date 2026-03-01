import pytest

from nrkradio import StandaloneProgramPlug


@pytest.fixture
def standaloneprogram_plug_response():
    return {
        "type": "standaloneProgram",
        "_links": {
            "program": "/programs/ABCDE12345678",
            "mediaelement": "/mediaelement/ABCDE12345678",
        },
        "program": {
            "titles": {
                "title": "Program Title",
                "subtitle": "Program subtitle",
            },
            "image": {
                "id": "019c39dd-ab7a-7a8f-8e17-4ddabd55f683",
                "webImages": [
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683_yDO3z4Ntptdhmb3_Ub0iQ",
                        "width": 300,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683rLa_uVTOE_pdhmb3_Ub0iQ",
                        "width": 600,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683GlIIpPHIX9Rdhmb3_Ub0iQ",
                        "width": 960,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683gl23UWjOJA5dhmb3_Ub0iQ",
                        "width": 1280,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683Illh5pIabwNdhmb3_Ub0iQ",
                        "width": 1600,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f6831ilEZT80k3tdhmb3_Ub0iQ",
                        "width": 1920,
                    },
                ],
            },
            "duration": "PT0S",
        },
    }


@pytest.fixture
def standaloneprogram_plug_only_subtitle_response():
    return {
        "type": "standaloneProgram",
        "_links": {
            "program": "/programs/ABCDE12345678",
            "mediaelement": "/mediaelement/ABCDE12345678",
        },
        "program": {
            "titles": {
                "subtitle": "Program subtitle",
            },
            "image": {
                "id": "019c39dd-ab7a-7a8f-8e17-4ddabd55f683",
                "webImages": [
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683_yDO3z4Ntptdhmb3_Ub0iQ",
                        "width": 300,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683rLa_uVTOE_pdhmb3_Ub0iQ",
                        "width": 600,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683GlIIpPHIX9Rdhmb3_Ub0iQ",
                        "width": 960,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683gl23UWjOJA5dhmb3_Ub0iQ",
                        "width": 1280,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683Illh5pIabwNdhmb3_Ub0iQ",
                        "width": 1600,
                    },
                    {
                        "uri": "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f6831ilEZT80k3tdhmb3_Ub0iQ",
                        "width": 1920,
                    },
                ],
            },
            "duration": "PT0S",
        },
    }


def test_init(standaloneprogram_plug_response):

    standaloneprogram_plug: StandaloneProgramPlug = StandaloneProgramPlug(
        standaloneprogram_plug_response
    )

    assert standaloneprogram_plug.id == None
    assert standaloneprogram_plug.title == "Program Title: Program subtitle"
    assert standaloneprogram_plug.manifest_url == "/programs/ABCDE12345678"
    assert (
        standaloneprogram_plug.thumb
        == "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683_yDO3z4Ntptdhmb3_Ub0iQ"
    )
    assert (
        standaloneprogram_plug.fanart
        == "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f6831ilEZT80k3tdhmb3_Ub0iQ"
    )


def test_init_only_subtitle(standaloneprogram_plug_only_subtitle_response):

    standaloneprogram_plug: StandaloneProgramPlug = StandaloneProgramPlug(
        standaloneprogram_plug_only_subtitle_response
    )

    assert standaloneprogram_plug.id == None
    assert standaloneprogram_plug.title == "Program subtitle"
    assert standaloneprogram_plug.manifest_url == "/programs/ABCDE12345678"
    assert (
        standaloneprogram_plug.thumb
        == "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f683_yDO3z4Ntptdhmb3_Ub0iQ"
    )
    assert (
        standaloneprogram_plug.fanart
        == "https://example.com/019c39dd-ab7a-7a8f-8e17-4ddabd55f6831ilEZT80k3tdhmb3_Ub0iQ"
    )
