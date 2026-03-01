from unittest import mock
import pytest

from nrk import Base
from nrkradio import PagesOverview


@pytest.fixture
def pages():
    return {
        "pages": [
            {
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
            },
            {
                "id": "page-2-id",
                "title": "Page 2 title",
                "image": {
                    "id": "019c3cdd-f815-7095-bcd6-4f83c47b2fc3",
                    "webImages": [
                        {
                            "uri": "https://example.com/019c3cdd-f815-7095-bcd6-4f83c47b2fc3hjIvsjAz3RBv3M7W1gol9w",
                            "width": 300,
                        },
                        {
                            "uri": "https://example.com/019c3cdd-f815-7095-bcd6-4f83c47b2fc3fZky2QUeIQVv3M7W1gol9w",
                            "width": 600,
                        },
                        {
                            "uri": "https://example.com/019c3cdd-f815-7095-bcd6-4f83c47b2fc3vxJrCrGtMFZv3M7W1gol9w",
                            "width": 960,
                        },
                        {
                            "uri": "https://example.com/019c3cdd-f815-7095-bcd6-4f83c47b2fc3s-tlf2PK7ixv3M7W1gol9w",
                            "width": 1920,
                        },
                        {
                            "uri": "https://example.com/019c3cdd-f815-7095-bcd6-4f83c47b2fc3OWkkME37HaNv3M7W1gol9w",
                            "width": 2560,
                        },
                    ],
                },
                "imageSquare": {
                    "id": "019c3cde-1bcd-7b86-a26c-01cfd54d9eac",
                    "webImages": [
                        {
                            "uri": "https://example.com/019c3cde-1bcd-7b86-a26c-01cfd54d9eacWQujeV-P_F0K65LK4HQ9qQ",
                            "width": 300,
                        },
                        {
                            "uri": "https://example.com/019c3cde-1bcd-7b86-a26c-01cfd54d9eachf3qrMP7znwK65LK4HQ9qQ",
                            "width": 600,
                        },
                        {
                            "uri": "https://example.com/019c3cde-1bcd-7b86-a26c-01cfd54d9eacYc1bu5OoeFYK65LK4HQ9qQ",
                            "width": 960,
                        },
                        {
                            "uri": "https://example.com/019c3cde-1bcd-7b86-a26c-01cfd54d9eacBuVY-q0fdRgK65LK4HQ9qQ",
                            "width": 1920,
                        },
                        {
                            "uri": "https://example.com/019c3cde-1bcd-7b86-a26c-01cfd54d9eac6iL1U-Bp6XAK65LK4HQ9qQ",
                            "width": 2560,
                        },
                    ],
                },
                "_links": {"self": {"href": "/radio/pages/page-2-id"}},
            },
        ],
        "_links": {"self": {"href": "/radio/pages"}},
    }


def test_init(pages):
    with mock.patch("nrk.get", return_value=pages) as mocked_get:
        pages_overview = PagesOverview()

        mocked_get.assert_called_once_with("/radio/pages")

        assert pages_overview.manifest_url == "/radio/pages"

        assert len(pages_overview.children) == 2
        assert all(isinstance(p, Base) for p in pages_overview.children)
        # The titles of the children should match the titles in the response
        assert [p.id for p in pages_overview.children] == ["page-1-id", "page-2-id"]
        assert [p.thumb for p in pages_overview.children] == [
            "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4cegKgTsPQJZae1rsNo2OAiGQ",
            "https://example.com/019c3cdd-f815-7095-bcd6-4f83c47b2fc3hjIvsjAz3RBv3M7W1gol9w",
        ]
        assert [p.fanart for p in pages_overview.children] == [
            "https://example.com/019c3cdd-6e05-7b5e-829b-6a4c9ddfa4cefOZP8gWnC_e1rsNo2OAiGQ",
            "https://example.com/019c3cdd-f815-7095-bcd6-4f83c47b2fc3OWkkME37HaNv3M7W1gol9w"
        ]
