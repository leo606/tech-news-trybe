import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)

input_options_text = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""


def option_zero():
    value = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(value)


def option_one():
    value = input("titulo")
    return search_by_title(value)


def option_two():
    value = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(value)


def option_three():
    value = input("Digite a fonte:")
    return search_by_source(value)


def option_four():
    value = input("Digite a categoria:")
    return search_by_category(value)


def option_five():
    return top_5_news()


def option_six():
    return top_5_categories()


def option_seven():
    return print("Encerrando script\n")


second_input_actions = {
    "0": option_zero,
    "1": option_one,
    "2": option_two,
    "3": option_three,
    "4": option_four,
    "5": option_five,
    "6": option_six,
    "7": option_seven,
}


def analyzer_menu():
    option = input(input_options_text)
    if option not in [str(n) for n in range(8)]:
        return print("Opção inválida", file=sys.stderr)

    try:
        second_input_actions[option]()
    except Exception as err:
        print(err, file=sys.stderr)
