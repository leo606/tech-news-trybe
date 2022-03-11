import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_source,
    search_by_category,
)

# Requisito 12
input_options_text = """Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por fonte;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair."""

second_input_actions = {
    "0": ("Digite quantas notícias serão buscadas:", get_tech_news),
    "1": ("Digite o título:", search_by_title),
    "2": ("Digite a data no formato aaaa-mm-dd:", search_by_date),
    "3": ("Digite a fonte:", search_by_source),
    "4": ("Digite a categoria:", search_by_category),
}

top_lists_actions = {
    "5": top_5_news,
    "6": top_5_categories,
}


def analyzer_menu():
    option = input(input_options_text)
    if option not in [str(n) for n in range(8)]:
        return print("Opção inválida", file=sys.stderr)

    if option == "7":
        return print("Encerrando script\n")

    if option in second_input_actions.keys():
        value = input(second_input_actions[option][0])
        response = second_input_actions[option][1](value)
        print(response, file=sys.stdout)
    elif option in top_lists_actions.keys():
        print(top_lists_actions[option])
