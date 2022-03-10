from pprint import pprint
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
        "title": news_details.get_title(),
        "timestamp": news_details.get_timestamp(),
        "writer": news_details.get_writer(),
    }


file_pixel = "tests/assets/tecmundo_pages/dispositivos-moveis|215327-pixel-5a-tera-lancamento-limitado-devido-escassez-chips.htm.html"
file_viloes = "tests/assets/tecmundo_pages/minha-serie|215168-10-viloes-animes-extremamente-inteligentes.htm.html"
file_seg = "tests/assets/tecmundo_pages/seguranca|215274-pmes-principais-alvos-ataques-ciberneticos.htm.html"

with open(file_viloes) as file:
    read_file = file.read()

pprint(scrape_noticia(read_file))


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
