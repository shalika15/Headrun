import scrapy
import datetime
from scrapy.spiders import CrawlSpider
import re
import scrapy
from scrapyheadrun.items import ArticleItem
from dateutil import parser

class MySpider(CrawlSpider):
    name = 'headrun_spider'
    allowed_domains = ['thehindu.com']

    def start_requests(self):
        url = 'https://www.thehindu.com/todays-paper/'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        yield scrapy.Request(url, self.parse, headers=headers)

    def parse(self, response):
        for li in response.css('ul.archive-list li'):
            furl = li.css('a::attr(href)').extract_first()
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
            yield scrapy.Request(furl, self.page_parse, headers=headers)

    def page_parse(self, response):
        try:
            post_id = re.search('article(.+?).ece', response.url).group(1)
        except:
            post_id = 0

        try:
           publish = response.css("div.ut-container > div > span > none::text").extract_first()
           publish =parser.parse(publish.strip())

        except:
           publish =datetime.datetime.now()

        article_item = ArticleItem()
        article_item['post_title'] = response.css('h2.intro::text').extract_first()
        article_item['post_url'] = response.url
        article_item['publish_time'] = publish
        article_item['fetch_time'] = datetime.datetime.now()
        article_item['author']= response.css("span > a.auth-nm::text").extract_first()
        article_item['post_text'] = ''.join(x.extract() for x in response.css("p::text"))
        article_item['post_id'] = post_id

        yield article_item



