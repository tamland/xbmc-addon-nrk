import copy
import re
from re import Match
from nrk import Base, deep_get_dict, deep_get_list
from unittest import mock
import pytest

from nrkradio import PodcastEpisode, Season, StandaloneProgram


@pytest.fixture
def season_podcast_manifest():
    return {
        "_links": {
            "self": {"href": "/radio/catalog/podcast/podcast_name/seasons/202601"},
            "podcast": {
                "name": "podcast_name",
                "href": "/radio/catalog/podcast/podcast_name",
                "title": "Podcast Title",
            },
            "episodes": {
                "href": "/radio/catalog/podcast/podcast_name/seasons/202601/episodes"
            },
            "favourite": {
                "href": "/radio/userdata/{userId}/favourites/podcast/podcast_name",
                "templated": True,
            },
            "share": {
                "href": "https://example.com/podkast/podcast_name/sesong/202601"
            },
            "primaryAction": {
                "href": "/radio/userdata/{userId}/primaryaction/podcasts/podcast_name/season/202601",
                "templated": True,
            },
        },
        "seriesType": "standard",
        "type": "podcast",
        "name": "202601",
        "titles": {"title": "Januar 2026"},
        "image": [
            {
                "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeet57DGpRUnjBBlrknzxEqFA",
                "width": 300,
            },
            {
                "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeem1fFySW7hn1BlrknzxEqFA",
                "width": 600,
            },
            {
                "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeeyzzmVDVACd5BlrknzxEqFA",
                "width": 960,
            },
            {
                "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeeSeavXwRZDOtBlrknzxEqFA",
                "width": 1280,
            },
            {
                "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeezv3ALjdBQ75BlrknzxEqFA",
                "width": 1600,
            },
            {
                "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efee-bEFtmssfbJBlrknzxEqFA",
                "width": 1920,
            },
        ],
        "squareImage": [
            {
                "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aJfedFmV-7HunLdQWB0BvZw",
                "width": 300,
            },
            {
                "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42a6EyM5GivinSnLdQWB0BvZw",
                "width": 600,
            },
            {
                "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aAQJXLC_6vRunLdQWB0BvZw",
                "width": 960,
            },
            {
                "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42ajU_KrC4YjqSnLdQWB0BvZw",
                "width": 1280,
            },
            {
                "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aKqkx59Qw8wCnLdQWB0BvZw",
                "width": 1600,
            },
        ],
        "backdropImage": [
            {
                "url": "https://example.com/019c3d87-c3d8-7c62-9b64-fb6df4d0198220DJl9T5Z7eKh112wPtdNQ",
                "width": 300,
            },
            {
                "url": "https://example.com/019c3d87-c3d8-7c62-9b64-fb6df4d01982iviNnt34A5KKh112wPtdNQ",
                "width": 600,
            },
            {
                "url": "https://example.com/019c3d87-c3d8-7c62-9b64-fb6df4d01982epEmdt6eczGKh112wPtdNQ",
                "width": 960,
            },
            {
                "url": "https://example.com/019c3d87-c3d8-7c62-9b64-fb6df4d01982u-G0Drs76n2Kh112wPtdNQ",
                "width": 1280,
            },
            {
                "url": "https://example.com/019c3d87-c3d8-7c62-9b64-fb6df4d01982poZaQNr3sLeKh112wPtdNQ",
                "width": 1600,
            },
            {
                "url": "https://example.com/019c3d87-c3d8-7c62-9b64-fb6df4d01982jejHSZ_udh6Kh112wPtdNQ",
                "width": 1920,
            },
        ],
        "navigationLinks": [],
        "hasAvailableEpisodes": True,
        "episodeCount": 21,
        "category": {"id": "category-id", "name": "Category Name"},
        "_embedded": {
            "episodes": {
                "_links": {
                    "self": {
                        "href": "/radio/catalog/podcast/podcast_name/seasons/202601/episodes?page=1&pageSize=20&sort=desc"
                    },
                    "next": {
                        "href": "/radio/catalog/podcast/podcast_name/seasons/202601/episodes?page=2&pageSize=20&sort=desc"
                    },
                    "progresses": [
                        {
                            "href": "/radio/userdata/{userId}/progress/podcast/podcast_name?contentIds=H4sIAAAAAAAAAyXSQY4EIAgEwA9NJwiI8JqJoJ7m_-cN2SMVE2jw99Ux511JOCMu9NhEzLuQ1NA12ef3vVJvaRLeHv2MA_6WIqmBD4efz--rlnrfIHDcC8070IBBDZl3RHx-33PC-bqDjyS00tAA94aotP-mJ4M5NshdoHc4GhC7Ie9wvp_fN8n3oVnYVQ9aa6MBsxqq1rb5-X3jkivJhbMzVF7AXQlyG7p-HWEw3whT8DKDcgX2jYBpQ3JFdlN-rlVMYOULnb0QrQJTw5kc9j6_r786Z_VY7ARd-uDnLNRroKXvdtKTy30PwT3q0BcX6b4xpGG8uC87gsmkaw7Kt6CWDznpwrzBLV-tvsKYw3dOHJYNHasQwzdyNsRYRR1hPRGZa4D4CdROIEUm1mgIO1G7k5JvqiMw3xu6l6ABRxrWXuLas9V5SiEgZocab8RTQkiDGW-Vz-8rYlTUN7Ve71DFpqK-qZnNoWodwVI9Rx7I6qSSAvccyNNwJEVHH2tuU8-DI3mgmgMNyNPAmmP0f9O3jcsEJ5ZA6200wKSB622uPxZd-XgLAwAA",
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
                                    "href": "/radio/catalog/podcast/podcast_name/episodes/l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae"
                                },
                                "playback": {
                                    "href": "/playback/metadata/podcast/podcast_name/l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae"
                                },
                                "series": {
                                    "name": "podcast_name",
                                    "href": "/radio/catalog/podcast/podcast_name",
                                    "title": "Podcast Title",
                                },
                                "season": {
                                    "name": "202601",
                                    "title": "Januar 2026",
                                    "href": "/radio/catalog/podcast/podcast_name/seasons/202601",
                                    "seriesType": "standard",
                                },
                                "favourite": {
                                    "href": "/radio/userdata/{userId}/favourites/podcast/podcast_name",
                                    "templated": True,
                                },
                                "share": {
                                    "href": "https://example.com/podkast/podcast_name/l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae"
                                },
                                "progress": {
                                    "href": "/radio/userdata/{userId}/progress/podcastepisode/podcast_name|l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae",
                                    "templated": True,
                                },
                                "recommendations": {
                                    "href": "/radio/recommendations/podcast_name?list=radio_viderenavigasjon_fra_program{&maxNumber}",
                                    "templated": True,
                                },
                            },
                            "id": "019c3d89-1808-761e-9218-3bc3dbcfca03",
                            "episodeId": "l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae",
                            "titles": {
                                "title": "Podcast episode title",
                                "subtitle": "Podcast episode subtitle",
                            },
                            "originalTitle": "Podcast Title",
                            "image": [
                                {
                                    "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeet57DGpRUnjBBlrknzxEqFA",
                                    "width": 300,
                                },
                                {
                                    "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeem1fFySW7hn1BlrknzxEqFA",
                                    "width": 600,
                                },
                                {
                                    "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeeyzzmVDVACd5BlrknzxEqFA",
                                    "width": 960,
                                },
                                {
                                    "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeeSeavXwRZDOtBlrknzxEqFA",
                                    "width": 1280,
                                },
                                {
                                    "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeezv3ALjdBQ75BlrknzxEqFA",
                                    "width": 1600,
                                },
                                {
                                    "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efee-bEFtmssfbJBlrknzxEqFA",
                                    "width": 1920,
                                },
                            ],
                            "squareImage": [
                                {
                                    "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aJfedFmV-7HunLdQWB0BvZw",
                                    "width": 300,
                                },
                                {
                                    "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42a6EyM5GivinSnLdQWB0BvZw",
                                    "width": 600,
                                },
                                {
                                    "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aAQJXLC_6vRunLdQWB0BvZw",
                                    "width": 960,
                                },
                                {
                                    "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42ajU_KrC4YjqSnLdQWB0BvZw",
                                    "width": 1280,
                                },
                                {
                                    "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aKqkx59Qw8wCnLdQWB0BvZw",
                                    "width": 1600,
                                },
                            ],
                            "duration": "PT15M3S",
                            "date": "2026-01-30T08:00:00+01:00",
                            "durationInSeconds": 903,
                            "usageRights": {
                                "from": {
                                    "date": "2026-01-30T08:00:00+01:00",
                                    "displayValue": "30. januar 2026 kl. 08:00",
                                },
                                "to": {
                                    "date": "9999-12-22T00:59:59+01:00",
                                    "displayValue": "Alltid tilgjengelig",
                                },
                                "geoBlock": {
                                    "isGeoBlocked": False,
                                    "displayValue": "Verden",
                                },
                            },
                            "availability": {"status": "available", "hasLabel": False},
                            "badges": [],
                            "category": {"id": "category-id", "name": "Category Name"},
                        },
                    ]
                },
            }
        },
    }


