from parsel import Selector


class News_details:
    def __init__(self, html_content):
        self.html_content = html_content
        self.select = Selector(html_content)

    def get_page_url(self):
        return self.select.css("head link[rel='canonical']::attr(href)").get()

    def get_title(self):
        return self.select.css("#js-article-title::text").get()

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

    def get_shares_count(self):
        shares = self.select.css(".tec--toolbar__item::text").re_first(r"\d+")
        return int(shares) if shares else 0

    def get_comments_count(self):
        comments = self.select.css(".comment-count::text").re_first(r"\d+")
        return int(comments) if comments else 0

    def get_summary(self):
        summary = self.select.css(
            ".tec--article__body p:first-child *::text"
        ).getall()
        return "".join(summary)

    def get_sources(self):
        sources_title = self.select.css(
            ".tec--article__body-grid > div:nth-last-child(2) h2::text"
        ).get()
        if not sources_title:
            return []

        sources = self.select.css(
            ".tec--article__body-grid > div:nth-last-child(2) a::text"
        ).getall()

        if sources:
            return [*map(lambda src: src.strip(), sources)]

    def get_categories(self):
        categories = self.select.css("#js-categories a::text").getall()
        return ([*map(lambda cat: cat.strip(), categories)])
