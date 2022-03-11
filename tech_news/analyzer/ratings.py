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




# Requisito 11
def top_5_categories():
    categories_list = db.news.aggregate(
        [
            {"$unwind": {"path": "$categories"}},
            {"$group": {"_id": "$categories", "count_cat": {"$sum": 1}}},
            {"$sort": {"_id": 1}},
            {"$limit": 5},
        ]
    )
    return [cat["_id"] for cat in categories_list]