@pytest.fixture
def season_podcast_episodes_page_1():
    return {
        "_links": {
            "self": {
                "href": "/radio/catalog/podcast/politisk_kvarter/seasons/202601/episodes?page=1&pageSize=50&sort=desc"
            },
            "progresses": [
                {
                    "href": "/radio/userdata/{userId}/progress/podcast/politisk_kvarter?contentIds=H4sIAAAAAAAAAyXSQY4EIAgEwA9NJwqI8JqJgJ7m_-cN2aMVE2jb31fmWnfHQE2_kNIFX3cjRkOfh35-38v5tsTAO7OvkcPeFsRooCK3-vy-oiH3zQHyeyFxJxowR0PEne6f37fKja4ZqDggGYoGmDV4hv4PrXAiPxhmDLnT0AA_DXGn0f38vjHs1FiJk_kguQ8asLIhcx9dn9_X7zAZfGFkBOHnMJMBvg19fh1hEl13FdBWhVA6znWHSkNQevRQeiaZNEBCF7L6QSQTNBpqkev7_L72smr3WmQDsuXBqjbyNYwt73bSim12JuOWGOT5RZgdTG6Yz--LjqC8xlXDiLchGg-xxoVag2m83N3CXNNOLBTxgcyd8GkHsRp87hwdYT9mXnti0GOIliOYF_ZscC3P00mHnZHFUDsHcjajAcUN-2w26d2yngxnDCKDKB34kwHnBlU6wp_fl1lHju5U-3mnCM7I0Z2q6poi2hE0xGJGgXcn5WCYxURUQ3GwzC5rHRWLQnEURGKiAVENJDFn_zd5RymVUb4Zku-gAcoNlO9QdllcdHT1UEvIqQWno1jVoKcWrz-K8TJfMgMAAA",
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
                            "href": "/radio/catalog/podcast/podcast_name/episodes/l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae"
                        },
                        "playback": {
                            "href": "/playback/metadata/podcast/podcast_name/l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae"
                        },
                        "series": {
                            "name": "podcast_name",
                            "href": "/radio/catalog/podcast/podcast_name",
                            "title": "Podcast Title",
                        },
                        "season": {
                            "name": "202601",
                            "title": "Januar 2026",
                            "href": "/radio/catalog/podcast/podcast_name/seasons/202601",
                            "seriesType": "standard",
                        },
                        "favourite": {
                            "href": "/radio/userdata/{userId}/favourites/podcast/podcast_name",
                            "templated": True,
                        },
                        "share": {
                            "href": "https://example.com/podkast/podcast_name/l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae"
                        },
                        "progress": {
                            "href": "/radio/userdata/{userId}/progress/podcastepisode/podcast_name|l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae",
                            "templated": True,
                        },
                        "recommendations": {
                            "href": "/radio/recommendations/podcast_name?list=radio_viderenavigasjon_fra_program{&maxNumber}",
                            "templated": True,
                        },
                    },
                    "id": "019c3d89-1808-761e-9218-3bc3dbcfca03",
                    "episodeId": "l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae",
                    "titles": {
                        "title": "Podcast episode title",
                        "subtitle": "Podcast episode subtitle",
                    },
                    "originalTitle": "Podcast Title",
                    "image": [
                        {
                            "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeet57DGpRUnjBBlrknzxEqFA",
                            "width": 300,
                        },
                        {
                            "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeem1fFySW7hn1BlrknzxEqFA",
                            "width": 600,
                        },
                        {
                            "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeeyzzmVDVACd5BlrknzxEqFA",
                            "width": 960,
                        },
                        {
                            "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeeSeavXwRZDOtBlrknzxEqFA",
                            "width": 1280,
                        },
                        {
                            "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeezv3ALjdBQ75BlrknzxEqFA",
                            "width": 1600,
                        },
                        {
                            "url": "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efee-bEFtmssfbJBlrknzxEqFA",
                            "width": 1920,
                        },
                    ],
                    "squareImage": [
                        {
                            "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aJfedFmV-7HunLdQWB0BvZw",
                            "width": 300,
                        },
                        {
                            "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42a6EyM5GivinSnLdQWB0BvZw",
                            "width": 600,
                        },
                        {
                            "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aAQJXLC_6vRunLdQWB0BvZw",
                            "width": 960,
                        },
                        {
                            "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42ajU_KrC4YjqSnLdQWB0BvZw",
                            "width": 1280,
                        },
                        {
                            "url": "https://example.com/019c3d87-7f4d-7c5c-9dc0-43bbe95fe42aKqkx59Qw8wCnLdQWB0BvZw",
                            "width": 1600,
                        },
                    ],
                    "duration": "PT15M3S",
                    "date": "2026-01-30T08:00:00+01:00",
                    "durationInSeconds": 903,
                    "usageRights": {
                        "from": {
                            "date": "2026-01-30T08:00:00+01:00",
                            "displayValue": "30. januar 2026 kl. 08:00",
                        },
                        "to": {
                            "date": "9999-12-22T00:59:59+01:00",
                            "displayValue": "Alltid tilgjengelig",
                        },
                        "geoBlock": {
                            "isGeoBlocked": False,
                            "displayValue": "Verden",
                        },
                    },
                    "availability": {"status": "available", "hasLabel": False},
                    "badges": [],
                    "category": {"id": "category-id", "name": "Category Name"},
                }
            ]
        },
    }


