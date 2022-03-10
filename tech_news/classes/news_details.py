from parsel import Selector


class News_details:
    def __init__(self, html_content):
        self.html_content = html_content

    def get_writer(self):
        select = Selector(self.html_content)
        writer = select.css(
            ".tec--author__info .tec--author__info__link::text"
        ).get()
        if not writer:
            writer = select.css(".tec--author__info p::text").get()
        if not writer:
            writer = select.css(
                "#js-article-title + div div:nth-child(2) a::text"
            ).get()

        if writer:
            return writer.strip()
