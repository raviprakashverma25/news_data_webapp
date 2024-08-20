import json

import pytest
from applications.data_collector.process import parse_data_from_api
from components.database_support.model import News
from datetime import datetime


@pytest.fixture
def mock_news_api_results():
    return json.loads(r"""
        {
        "data": {
            "min_news_id": "ywpyknl5-1",
            "news_list": [
                {
                    "hash_id": "ukck01oe-1",
                    "news_type": "NEWS",
                    "rank": 0,
                    "actions": null,
                    "version": 0,
                    "type": "NEWS",
                    "read_override": false,
                    "fixed_rank": false,
                    "publisher_interaction_meta": {
                        "user_id": "TEzH3iHxzBXqfOZSeyPEbxwkAA62",
                        "is_publisher_followed": false,
                        "show_follow_button": true
                    },
                    "news_obj": {
                        "old_hash_id": "gave-you-my-best--america--prez-biden-as-he-passes-torch-to-harris-1724140689077",
                        "hash_id": "ukck01oe-1",
                        "author_name": "Swati Dubey",
                        "content": "President Joe Biden delivered emotional farewell speech as he passed the torch to Kamala Harris at Democratic National Convention. In his tearful address, Biden said, \"I love the job, but I love my country more\" and described Harris as his \"best decision\". \"America, I gave my best to you,\" he said, reflecting on his 50 years of dedication to US.",
                        "source_url": "https://www.moneycontrol.com/news/world/gave-you-my-best-after-emotional-farewell-speech-president-biden-passes-the-torch-to-harris-12801516.html/amp?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts",
                        "source_name": "Moneycontrol",
                        "title": "Gave you my best, America: Prez Biden as he passes torch to Harris",
                        "important": false,
                        "image_url": "https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/20_tue/img_1724138752602_290.jpg?",
                        "shortened_url": "https://shrts.in/fK5RE",
                        "created_at": 1724140689000,
                        "score": 800,
                        "category_names": [
                            "politics",
                            "world"
                        ],
                        "relevancy_tags": [
                            "world",
                            "politics"
                        ],
                        "tenant": "ENGLISH",
                        "fb_object_id": "",
                        "fb_like_count": 0,
                        "country_code": "IN",
                        "impressive_score": 12.559999999999999,
                        "targeted_city": [

                        ],
                        "gallery_image_urls": [

                        ],
                        "full_gallery_urls": [

                        ],
                        "bottom_headline": " Biden received a standing ovation",
                        "bottom_text": "Tap to know more",
                        "darker_fonts": true,
                        "bottom_panel_link": "https://www.moneycontrol.com/news/world/gave-you-my-best-after-emotional-farewell-speech-president-biden-passes-the-torch-to-harris-12801516.html/amp?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts",
                        "bottom_type": "DEFAULT",
                        "byline_1": [
                            {
                                "type": "TEXT",
                                "text": "swipe left for more at Moneycontrol / "
                            },
                            {
                                "type": "TIME"
                            }
                        ],
                        "byline_2": [
                            {
                                "type": "TEXT",
                                "text": "short by "
                            },
                            {
                                "type": "TEXT",
                                "text": "Swati Dubey"
                            }
                        ],
                        "version": 0,
                        "position_start_time": "1970-01-01T00:00:00Z",
                        "position_expire_time": "2024-08-21T07:57:18.229Z",
                        "trackers": [

                        ],
                        "dfp_tags": "score:800,news:default,cat:politics,cat:world,hash:7",
                        "dont_show_ad": false,
                        "poll_tenant": "ENGLISH",
                        "language": "english",
                        "show_inshorts_brand_name": true,
                        "crypto_coin_preference": null,
                        "is_overlay_supported": true,
                        "news_type": "NEWS",
                        "is_muted": false,
                        "video_audio_type": "USER_SPECIFIED_AUDIO",
                        "auto_play_type": "AUTO_PLAY_USER_SPECIFIED",
                        "show_in_video_feed_only": false,
                        "similar_threshold": 0,
                        "is_similar_feed_available": false,
                        "publisher_info": {
                            "name": "Inshorts",
                            "user_id": "TEzH3iHxzBXqfOZSeyPEbxwkAA62",
                            "user_type": "INSHORTS",
                            "profile_image_url": "https://nis-gs.pix.in/public/images/v1/variants/jpg/m/2024/01_jan/5_fri/img_1704466220628_915.jpg",
                            "thumbnail_image_url": "",
                            "sponsored_text": ""
                        },
                        "show_publisher_info": false,
                        "is_profile_clickable": false,
                        "publisher_interaction_meta": {
                            "user_id": "TEzH3iHxzBXqfOZSeyPEbxwkAA62",
                            "is_publisher_followed": false,
                            "show_follow_button": true
                        },
                        "show_capsule_image": false,
                        "capsule_image_url": "",
                        "capsule_custom_card_id": "",
                        "capsule_custom_card_url": "",
                        "capsule_campaign": "",
                        "is_youtube_video": null,
                        "publishing_status": {

                        }
                    }
                },
                {
                    "hash_id": "ywpyknl5-1",
                    "news_type": "NEWS",
                    "rank": 1,
                    "actions": null,
                    "version": 0,
                    "type": "NEWS",
                    "read_override": false,
                    "fixed_rank": false,
                    "publisher_interaction_meta": {
                        "user_id": "TEzH3iHxzBXqfOZSeyPEbxwkAA62",
                        "is_publisher_followed": false,
                        "show_follow_button": true
                    },
                    "news_obj": {
                        "old_hash_id": "nursing-student-found-dead-at-pg-room-in-delhi--iv-drips-seen-hanging-from-fan-1724139957585",
                        "hash_id": "ywpyknl5-1",
                        "author_name": "Ashley Paul",
                        "content": "A 22-year-old nursing student was found dead with a cannula (a thin tube inserted into a vein to administer medication) in her hand at her PG accommodation in Delhi's New Ashok Nagar, police said. Police found the girl's room locked from inside. The girl's body was found lying on her bed with two IV drips hanging from the ceiling fan.",
                        "source_url": "https://repository.inshorts.com/articles/en/PTI/701dfa96-e42d-4476-a67d-d42b99fb5e02?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts",
                        "source_name": "PTI",
                        "title": "Nursing student found dead at PG room in Delhi, IV drips seen hanging from fan",
                        "important": false,
                        "image_url": "https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/20_tue/img_1724136847982_595.jpg?",
                        "shortened_url": "https://shrts.in/k1Vrq",
                        "created_at": 1724139957000,
                        "score": 800,
                        "category_names": [
                            "national"
                        ],
                        "relevancy_tags": [
                            "national"
                        ],
                        "tenant": "ENGLISH",
                        "fb_object_id": "",
                        "fb_like_count": 0,
                        "country_code": "IN",
                        "native_source_url": "https://article-repository-read.newsinshorts.com/en/v1/article/vendor/PTI/hash_id/701dfa96-e42d-4476-a67d-d42b99fb5e02",
                        "impressive_score": 12.33,
                        "targeted_city": [

                        ],
                        "gallery_image_urls": [

                        ],
                        "full_gallery_urls": [

                        ],
                        "bottom_headline": "It is suspected to be a case of suicide",
                        "bottom_text": "No suicide note was found at the spot",
                        "darker_fonts": true,
                        "bottom_panel_link": "https://repository.inshorts.com/articles/en/PTI/701dfa96-e42d-4476-a67d-d42b99fb5e02?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts",
                        "bottom_type": "DEFAULT",
                        "byline_1": [
                            {
                                "type": "TEXT",
                                "text": "swipe left for more at PTI / "
                            },
                            {
                                "type": "TIME"
                            }
                        ],
                        "byline_2": [
                            {
                                "type": "TEXT",
                                "text": "short by "
                            },
                            {
                                "type": "TEXT",
                                "text": "Ashley Paul"
                            }
                        ],
                        "version": 0,
                        "position_start_time": "1970-01-01T00:00:00Z",
                        "position_expire_time": "2024-08-21T07:44:29.513Z",
                        "trackers": [

                        ],
                        "dfp_tags": "score:800,news:default,cat:national,hash:5,noads:true",
                        "dont_show_ad": true,
                        "poll_tenant": "ENGLISH",
                        "image_for_representation": true,
                        "language": "english",
                        "show_inshorts_brand_name": true,
                        "crypto_coin_preference": null,
                        "is_overlay_supported": false,
                        "news_type": "NEWS",
                        "is_muted": false,
                        "video_audio_type": "USER_SPECIFIED_AUDIO",
                        "auto_play_type": "AUTO_PLAY_USER_SPECIFIED",
                        "show_in_video_feed_only": false,
                        "similar_threshold": 0,
                        "is_similar_feed_available": false,
                        "publisher_info": {
                            "name": "Inshorts",
                            "user_id": "TEzH3iHxzBXqfOZSeyPEbxwkAA62",
                            "user_type": "INSHORTS",
                            "profile_image_url": "https://nis-gs.pix.in/public/images/v1/variants/jpg/m/2024/01_jan/5_fri/img_1704466220628_915.jpg",
                            "thumbnail_image_url": "",
                            "sponsored_text": ""
                        },
                        "show_publisher_info": false,
                        "is_profile_clickable": false,
                        "publisher_interaction_meta": {
                            "user_id": "TEzH3iHxzBXqfOZSeyPEbxwkAA62",
                            "is_publisher_followed": false,
                            "show_follow_button": true
                        },
                        "show_capsule_image": false,
                        "capsule_image_url": "",
                        "capsule_custom_card_id": "",
                        "capsule_custom_card_url": "",
                        "capsule_campaign": "",
                        "is_youtube_video": null,
                        "publishing_status": {

                        }
                    }
                }
            ],
            "reload_required": true,
            "feed_type": "svd"
        },
        "error": false
    }
    """)