@pytest.fixture
def season_series_manifest():
    return {
        "_links": {
            "self": {"href": "/radio/catalog/series/series-name/seasons/202505"},
            "series": {
                "name": "series-name",
                "href": "/radio/catalog/series/series-name",
                "title": "Series Title",
            },
            "episodes": {
                "href": "/radio/catalog/series/series-name/seasons/202505/episodes"
            },
            "primaryAction": {
                "href": "/radio/userdata/{userId}/primaryaction/series/series-name/season/202505",
                "templated": True,
            },
        },
        "seriesType": "standard",
        "type": "series",
        "titles": {"title": "Mai 2025"},
        "image": [
            {
                "url": "https://example.com/019c3dbf-21e5-7889-a986-2eed285434646A840Arjkr-_75kmSkSOeg",
                "width": 300,
            },
            {
                "url": "https://example.com/019c3dbf-21e5-7889-a986-2eed28543464f6TFdjHDsoS_75kmSkSOeg",
                "width": 600,
            },
            {
                "url": "https://example.com/019c3dbf-21e5-7889-a986-2eed28543464z6_B4R7EMI-_75kmSkSOeg",
                "width": 960,
            },
            {
                "url": "https://example.com/019c3dbf-21e5-7889-a986-2eed28543464pPd-tw4pzam_75kmSkSOeg",
                "width": 1280,
            },
            {
                "url": "https://example.com/019c3dbf-21e5-7889-a986-2eed28543464kq2A0WiDvdq_75kmSkSOeg",
                "width": 1600,
            },
            {
                "url": "https://example.com/019c3dbf-21e5-7889-a986-2eed285434649tA_ScAmw6e_75kmSkSOeg",
                "width": 1920,
            },
        ],
        "hasAvailableEpisodes": True,
        "episodeCount": 6,
        "_embedded": {
            "episodes": {
                "_links": {
                    "self": {
                        "href": "/radio/catalog/series/series-name/seasons/202505/episodes?page=1&pageSize=20&sort=desc"
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
                                "self": {"href": "/radio/catalog/programs/YXCVB987654"},
                                "playback": {
                                    "href": "/playback/metadata/program/YXCVB987654"
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
                                    "href": "https://example.com/serie/series-name/YXCVB987654"
                                },
                                "progress": {
                                    "href": "/radio/userdata/{userId}/progress/programs/YXCVB987654",
                                    "templated": True,
                                },
                                "recommendations": {
                                    "href": "/radio/recommendations/YXCVB987654?list=radio_viderenavigasjon_fra_program{&maxNumber}",
                                    "templated": True,
                                },
                            },
                            "id": "8ff58caef93c6e760cf18406e41c8f9a",
                            "episodeId": "YXCVB987654",
                            "titles": {
                                "title": "Program title",
                                "subtitle": "Program subtitle",
                            },
                            "image": [
                                {
                                    "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddo3FUALEaZ6FUr_ro5v_InA",
                                    "width": 300,
                                },
                                {
                                    "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddUGWalBA6tl5Ur_ro5v_InA",
                                    "width": 600,
                                },
                                {
                                    "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddnp805RQb6G5Ur_ro5v_InA",
                                    "width": 960,
                                },
                                {
                                    "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddgRNnl72vGO9Ur_ro5v_InA",
                                    "width": 1280,
                                },
                                {
                                    "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddhM3DuGDLR_hUr_ro5v_InA",
                                    "width": 1600,
                                },
                                {
                                    "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddm2IjJ5GibV1Ur_ro5v_InA",
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
                                {"name": "Sara Amundsen", "role": "Programleder"},
                                {"name": "Viljar Iqbal", "role": "Programleder"},
                                {"name": "Isak Strand", "role": "Medvirkende"},
                                {"name": "Levi Hammer", "role": "Lydtekniker"},
                                {
                                    "name": "Esther Evensen",
                                    "role": "Prosjektleder",
                                },
                            ],
                            "badges": [],
                        }
                    ]
                },
            }
        },
    }


