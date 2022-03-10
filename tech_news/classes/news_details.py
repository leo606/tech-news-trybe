from parsel import Selector


class News_details:
    def __init__(self, html_content):
        self.html_content = html_content
        self.select = Selector(html_content)

    def get_timestamp(self):
        return self.select.css("#js-article-date::attr(datetime)").get()

    def get_writer(self):
        writer = self.select.css(
            ".tec--author__info .tec--author__info__link::text"
        ).get()
        if not writer:
            writer = self.select.css(".tec--author__info p::text").get()
        if not writer:
            writer = self.select.css(
                "#js-article-title + div div:nth-child(2) a::text"
            ).get()

        if writer:
            return writer.strip()
