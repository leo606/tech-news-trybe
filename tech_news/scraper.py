import time
import requests
from parsel import Selector
from tech_news.classes.news_details import News_details


# Requisito 1
def fetch(url):
    time.sleep(1)
    try:
        response = requests.get(url, timeout=3)
        response.raise_for_status()
    except requests.ReadTimeout:
        return
    except requests.HTTPError:
        return
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    select = Selector(html_content)
    url_list = select.css(
        ".tec--list.tec--list--lg a.tec--card__title__link::attr(href)"
    ).getall()
    return url_list


# Requisito 3
def scrape_next_page_link(html_content):
    select = Selector(html_content)
    url_next_page = select.css(
        ".tec--list.tec--list--lg > a:last-child::attr(href)"
    ).get()
    return url_next_page


# Requisito 4
def scrape_noticia(html_content):
    news_details = News_details(html_content)

    return {
        "url": news_details.get_page_url(),
        "title": news_details.get_title(),
        "timestamp": news_details.get_timestamp(),
        "writer": news_details.get_writer(),
        "shares_count": news_details.get_shares_count(),
        "comments_count": news_details.get_comments_count(),
        "summary": news_details.get_summary(),
        "sources": news_details.get_sources(),
        "categories": news_details.get_categories(),
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