@pytest.fixture
def season_series_episodes_page_1():
    return {
        "_links": {
            "self": {
                "href": "/radio/catalog/series/series-name/seasons/202505/episodes?page=1&pageSize=50&sort=desc"
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
                        "self": {"href": "/radio/catalog/programs/YXCVB987654"},
                        "playback": {"href": "/playback/metadata/program/YXCVB987654"},
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
                            "href": "https://example.com/serie/series-name/YXCVB987654"
                        },
                        "progress": {
                            "href": "/radio/userdata/{userId}/progress/programs/YXCVB987654",
                            "templated": True,
                        },
                        "recommendations": {
                            "href": "/radio/recommendations/YXCVB987654?list=radio_viderenavigasjon_fra_program{&maxNumber}",
                            "templated": True,
                        },
                    },
                    "id": "8ff58caef93c6e760cf18406e41c8f9a",
                    "episodeId": "YXCVB987654",
                    "titles": {
                        "title": "Program title",
                        "subtitle": "Program subtitle",
                    },
                    "image": [
                        {
                            "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddo3FUALEaZ6FUr_ro5v_InA",
                            "width": 300,
                        },
                        {
                            "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddUGWalBA6tl5Ur_ro5v_InA",
                            "width": 600,
                        },
                        {
                            "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddnp805RQb6G5Ur_ro5v_InA",
                            "width": 960,
                        },
                        {
                            "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddgRNnl72vGO9Ur_ro5v_InA",
                            "width": 1280,
                        },
                        {
                            "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddhM3DuGDLR_hUr_ro5v_InA",
                            "width": 1600,
                        },
                        {
                            "url": "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddm2IjJ5GibV1Ur_ro5v_InA",
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
                        {"name": "Sara Amundsen", "role": "Programleder"},
                        {"name": "Viljar Iqbal", "role": "Programleder"},
                        {"name": "Isak Strand", "role": "Medvirkende"},
                        {"name": "Levi Hammer", "role": "Lydtekniker"},
                        {
                            "name": "Esther Evensen",
                            "role": "Prosjektleder",
                        },
                    ],
                    "badges": [],
                }
            ]
        },
    }


