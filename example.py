import scrapy


class SP500Spider(scrapy.Spider):
    name = 'sp500'
    start_urls = ['http://www.slickcharts.com/sp500/performance']

    def parse(self, response):
        rows = response.xpath('//table[@id="table table-hover table-borderless table-sm"]/tbody/tr')
        for row in rows:
            yield {
                'number': row.xpath('.//td[1]/text()').get(),
                'company': row.xpath('.//td[2]/a/text()').get(),
                'symbol': row.xpath('.//td[3]/a/text()').get(),
                'ytd_return': row.xpath('.//td[4]/text()').get()
            }

