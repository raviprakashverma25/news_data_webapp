from typing import List
from components.database_support.model import News
from datetime import datetime


def parse_data_from_api(news_data) -> List[News]:
    news_list = []
    for news_obj in news_data:
        news_obj_values = news_obj["news_obj"]
        news_item = News(
                         id=news_obj_values["hash_id"],
                         title=news_obj_values["title"],
                         author=news_obj_values["author_name"],
                         description=news_obj_values["content"],
                         source=news_obj_values["source_name"],
                         source_link=news_obj_values["source_url"],
                         image_url=news_obj_values["image_url"],
                         source_created_at=datetime.fromtimestamp(news_obj_values["created_at"]/1000))
        news_list.append(news_item)
    return news_list