@pytest.fixture
def mock_nrk_get(
    season_podcast_manifest,
    season_podcast_episodes_page_1,
    season_series_manifest,
    season_series_episodes_page_1,
):
    def _fake_nrk_get(*, path, params=None):
        podcast_manifest_url = "/radio/catalog/podcast/podcast_name/seasons/202601"
        series_manifest_url = "/radio/catalog/series/series-name/seasons/202505"

        page_size = 0
        page = 0

        if path == podcast_manifest_url and params is None:
            return season_podcast_manifest
        elif path == series_manifest_url and params is None:
            return season_series_manifest
        elif params:
            search_object: Match[str] | None = re.search(r"page=([0-9]+)&", params)
            if search_object:
                page: int = int(search_object.group(1))
            search_object: Match[str] | None = re.search(r"pageSize=([0-9]+)&", params)
            if search_object:
                page_size: int = int(search_object.group(1))

            episodes_on_page: int = _episodes_on_page(page, page_size)

            if path == f"{podcast_manifest_url}/episodes":
                page_copy = copy.deepcopy(season_podcast_episodes_page_1)
                episode_copy = copy.deepcopy(
                    season_podcast_episodes_page_1["_embedded"]["episodes"][0]
                )
            elif path == f"{series_manifest_url}/episodes":
                page_copy = copy.deepcopy(season_series_episodes_page_1)
                episode_copy = copy.deepcopy(
                    season_series_episodes_page_1["_embedded"]["episodes"][0]
                )
            else:
                raise AssertionError(f"Unexpected call: path={path}, params={params}")

            page_copy["_embedded"]["episodes"] = [
                copy.deepcopy(episode_copy) for _ in range(episodes_on_page)
            ]
            return page_copy

        raise AssertionError(f"Unexpected call: path={path}, params={params}")

    def _episodes_on_page(page: int, page_size: int) -> int:
        total_episodes = 80
        full_pages = total_episodes // page_size
        remainder = total_episodes % page_size
        if page <= full_pages:
            return page_size
        elif page == full_pages + 1:
            return remainder
        else:
            return 0

    with mock.patch("nrk.get", side_effect=_fake_nrk_get) as mocked:
        yield mocked


