import scrapy

baseUrl = 'http://www.billboard.com'

class BillboardSpider(scrapy.Spider):
    name = "Billboard"

    def start_requests(self):
        start_urls = ['http://www.billboard.com/search/dmx?page=1&type=article']
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parseResList)

    def parseResList(self, response):
        urls = response.css('.result__text__title a::attr(href)').extract()
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parseRes)

        next_page = response.css('.pagination a::attr(href)').extract()
        if len(next_page) > 1:
            next_page = response.urljoin(next_page[1])
            yield scrapy.Request(next_page, callback=self.parseResList)

        if len(next_page):
            next_page = response.urljoin(next_page[0])
            yield scrapy.Request(next_page, callback=self.parseResList)

    def parseRes(self, response):
        res = {
            'source': 'Billboard',
            'author': switchArticle(response, '.article__author-link::text', '.author::text')[0],
            'date': switchArticle(response, '.js-publish-date::text', '.js-publish-date::text')[0],
            'title': switchArticle(response, 'h1.longform__title::text', 'h1.article__headline::text')[0],
            'content': "\n".join(switchArticle(response, '.longform__body-primary::text', '.article__body p::text')),
            'subtitle': response.xpath('//meta[contains(@name, "og:description")]/@content').extract()[0],
            'description': response.xpath('//meta[contains(@name, "og:description")]/@content').extract()[0],
            'url': response.xpath('//meta[contains(@name, "og:url")]/@content').extract()[0],
            'imgUrl': response.xpath('//meta[contains(@name, "og:image")]/@content').extract()[0]

        }

        if res['content'] == 'Unknown':
            res['content'] == [res['subtitle']]

        return res

def parseAuthor(response):
    if len(author = response.css('.longform__body-primary::text').extract()):
        return author[0]
    if len(author = response.css('.article__body p::text').extract()):
        return content

def switchArticle(response, url1, url2):
    title = response.css(url1).extract()
    if len(title):
        return title

    title = response.css(url2).extract()
    if len(title):
        return title

    return ['Unknown']
