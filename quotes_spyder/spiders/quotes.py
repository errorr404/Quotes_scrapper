# -*- coding: utf-8 -*-
import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['https://quotes.toscrape.com/page/']

    # home_url = "http://quotes.toscrape.com/page/"

    # start_urls = ["http://quotes.toscrape.com/page/" + str(page_num) + '/' for page_num in range(1,20)]
    start_urls=['http://quotes.toscrape.com/']

    output_file = open("quotes.json", "w+")

    def parse(self, response):
        # h1_tag = response.xpath('//h1/a/text()').extract_first()
        # tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()
        #
        # yield {'H1 Tag': h1_tag, 'Tags': tags}
        # /html/body/div[1]/div[2]/div[1]/div[1]
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()


            # self.output_file.write(json.dumps({
            #       'Text':text,
            #       'Author':author,
            #       'Tags':tags
            #       }))
            # self.output_file.write("\n")

            yield{
                  'Text':text,
                  'Author':author,
                  'Tags':tags
                  }

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        print(next_page_url)
        print("-------------------------------------")
        absolute_next_page_url = response.urljoin(next_page_url)
        print(absolute_next_page_url)
        print("---------------------------------------------")

        yield scrapy.Request(absolute_next_page_url)