def test_init(season_podcast_manifest):
    title = "Dummy title"
    manifest_url = "/playback/id"
    images = deep_get_list(season_podcast_manifest, "image")
    season: Season = Season(title, manifest_url, images)

    assert season.title == title
    assert season.manifest_url == manifest_url
    assert (
        season.thumb
        == "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeet57DGpRUnjBBlrknzxEqFA"
    )
    assert (
        season.fanart
        == "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efee-bEFtmssfbJBlrknzxEqFA"
    )


def test_from_url_from_season_success(season_podcast_manifest):

    podcast_series_id = "podcast_name"
    podcast_season_id = "202601"
    manifest_url = (
        f"/radio/catalog/podcast/{podcast_series_id}/seasons/{podcast_season_id}"
    )

    with mock.patch("nrk.get", return_value=season_podcast_manifest) as mocked_get:
        season: Season = Season.from_url(manifest_url)

        mocked_get.assert_called_once_with(manifest_url)

        assert season.title == "Januar 2026"
        assert season.manifest_url == manifest_url
        assert (
            season.thumb
            == "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeet57DGpRUnjBBlrknzxEqFA"
        )
        assert (
            season.fanart
            == "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efee-bEFtmssfbJBlrknzxEqFA"
        )


def test_from_url_from_plug_success(season_series_manifest):

    podcast_series_id = "series-name"
    podcast_season_id = "202505"
    manifest_url = (
        f"/radio/catalog/series/{podcast_series_id}/seasons/{podcast_season_id}"
    )

    with mock.patch("nrk.get", return_value=season_series_manifest) as mocked_get:
        season: Season = Season.from_url(manifest_url)

        mocked_get.assert_called_once_with(manifest_url)

        assert season.title == "Mai 2025"
        assert season.manifest_url == manifest_url
        assert (
            season.thumb
            == "https://example.com/019c3dbf-21e5-7889-a986-2eed285434646A840Arjkr-_75kmSkSOeg"
        )
        assert (
            season.fanart
            == "https://example.com/019c3dbf-21e5-7889-a986-2eed285434649tA_ScAmw6e_75kmSkSOeg"
        )


def test_from_url_wrong_format():
    with pytest.raises(ValueError, match="Wrong format of url"):
        _ = Season.from_url("/radio/only-two-parts")


