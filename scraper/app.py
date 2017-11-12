import scrapy
from nltk import ConditionalFreqDist, pos_tag, tokenize, data

urls = [
    "http://www.eonline.com/search?query=dmx",
    "https://www.tmz.com/search/news/DMX?adid=TMZ_Web_Nav_Search"
]

class EsquireSpider(scrapy.Spider):
    name = "Esquire"

    def start_requests(self):
        start_urls = [
            'http://www.esquire.com/search/?q=dmx'
        ]
        for url in start_urls:
            yield scrapy.Request(url = url, callback = self.parseResList)

    def parseResList(self, response):
        page = response.url.split("/")[-2]
        baseUrl = response.xpath('//base/@href').extract();
        urls = response.css('.simple-item-title::attr(href)').extract()

        for url in urls:
            url = 'http://www.esquire.com/' + url
            yield scrapy.Request(url = url, callback = self.parseRes)

    def parseRes(self, response):
        return {
            'source': 'Esquire',
            'date': response.xpath('//meta[contains(@name, "sailthru.date")]/@content').extract()[0],
            'title': response.css('h1.content-hed::text').extract()[0],
            'subtitle': response.css('h2.content-dek::text').extract()[0],
            'description': response.xpath('//meta[contains(@name, "og:description")]/@content').extract()[0],
            'url': response.xpath('//meta[contains(@name, "og:url")]/@content').extract()[0],
            'imgUrl': response.xpath('//meta[contains(@name, "og:image")]/@content').extract()[0],
        }


def tagText(text):
    tokenizedText = tokenize.word_tokenize(text)
    return pos_tag(tokenizedText)

def mostCommon(pos, taggedText):
    dist = ConditionalFreqDist((tag, word.lower()) for (word, tag) in taggedText)
    return dist[pos].most_common()
