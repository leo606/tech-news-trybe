from pprint import pprint
from tech_news.database import db


# Requisito 10
def top_5_news():
    news_list = db.news.aggregate(
        [
            {
                "$addFields": {
                    "sum": {"$sum": ["$shares_count", "$comments_count"]}
                }
            },
            {"$sort": {"sum": -1}},
            {"$limit": 5},
        ]
    )

    return [(item["title"], item["url"]) for item in news_list]


pprint(top_5_news())


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