def test_get_children_of_podcast(
    mock_nrk_get, season_podcast_manifest, season_podcast_episodes_page_1
):
    podcast_series_id = "podcast_name"
    podcast_season_id = "202601"
    manifest_url = (
        f"/radio/catalog/podcast/{podcast_series_id}/seasons/{podcast_season_id}"
    )
    total_episodes = 80
    season: Season = Season("Dummy title", manifest_url, [])

    children: list[Base] = season.children

    mock_nrk_get.assert_has_calls(
        calls=[
            mock.call(path=f"{manifest_url}"),
            mock.call(
                path=f"{manifest_url}/episodes",
                params="&page=1&pageSize=50&sort=desc",
            ),
            mock.call(
                path=f"{manifest_url}/episodes",
                params="&page=2&pageSize=50&sort=desc",
            ),
        ]
    )
    assert len(children) == total_episodes
    assert [isinstance(child, PodcastEpisode) for child in children] == [
        True for _ in range(total_episodes)
    ]
    assert children[0].title == "Podcast episode title"
    assert (
        children[0].manifest_url
        == "/playback/manifest/podcast/podcast_name/l_019c3dbd-bb8b-73b7-80c7-31536d3d90ae"
    )
    assert (
        children[0].thumb
        == "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efeet57DGpRUnjBBlrknzxEqFA"
    )
    assert (
        children[0].fanart
        == "https://example.com/019c3d87-3ca5-7fe2-a9fe-5fcf8eb2efee-bEFtmssfbJBlrknzxEqFA"
    )


def test_get_children_of_podcast_multiple_calls(
    mock_nrk_get, season_podcast_manifest, season_podcast_episodes_page_1
):
    podcast_series_id = "podcast_name"
    podcast_season_id = "202601"
    manifest_url = (
        f"/radio/catalog/podcast/{podcast_series_id}/seasons/{podcast_season_id}"
    )
    total_episodes = 80
    season: Season = Season("Dummy title", manifest_url, [])

    children: list[Base] = season.children
    children: list[Base] = season.children
    children: list[Base] = season.children
    children: list[Base] = season.children
    children: list[Base] = season.children

    mock_nrk_get.assert_has_calls(
        calls=[
            mock.call(path=f"{manifest_url}"),
            mock.call(
                path=f"{manifest_url}/episodes",
                params="&page=1&pageSize=50&sort=desc",
            ),
            mock.call(
                path=f"{manifest_url}/episodes",
                params="&page=2&pageSize=50&sort=desc",
            ),
        ]
    )
    assert len(children) == total_episodes


def test_get_children_of_series(mock_nrk_get):
    podcast_series_id = "series-name"
    podcast_season_id = "202505"
    manifest_url = (
        f"/radio/catalog/series/{podcast_series_id}/seasons/{podcast_season_id}"
    )
    total_episodes = 80
    season: Season = Season("Dummy title", manifest_url, [])

    children: list[Base] = season.children

    mock_nrk_get.assert_has_calls(
        calls=[
            mock.call(path=f"{manifest_url}"),
            mock.call(
                path=f"{manifest_url}/episodes",
                params="&page=1&pageSize=50&sort=desc",
            ),
            mock.call(
                path=f"{manifest_url}/episodes",
                params="&page=2&pageSize=50&sort=desc",
            ),
        ]
    )

    assert len(children) == total_episodes
    assert [isinstance(child, StandaloneProgram) for child in children] == [
        True for _ in range(total_episodes)
    ]
    assert children[0].title == "Program title"
    assert children[0].manifest_url == "/playback/manifest/program/YXCVB987654"
    assert (
        children[0].thumb
        == "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddo3FUALEaZ6FUr_ro5v_InA"
    )
    assert (
        children[0].fanart
        == "https://example.com/019c3dc1-2130-79e2-a352-fd9c18a518ddm2IjJ5GibV1Ur_ro5v_InA"
    )


def test_get_children_of_series_multiple_calls(mock_nrk_get):
    podcast_series_id = "series-name"
    podcast_season_id = "202505"
    manifest_url = (
        f"/radio/catalog/series/{podcast_series_id}/seasons/{podcast_season_id}"
    )
    total_episodes = 80
    season: Season = Season("Dummy title", manifest_url, [])

    children: list[Base] = season.children
    children: list[Base] = season.children
    children: list[Base] = season.children
    children: list[Base] = season.children
    children: list[Base] = season.children

    mock_nrk_get.assert_has_calls(
        calls=[
            mock.call(path=f"{manifest_url}"),
            mock.call(
                path=f"{manifest_url}/episodes",
                params=f"&page=1&pageSize=50&sort=desc",
            ),
            mock.call(
                path=f"{manifest_url}/episodes",
                params="&page=2&pageSize=50&sort=desc",
            ),
        ]
    )

    assert len(children) == total_episodes