def test_parse_data_from_api(mock_news_api_results):
    result = parse_data_from_api(mock_news_api_results["data"]["news_list"])

    expected = [
        News(
            id="ukck01oe-1",
            title="Gave you my best, America: Prez Biden as he passes torch to Harris",
            author="Swati Dubey",
            description="President Joe Biden delivered emotional farewell speech as he passed the torch to Kamala Harris at Democratic National Convention. In his tearful address, Biden said, \"I love the job, but I love my country more\" and described Harris as his \"best decision\". \"America, I gave my best to you,\" he said, reflecting on his 50 years of dedication to US.",
            source="Moneycontrol",
            source_link="https://www.moneycontrol.com/news/world/gave-you-my-best-after-emotional-farewell-speech-president-biden-passes-the-torch-to-harris-12801516.html/amp?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts",
            image_url="https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/20_tue/img_1724138752602_290.jpg?",
            source_created_at=datetime.fromtimestamp(1724140689000/1000)
        ),
        News(
            id="ywpyknl5-1",
            title="Nursing student found dead at PG room in Delhi, IV drips seen hanging from fan",
            author="Ashley Paul",
            description="A 22-year-old nursing student was found dead with a cannula (a thin tube inserted into a vein to administer medication) in her hand at her PG accommodation in Delhi's New Ashok Nagar, police said. Police found the girl's room locked from inside. The girl's body was found lying on her bed with two IV drips hanging from the ceiling fan.",
            source="PTI",
            source_link="https://repository.inshorts.com/articles/en/PTI/701dfa96-e42d-4476-a67d-d42b99fb5e02?utm_campaign=fullarticle&utm_medium=referral&utm_source=inshorts",
            image_url="https://nis-gs.pix.in/inshorts/images/v1/variants/jpg/m/2024/08_aug/20_tue/img_1724136847982_595.jpg?",
            source_created_at=datetime.fromtimestamp(1724139957000/1000)
        ),
    ]

    assert len(result) == len(expected), "Mismatch in number of parsed jobs"

    for r, e in zip(result, expected):
        assert r.id == e.id, f"Expected id {e.id}, but got {r.id}"
        assert r.title == e.title, f"Expected title {e.title}, but got {r.title}"
        assert r.author == e.author, f"Expected author {e.author}, but got {r.author}"
        assert r.description == e.description, f"Expected description {e.description}, but got {r.description}"
        assert r.source == e.source, f"Expected source {e.source}, but got {r.source}"
        assert r.source_link == e.source_link, f"Expected source_link {e.source_link}, but got {r.source_link}"
        assert r.image_url == e.image_url, f"Expected image_url {e.image_url}, but got {r.image_url}"
        assert r.source_created_at == e.source_created_at, f"Expected source_created_at {e.source_created_at}, but got {r.source_created_at}"