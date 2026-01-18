import pytest
from unittest import mock

from nrkradio import Page


@pytest.fixture
def full_page_response():
    """A minimal response containing an ``included`` block."""
    return {
        "title": "Placeholder Page Title",
        "sections": [
            {
                "included": {
                    "title": "Section 1 Title",
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
            },
            {
                "included": {
                    "title": "Section 2 Title",
                    "plugs": [
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
                    ],
                }
            },
        ],
    }


@pytest.fixture
def partial_pageoverview_response():
    return {
        "id": "page-1-id",
        "title": "Page 1 title",
        "image": {
            "id": "019c3cdd-6e05-7b5e-829b-6a4c9ddfa4ce",
            "webImages": [
                {
                    "uri": "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4cegKgTsPQJZae1rsNo2OAiGQ",
                    "width": 300,
                },
                {
                    "uri": "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4ce7hh1hLWNswW1rsNo2OAiGQ",
                    "width": 600,
                },
                {
                    "uri": "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4ceKyiD_s3EMtS1rsNo2OAiGQ",
                    "width": 960,
                },
                {
                    "uri": "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4cezN14j0NRrlu1rsNo2OAiGQ",
                    "width": 1920,
                },
                {
                    "uri": "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4cefOZP8gWnC_e1rsNo2OAiGQ",
                    "width": 2560,
                },
            ],
        },
        "imageSquare": {
            "id": "019c3cdd-c545-778e-a526-4c28dd1edfc6",
            "webImages": [
                {
                    "uri": "https://example.com/019c3cdd-c545-778e-a526-4c28dd1edfc6UG6zSk2546ubgVx8rcIBLw",
                    "width": 300,
                },
                {
                    "uri": "https://example.com/019c3cdd-c545-778e-a526-4c28dd1edfc6uC694XTUenmbgVx8rcIBLw",
                    "width": 600,
                },
                {
                    "uri": "https://example.com/019c3cdd-c545-778e-a526-4c28dd1edfc6Y8ZP28eolNqbgVx8rcIBLw",
                    "width": 960,
                },
                {
                    "uri": "https://example.com/019c3cdd-c545-778e-a526-4c28dd1edfc6tIxagAXA9aWbgVx8rcIBLw",
                    "width": 1920,
                },
                {
                    "uri": "https://example.com/019c3cdd-c545-778e-a526-4c28dd1edfc6adV_E5T3IambgVx8rcIBLw",
                    "width": 2560,
                },
            ],
        },
        "_links": {"self": {"href": "/radio/pages/page-1-id"}},
    }


def test_init_full_page(full_page_response):
    page_id = "page-id"
    page = Page(page_id, full_page_response)
    assert page.id == page_id
    assert len(page.children) == 2
    assert [child.id for child in page.children] == ["0", "1"]
    assert [child.title for child in page.children] == [
        "Section 1 Title",
        "Section 2 Title",
    ]
    assert page.thumb == None
    assert page.fanart == None


def test_init_partial_pageoverview(partial_pageoverview_response):
    page_id = "page-id"
    page = Page(page_id, partial_pageoverview_response)
    assert page.id == page_id
    assert len(page.children) == 0
    assert (
        page.thumb
        == "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4cegKgTsPQJZae1rsNo2OAiGQ"
    )
    assert (
        page.fanart
        == "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4cefOZP8gWnC_e1rsNo2OAiGQ"
    )


def test_from_url_success():
    with mock.patch("nrk.get", return_value=full_page_response) as mocked_get:
        page_id = "page-id"
        page = Page.from_url(f"/radio/pages/{page_id}")

        mocked_get.assert_called_once_with(f"/radio/pages/{page_id}")

        assert page.id == page_id


def test_from_url_invalid_format():
    """
    An incorrectly formatted URL should raise ``ValueError``.
    """
    with pytest.raises(ValueError, match="Wrong format of url"):
        _ = Page.from_url("/radio/pages")
