import scrapy

baseUrl = 'http://www.esquire.com'

class EsquireSpider(scrapy.Spider):
    name = "Esquire"

    def start_requests(self):
        start_urls = [
            'http://www.esquire.com/search/?q=dmx'
        ]
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parseResList)

    def parseResList(self, response):
        urls = response.css('.simple-item-title::attr(href)').extract()

        for url in urls:
            yield scrapy.Request(url = baseUrl + '/' + url, callback = self.parseRes)

    def parseRes(self, response):
        return {
            'source': 'Esquire',
            'date': response.xpath('//meta[contains(@name, "sailthru.date")]/@content').extract()[0],
            'title': response.css('h1.content-hed::text').extract()[0],
            'subtitle': response.xpath('//meta[contains(@name, "og:description")]/@content').extract()[0],
            'description': response.xpath('//meta[contains(@name, "og:description")]/@content').extract()[0],
            'url': response.xpath('//meta[contains(@name, "og:url")]/@content').extract()[0],
            'imgUrl': response.xpath('//meta[contains(@name, "og:image")]/@content').extract()[0],
            'content': response.css('p.body-text::text').extract()[0],
        }
