import pytest
from unittest import mock

from nrkradio import Podcast, Season


@pytest.fixture
def podcast_manifest():
    return {
        "_links": {
            "self": {"href": "/radio/catalog/podcast/podcast-name"},
            "seasons": [
                {
                    "name": "202602",
                    "href": "/radio/catalog/podcast/podcast-name/seasons/202602",
                    "title": "Februar 2026",
                },
                {
                    "name": "202601",
                    "href": "/radio/catalog/podcast/podcast-name/seasons/202601",
                    "title": "Januar 2026",
                },
            ],
            "userData": {
                "href": "/radio/userdata/podcast/podcast-name/{userId}",
                "templated": True,
            },
            "favourite": {
                "href": "/radio/userdata/{userId}/favourites/podcast/podcast-name",
                "templated": True,
            },
            "episodes": {"href": "/radio/catalog/podcast/podcast-name/episodes"},
            "highlightedEpisode": {
                "href": "/radio/userdata/{userId}/progress/podcast/podcast-name/highlightedProgram",
                "templated": True,
            },
            "primaryAction": {
                "href": "/radio/userdata/{userId}/primaryaction/podcasts/podcast-name",
                "templated": True,
            },
            "share": {"href": "https://example.com/podkast/podcast-name"},
        },
        "seriesType": "standard",
        "type": "podcast",
        "seasonDisplayType": "month",
        "navigationLinks": [],
        "series": {
            "id": "podcast-name",
            "titles": {
                "title": "Podcast title",
                "subtitle": "Podcast subtitle",
            },
            "category": {"id": "category-id", "name": "category name"},
            "image": [
                {
                    "url": "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b3112EXYyR0PkRL8goQ9CQfoZA",
                    "width": 300,
                },
                {
                    "url": "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b311ROi83L76Jtf8goQ9CQfoZA",
                    "width": 600,
                },
                {
                    "url": "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b311outL2MSyoo_8goQ9CQfoZA",
                    "width": 960,
                },
                {
                    "url": "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b311hq1QPfWftqn8goQ9CQfoZA",
                    "width": 1280,
                },
                {
                    "url": "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b311L_pTSxw2erj8goQ9CQfoZA",
                    "width": 1600,
                },
                {
                    "url": "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b311Vn6Zf67d6fj8goQ9CQfoZA",
                    "width": 1920,
                },
            ],
            "backdropImage": [
                {
                    "url": "https://example.com/019c46e6-a6fb-73bb-a48c-325d8550360120DJl9T5Z7eKh112wPtdNQ",
                    "width": 300,
                },
                {
                    "url": "https://example.com/019c46e6-a6fb-73bb-a48c-325d85503601iviNnt34A5KKh112wPtdNQ",
                    "width": 600,
                },
                {
                    "url": "https://example.com/019c46e6-a6fb-73bb-a48c-325d85503601epEmdt6eczGKh112wPtdNQ",
                    "width": 960,
                },
                {
                    "url": "https://example.com/019c46e6-a6fb-73bb-a48c-325d85503601u-G0Drs76n2Kh112wPtdNQ",
                    "width": 1280,
                },
                {
                    "url": "https://example.com/019c46e6-a6fb-73bb-a48c-325d85503601poZaQNr3sLeKh112wPtdNQ",
                    "width": 1600,
                },
                {
                    "url": "https://example.com/019c46e6-a6fb-73bb-a48c-325d85503601jejHSZ_udh6Kh112wPtdNQ",
                    "width": 1920,
                },
            ],
            "posterImage": [],
            "squareImage": [
                {
                    "url": "https://example.com/019c46e7-042e-756f-8f9a-bce6c154e991F6HS86WlEctR-3he47nZKg",
                    "width": 300,
                },
                {
                    "url": "https://example.com/019c46e7-042e-756f-8f9a-bce6c154e991S0a4RSlk-vlR-3he47nZKg",
                    "width": 600,
                },
                {
                    "url": "https://example.com/019c46e7-042e-756f-8f9a-bce6c154e991b4OLFT2BFmxR-3he47nZKg",
                    "width": 960,
                },
                {
                    "url": "https://example.com/019c46e7-042e-756f-8f9a-bce6c154e991Vb8FKln4GSpR-3he47nZKg",
                    "width": 1280,
                },
                {
                    "url": "https://example.com/019c46e7-042e-756f-8f9a-bce6c154e991jM4xS3AUNipR-3he47nZKg",
                    "width": 1600,
                },
            ],
        },
        "_embedded": {
            "episodes": {
                "_links": {
                    "self": {
                        "href": "/radio/catalog/podcast/podcast-name/episodes?page=1&pageSize=20&sort=desc"
                    },
                    "next": {
                        "href": "/radio/catalog/podcast/podcast-name/episodes?page=2&pageSize=20&sort=desc"
                    },
                    "progresses": [
                        {
                            "href": "/radio/userdata/{userId}/progress/podcast/podcast-name?contentIds=H4sIAAAAAAAAAyXRS64tIQgF0AmdnSiFCKOpyMdWzb_9wrtNVoi44XstMinKIR4HXKSwpEB5gxTpc37faytjpAlGuYEtAhYjYdIgFvG_LdmIR14sORs8faEBeRto-ir-fe9hUjY72LMKvG3hKBvsNMxt69bve-dcLiQHe8UESxXMhSCnYUkVzW6rK_uS4MndEfLCZV-QNFDl9W5bfI7lUmy7B7x3oQFLG3Tvuvr7Xp5r1faBnFbglAVbteGjoeshv--tJ-5mH7hndhsZ9G6GjwZKMs1-TZzrzgGyTuo10YA5GtxrmvXe0pRKFZSPg8MFDVBtsHD5G5puRHYwVB9wTUUD7DR4TaXemw89OVbgRFxw7IMGrGiI2EdW37SG8ngKSkrg5xpUeeCphq5vR5hEZSYM2iJgCsMpMwg3OIV5D6WrHEEDxFTg1QvhCNBoyEUm9_e9eiNz97dIB3jzhWZuxG0Ym2910vSteuaDSlbwtYKrHsynYV6r6x1BnjVKFMPvBotf-BoF0QYVv7H_bjr1-ELSc8BzB2zqga8GmztG_QOgS0gNCwMAAA",
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
                                    "href": "/radio/catalog/podcast/podcast-name/episodes/l_019c46e7-582a-76cb-8b53-c0e2abea7bfc"
                                },
                                "playback": {
                                    "href": "/playback/metadata/podcast/podcast-name/l_019c46e7-582a-76cb-8b53-c0e2abea7bfc"
                                },
                                "series": {
                                    "name": "podcast-name",
                                    "href": "/radio/catalog/podcast/podcast-name",
                                    "title": "Podcast title",
                                },
                                "season": {
                                    "name": "202602",
                                    "title": "Februar 2026",
                                    "href": "/radio/catalog/podcast/podcast-name/seasons/202602",
                                    "seriesType": "standard",
                                },
                                "favourite": {
                                    "href": "/radio/userdata/{userId}/favourites/podcast/podcast-name",
                                    "templated": True,
                                },
                                "share": {
                                    "href": "https://example.com/podkast/podcast-name/l_019c46e7-582a-76cb-8b53-c0e2abea7bfc"
                                },
                                "progress": {
                                    "href": "/radio/userdata/{userId}/progress/podcastepisode/podcast-name|l_019c46e7-582a-76cb-8b53-c0e2abea7bfc",
                                    "templated": True,
                                },
                                "recommendations": {
                                    "href": "/radio/recommendations/podcast-name?list=radio_viderenavigasjon_fra_program{&maxNumber}",
                                    "templated": True,
                                },
                            },
                            "id": "019c46e7-dd0b-723b-ae9e-8a4f66f20479",
                            "episodeId": "l_019c46e7-582a-76cb-8b53-c0e2abea7bfc",
                            "titles": {
                                "title": "Podcast episode 1 title",
                                "subtitle": "Podcast episode 1 subtitle",
                            },
                            "originalTitle": "Podcast title",
                            "image": [
                                {
                                    "url": "https://example.com/019c46e8-8257-7b50-a629-70def026f329wifA9oZ07Pu36ahKZaGpwDQ",
                                    "width": 300,
                                },
                                {
                                    "url": "https://example.com/019c46e8-8257-7b50-a629-70def026f329w30RRfaa-vzT6ahKZaGpwDQ",
                                    "width": 600,
                                },
                                {
                                    "url": "https://example.com/019c46e8-8257-7b50-a629-70def026f329wv0ZFsoLm_oT6ahKZaGpwDQ",
                                    "width": 960,
                                },
                                {
                                    "url": "https://example.com/019c46e8-8257-7b50-a629-70def026f329whiBRcbzHO9H6ahKZaGpwDQ",
                                    "width": 1280,
                                },
                                {
                                    "url": "https://example.com/019c46e8-8257-7b50-a629-70def026f329wiojpZwMn5ez6ahKZaGpwDQ",
                                    "width": 1600,
                                },
                                {
                                    "url": "https://example.com/019c46e8-8257-7b50-a629-70def026f329wZaA8XwWw5fH6ahKZaGpwDQ",
                                    "width": 1920,
                                },
                            ],
                            "squareImage": [
                                {
                                    "url": "https://example.com/019c46e8-ab14-7d94-b70a-a8f55219ae72wzDN29YyRVDhPwX_EFNfIA",
                                    "width": 300,
                                },
                                {
                                    "url": "https://example.com/019c46e8-ab14-7d94-b70a-a8f55219ae729lbin9X3mWThPwX_EFNfIA",
                                    "width": 600,
                                },
                                {
                                    "url": "https://example.com/019c46e8-ab14-7d94-b70a-a8f55219ae72s4RlQmo2kVfhPwX_EFNfIA",
                                    "width": 960,
                                },
                                {
                                    "url": "https://example.com/019c46e8-ab14-7d94-b70a-a8f55219ae72yoN9Qmgn5r7hPwX_EFNfIA",
                                    "width": 1280,
                                },
                                {
                                    "url": "https://example.com/019c46e8-ab14-7d94-b70a-a8f55219ae72d-G_kab5O1nhPwX_EFNfIA",
                                    "width": 1600,
                                },
                            ],
                            "duration": "PT15M2S",
                            "date": "2026-02-10T08:00:00+01:00",
                            "durationInSeconds": 902,
                            "usageRights": {
                                "from": {
                                    "date": "2026-02-10T08:00:00+01:00",
                                    "displayValue": "10. februar 2026 kl. 08:00",
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
                            "badges": [{"label": "Ny", "type": "new"}],
                            "category": {"id": "category-id", "name": "category name"},
                        },
                        {
                            "_links": {
                                "self": {
                                    "href": "/radio/catalog/podcast/podcast-name/episodes/l_019c46e9-065f-7c87-bb14-f4c2f62c1270"
                                },
                                "playback": {
                                    "href": "/playback/metadata/podcast/podcast-name/l_019c46e9-065f-7c87-bb14-f4c2f62c1270"
                                },
                                "series": {
                                    "name": "podcast-name",
                                    "href": "/radio/catalog/podcast/podcast-name",
                                    "title": "Podcast title",
                                },
                                "season": {
                                    "name": "202602",
                                    "title": "Februar 2026",
                                    "href": "/radio/catalog/podcast/podcast-name/seasons/202602",
                                    "seriesType": "standard",
                                },
                                "favourite": {
                                    "href": "/radio/userdata/{userId}/favourites/podcast/podcast-name",
                                    "templated": True,
                                },
                                "share": {
                                    "href": "https://example.com/podkast/podcast-name/l_019c46e9-065f-7c87-bb14-f4c2f62c1270"
                                },
                                "progress": {
                                    "href": "/radio/userdata/{userId}/progress/podcastepisode/podcast-name|l_019c46e9-065f-7c87-bb14-f4c2f62c1270",
                                    "templated": True,
                                },
                                "recommendations": {
                                    "href": "/radio/recommendations/podcast-name?list=radio_viderenavigasjon_fra_program{&maxNumber}",
                                    "templated": True,
                                },
                            },
                            "id": "16ded18f75e1e98452a320b4e00a7ff6",
                            "episodeId": "l_019c46e9-065f-7c87-bb14-f4c2f62c1270",
                            "titles": {
                                "title": "Podcast episode 2 title",
                                "subtitle": "Podcast episode 2 subtitle",
                            },
                            "originalTitle": "Podcast title",
                            "image": [
                                {
                                    "url": "https://example.com/019c46e9-e9c8-7605-b642-d8f501927538FlzFicTfH4iSel3Vp_qanQ",
                                    "width": 300,
                                },
                                {
                                    "url": "https://example.com/019c46e9-e9c8-7605-b642-d8f501927538bI50ao6OeY-Sel3Vp_qanQ",
                                    "width": 600,
                                },
                                {
                                    "url": "https://example.com/019c46e9-e9c8-7605-b642-d8f501927538BSqjZUTmi4WSel3Vp_qanQ",
                                    "width": 960,
                                },
                                {
                                    "url": "https://example.com/019c46e9-e9c8-7605-b642-d8f501927538JUYrlDMGD_6Sel3Vp_qanQ",
                                    "width": 1280,
                                },
                                {
                                    "url": "https://example.com/019c46e9-e9c8-7605-b642-d8f501927538KPDGtZZdTT-Sel3Vp_qanQ",
                                    "width": 1600,
                                },
                                {
                                    "url": "https://example.com/019c46e9-e9c8-7605-b642-d8f501927538uxL4fOnJeLiSel3Vp_qanQ",
                                    "width": 1920,
                                },
                            ],
                            "squareImage": [
                                {
                                    "url": "https://example.com/019c46ea-1a12-714e-a8c2-3cc37225e3aa7P9j0IqX7hzlQlJdukWb7A",
                                    "width": 300,
                                },
                                {
                                    "url": "https://example.com/019c46ea-1a12-714e-a8c2-3cc37225e3aaLZR7Z3VMSLblQlJdukWb7A",
                                    "width": 600,
                                },
                                {
                                    "url": "https://example.com/019c46ea-1a12-714e-a8c2-3cc37225e3aaZAtpD87XlwHlQlJdukWb7A",
                                    "width": 960,
                                },
                                {
                                    "url": "https://example.com/019c46ea-1a12-714e-a8c2-3cc37225e3aaWL4cikhwZA_lQlJdukWb7A",
                                    "width": 1280,
                                },
                                {
                                    "url": "https://example.com/019c46ea-1a12-714e-a8c2-3cc37225e3aaVYjiK16KXtPlQlJdukWb7A",
                                    "width": 1600,
                                },
                            ],
                            "duration": "PT15M9S",
                            "date": "2026-02-09T08:00:00+01:00",
                            "durationInSeconds": 909,
                            "usageRights": {
                                "from": {
                                    "date": "2026-02-09T08:00:00+01:00",
                                    "displayValue": "9. februar 2026 kl. 08:00",
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
                            "category": {"id": "category-id", "name": "category name"},
                        },
                    ]
                },
            }
        },
    }


def test_init(podcast_manifest):
    podcast_series_id = "podcast-name"
    podcast = Podcast(podcast_series_id, podcast_manifest)

    assert podcast.title == "Podcast title"
    assert podcast.manifest_url == f"/radio/catalog/podcast/{podcast_series_id}"
    assert podcast.thumb == "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b3112EXYyR0PkRL8goQ9CQfoZA"
    assert podcast.fanart == "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b311Vn6Zf67d6fj8goQ9CQfoZA"
    assert len(podcast.children) == 2
    assert [isinstance(child, Season) for child in podcast.children] == [True, True]
    assert [child.title for child in podcast.children] == [
        "Februar 2026",
        "Januar 2026",
    ]
    assert [child.manifest_url for child in podcast.children] == [
        "/radio/catalog/podcast/podcast-name/seasons/202602",
        "/radio/catalog/podcast/podcast-name/seasons/202601",
    ]
    assert [child.thumb for child in podcast.children] == [ None, None]
    assert [child.fanart for child in podcast.children] == [ None, None]


def test_from_url_success(podcast_manifest):
    podcast_series_id = "podcast-name"
    with mock.patch("nrk.get", return_value=podcast_manifest) as mocked_get:
        podcast = Podcast.from_url(f"/podcasts/{podcast_series_id}")

        # ---- Assertions about the call ------------------------------
        mocked_get.assert_called_once_with(
            f"/radio/catalog/podcast/{podcast_series_id}"
        )

        # ---- Assertions about the created Podcast -------------------
        assert podcast.id == podcast_series_id
        assert podcast.title == "Podcast title"
        assert podcast.manifest_url == f"/radio/catalog/podcast/{podcast_series_id}"
        assert podcast.thumb == "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b3112EXYyR0PkRL8goQ9CQfoZA"
        assert podcast.fanart == "https://example.com/019c46e6-4c9b-74f2-b0bc-20693718b311Vn6Zf67d6fj8goQ9CQfoZA"

        assert len(podcast.children) == 2

def test_from_url_wrong_format():
    
    with pytest.raises(ValueError, match="Wrong format of url"):
        _ = Podcast.from_url("/podcasts/podcast-name/season/season1")
    
