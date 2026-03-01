from nrk import Base
from nrkradio import Section
import pytest
from unittest import mock


@pytest.fixture
def full_page_response():
    """A minimal response containing an ``included`` block."""
    return {
        "title": "Placeholder Page Title",
        "sections": [
            {
                "included": {
                    "title": "Section Title",
                    "plugs": [
                        {
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
                        },
                        {
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
                        },
                        {
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
                        },
                        {
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
                        },
                        {
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
                        },
                        {
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
                        },
                    ],
                }
            }
        ],
    }


@pytest.fixture
def section_response():
    """A minimal response containing an ``included`` block."""
    return {
        "included": {
            "title": "Section Title",
            "plugs": [
                {
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
            ],
        }
    }


def test_init_with_full_page_response(full_page_response):
    """
    Verify that a Section created from a response that contains an
    ``included`` block extracts the title and creates plug objects.
    """
    sec = Section(page_id="drama", section_id="0", response=full_page_response)

    # Title should come from the ``included`` dict.
    assert sec.title == "Section Title"

    # Path must reflect the page and section identifiers.
    assert sec.manifest_url == "/pages/drama/0"

    assert sec.thumb == None
    assert sec.fanart == None

    # Six plugs should have been instantiated via ``plug_factory``.
    assert len(sec.children) == 6
    assert all(isinstance(p, Base) for p in sec.children)
    # The titles of the children should match the titles in the response
    assert [p.title for p in sec.children] == [
        "Podcast Title: Podcast episode title",
        "Channel title",
        "Program Title: Program subtitle",
        "Podcast title: Podcast subtitle",
        "Series title: Series subtitle",
        "Series title: Episode title: Episode subtitle"
    ]


def test_init_with_section_response(section_response):
    """
    Verify that a Section created from a response that contains an
    ``included`` block extracts the title and creates plug objects.
    """
    sec = Section(page_id="drama", section_id="0", response=section_response)

    # Title should come from the ``included`` dict.
    assert sec.title == "Section Title"

    # Path must reflect the page and section identifiers.
    assert sec.manifest_url == "/pages/drama/0"

    assert sec.thumb == None
    assert sec.fanart == None

    # One plug should have been instantiated via ``plug_factory``.
    assert len(sec.children) == 1
    assert all(isinstance(p, Base) for p in sec.children)
    # The titles of the children should match the titles in the response
    assert [p.title for p in sec.children] == [
        "Podcast Title: Podcast episode title"
    ]


def test_init_without_any_block():
    """
    If the response contains neither ``included`` nor ``placeholder``,
    the title should be ``None`` and no children should be added.
    """
    empty_resp = {"sections": [{"foo": "bar"}]}
    sec = Section(page_id="99", section_id="0", response=empty_resp)

    assert sec.title == "Ingen tittel"
    assert sec.manifest_url == "/pages/99/0"
    assert sec.children == []


def test_from_url_success(full_page_response):
    """
    ``from_url`` should split the URL, request the correct endpoint 
    and return a fully initialised Section.
    """
    



    with mock.patch("nrk.get", return_value=full_page_response) as mocked_get:
        sec = Section.from_url("radio/pages/pagename/0")

        # ---- Assertions about the call ------------------------------
        mocked_get.assert_called_once_with("/radio/pages/pagename")

        # ---- Assertions about the created Section -------------------
        assert sec.id == "0"
        assert sec.manifest_url == "/pages/pagename/0"
        # Title comes from the `included` block of the fake response.
        assert sec.title == "Section Title"
        # Six plugs should have been created via `plug_factory`.
        assert len(sec.children) == 6
        assert [p.title for p in sec.children] == [
        "Podcast Title: Podcast episode title",
        "Channel title",
        "Program Title: Program subtitle",
        "Podcast title: Podcast subtitle",
        "Series title: Series subtitle",
        "Series title: Episode title: Episode subtitle"
    ]


def test_from_url_invalid_format():
    """
    An incorrectly formatted URL should raise ``ValueError``.
    """
    with pytest.raises(ValueError, match="Wrong format of url"):
        _ = Section.from_url("https://example.com/radio/only-two-parts")