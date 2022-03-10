import re
from tech_news.database import db


# Requisito 6
def search_by_title(title):
    reg = re.compile(title, re.IGNORECASE)
    list = db.news.find({"title": {"$regex": reg}})
    return [(item["title"], item["url"]) for item in list]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
