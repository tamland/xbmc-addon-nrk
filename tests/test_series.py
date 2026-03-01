import pytest
from unittest import mock
from nrkradio import Season, Series


@pytest.fixture
def series_manifest():
    return {
        "_links": {
            "self": {"href": "/radio/catalog/series/series-name"},
            "seasons": [
                {
                    "name": "202505",
                    "href": "/radio/catalog/series/series-name/seasons/202505",
                    "title": "Mai 2025",
                }
            ],
            "userData": {
                "href": "/radio/userdata/series/series-name/{userId}",
                "templated": True,
            },
            "episodes": {"href": "/radio/catalog/series/series-name/episodes"},
            "highlightedEpisode": {
                "href": "/radio/userdata/{userId}/progress/series/series-name/highlightedProgram",
                "templated": True,
            },
            "primaryAction": {
                "href": "/radio/userdata/{userId}/primaryaction/series/series-name",
                "templated": True,
            },
            "favourite": {
                "href": "/radio/userdata/{userId}/favourites/series/series-name",
                "templated": True,
            },
            "share": {"href": "https://example.com/serie/series-name"},
        },
        "seriesType": "standard",
        "type": "series",
        "seasonDisplayType": "month",
        "navigationLinks": [],
        "series": {
            "id": "series-name",
            "highlightedEpisode": "019c4988-393c-724a-870a-42c0bd2450ad",
            "titles": {
                "title": "Series Title",
                "subtitle": "Series Subtitle",
            },
            "category": {"id": "category-id", "name": "Category Name"},
            "image": [
                {
                    "url": "https://example.com/019c4988-b05a-7aec-91ad-71a8263312a96A840Arjkr-_75kmSkSOeg",
                    "width": 300,
                },
                {
                    "url": "https://example.com/019c4988-b05a-7aec-91ad-71a8263312a9f6TFdjHDsoS_75kmSkSOeg",
                    "width": 600,
                },
                {
                    "url": "https://example.com/019c4988-b05a-7aec-91ad-71a8263312a9z6_B4R7EMI-_75kmSkSOeg",
                    "width": 960,
                },
                {
                    "url": "https://example.com/019c4988-b05a-7aec-91ad-71a8263312a9pPd-tw4pzam_75kmSkSOeg",
                    "width": 1280,
                },
                {
                    "url": "https://example.com/019c4988-b05a-7aec-91ad-71a8263312a9kq2A0WiDvdq_75kmSkSOeg",
                    "width": 1600,
                },
                {
                    "url": "https://example.com/019c4988-b05a-7aec-91ad-71a8263312a99tA_ScAmw6e_75kmSkSOeg",
                    "width": 1920,
                },
            ],
            "backdropImage": [
                {
                    "url": "https://example.com/019c4988-f4c5-7632-af5f-625bc43cce77Ak38loT3hqws8y-0S2WgJw",
                    "width": 600,
                },
                {
                    "url": "https://example.com/019c4988-f4c5-7632-af5f-625bc43cce779qKNraIlnXws8y-0S2WgJw",
                    "width": 960,
                },
                {
                    "url": "https://example.com/019c4988-f4c5-7632-af5f-625bc43cce77KKQu1u0Kdaks8y-0S2WgJw",
                    "width": 1600,
                },
                {
                    "url": "https://example.com/019c4988-f4c5-7632-af5f-625bc43cce77EaJkvBz6D9As8y-0S2WgJw",
                    "width": 1920,
                },
            ],
            "squareImage": [
                {
                    "url": "https://example.com/019c4989-4005-7045-9820-ab1a2341c4f54nJCUvcW9IONn2DrwGgbbA",
                    "width": 300,
                },
                {
                    "url": "https://example.com/019c4989-4005-7045-9820-ab1a2341c4f50a2fCCXTediNn2DrwGgbbA",
                    "width": 600,
                },
                {
                    "url": "https://example.com/019c4989-4005-7045-9820-ab1a2341c4f5_C5tvNruZb-Nn2DrwGgbbA",
                    "width": 960,
                },
                {
                    "url": "https://example.com/019c4989-4005-7045-9820-ab1a2341c4f5WzsDjBXC9eGNn2DrwGgbbA",
                    "width": 1280,
                },
                {
                    "url": "https://example.com/019c4989-4005-7045-9820-ab1a2341c4f5A0Qyo5qct_SNn2DrwGgbbA",
                    "width": 1600,
                },
            ],
        },
        "_embedded": {
            "episodes": {
                "_links": {
                    "self": {
                        "href": "/radio/catalog/series/series-name/episodes?page=1&pageSize=20&sort=desc"
                    },
                    "progresses": [
                        {
                            "href": "/radio/userdata/{userId}/progress/series/series-name?contentIds=H4sIAAAAAAAAA_P19g01MDMyMDAzMtXxhXFMkTkmyBxjZI4RMsfQyBQAUnyJvU0AAAA",
                            "templated": True,
                        }
                    ],
                },
                "seriesType": "standard",
                "_embedded": {
                    "episodes": [
                        {
                            "_links": {
                                "self": {
                                    "href": "/radio/catalog/programs/ASDF12345678"
                                },
                                "playback": {
                                    "href": "/playback/metadata/program/ASDF12345678"
                                },
                                "series": {
                                    "name": "series-name",
                                    "href": "/radio/catalog/series/series-name",
                                    "title": "Series Title",
                                },
                                "season": {
                                    "name": "202505",
                                    "title": "Mai 2025",
                                    "href": "/radio/catalog/series/series-name/seasons/202505",
                                    "seriesType": "standard",
                                },
                                "favourite": {
                                    "href": "/radio/userdata/{userId}/favourites/series/series-name",
                                    "templated": True,
                                },
                                "share": {
                                    "href": "https://example.com/serie/series-name/ASDF12345678"
                                },
                                "progress": {
                                    "href": "/radio/userdata/{userId}/progress/programs/ASDF12345678",
                                    "templated": True,
                                },
                                "recommendations": {
                                    "href": "/radio/recommendations/ASDF12345678?list=radio_viderenavigasjon_fra_program{&maxNumber}",
                                    "templated": True,
                                },
                            },
                            "id": "019c4988-393c-724a-870a-42c0bd2450ad",
                            "episodeId": "ASDF12345678",
                            "titles": {
                                "title": "Episode title",
                                "subtitle": "Episode subtitle",
                            },
                            "image": [
                                {
                                    "url": "https://example.com/019c498a-d781-78df-a62b-bea6c5650dc8o3FUALEaZ6FUr_ro5v_InA",
                                    "width": 300,
                                },
                                {
                                    "url": "https://example.com/019c498a-d781-78df-a62b-bea6c5650dc8UGWalBA6tl5Ur_ro5v_InA",
                                    "width": 600,
                                },
                                {
                                    "url": "https://example.com/019c498a-d781-78df-a62b-bea6c5650dc8np805RQb6G5Ur_ro5v_InA",
                                    "width": 960,
                                },
                                {
                                    "url": "https://example.com/019c498a-d781-78df-a62b-bea6c5650dc8gRNnl72vGO9Ur_ro5v_InA",
                                    "width": 1280,
                                },
                                {
                                    "url": "https://example.com/019c498a-d781-78df-a62b-bea6c5650dc8hM3DuGDLR_hUr_ro5v_InA",
                                    "width": 1600,
                                },
                                {
                                    "url": "https://example.com/019c498a-d781-78df-a62b-bea6c5650dc8m2IjJ5GibV1Ur_ro5v_InA",
                                    "width": 1920,
                                },
                            ],
                            "duration": "PT57M",
                            "date": "2025-05-01T15:03:00+02:00",
                            "durationInSeconds": 3420,
                            "usageRights": {
                                "from": {
                                    "date": "2025-05-01T15:03:00+02:00",
                                    "displayValue": "1. mai 2025 kl. 15:03",
                                },
                                "to": {
                                    "date": "2100-01-01T23:03:00+01:00",
                                    "displayValue": "Alltid tilgjengelig",
                                },
                                "geoBlock": {
                                    "isGeoBlocked": False,
                                    "displayValue": "Verden",
                                },
                            },
                            "productionYear": 2025,
                            "availability": {"status": "available", "hasLabel": False},
                            "contributors": [
                                {"name": "Salma Lindgren", "role": "Programleder"},
                                {"name": "Jacob Egeland", "role": "Programleder"},
                                {"name": "Henrik Braaten", "role": "Medvirkende"},
                                {"name": "Alex Borgen", "role": "Lydtekniker"},
                                {
                                    "name": "Mathias Sand",
                                    "role": "Prosjektleder",
                                },
                            ],
                            "badges": [],
                        },
                    ]
                },
            }
        },
    }


def test_init(series_manifest):
    series_id = "series-123"
    manifest_url = f"/radio/catalog/series/{series_id}"

    series = Series(series_id, series_manifest)

    assert series.id == series_id
    assert series.title == "Series Title"
    assert series.manifest_url == manifest_url

    assert len(series.children) == 1
    assert isinstance(series.children[0], Season)
    assert series.children[0].title == "Mai 2025"
    assert (
        series.children[0].manifest_url
        == "/radio/catalog/series/series-name/seasons/202505"
    )
    assert series.children[0].thumb == None
    assert series.children[0].fanart == None


def test_from_url_success(series_manifest):
    series_id = "series-123"
    manifest_url = f"/radio/catalog/series/{series_id}"

    with mock.patch("nrk.get", return_value=series_manifest) as mocked_get:
        series = Series.from_url(f"/series/{series_id}")

        mocked_get.assert_called_once_with(manifest_url)

        assert series.id == series_id
        assert series.title == "Series Title"
        assert series.manifest_url == manifest_url

        assert len(series.children) == 1


def test_from_url_wrong_format():
    with pytest.raises(ValueError, match="Wrong format of url"):
        _ = Series.from_url("/radio/series/series-123")
