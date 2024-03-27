import scrapy

class HackerNewsSpider(scrapy.Spider):
    name = "hacker_news"
    start_urls = [
        "https://news.ycombinator.com/"
    ]
    def parse(self, response):
        for article in response.css("tr.athing"):
            yield {
                "title": article.css("a.storylink::text").get(),
                "url": article.css("a.storylink::attr(href)").get(),
                "votes": int(article.css("span.score::text").re_first(r"\d+"))
            }
        next_page = response.css("a.morelink::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)