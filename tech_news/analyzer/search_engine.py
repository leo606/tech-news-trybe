import re
from tech_news.database import db
from datetime import datetime, timedelta


# Requisito 6
def search_by_title(title):
    reg = re.compile(title, re.IGNORECASE)
    list = db.news.find({"title": {"$regex": reg}})
    return [(item["title"], item["url"]) for item in list]


# Requisito 7
def search_by_date(date):
    try:
        timestamp = datetime.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")

    tomorrow = timestamp + timedelta(days=1)
    list = db.news.find(
        {
            "timestamp": {
                "$gte": timestamp.isoformat(),
                "$lt": tomorrow.isoformat(),
            }
        }
    )
    return [(item["title"], item["url"]) for item in list]


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
