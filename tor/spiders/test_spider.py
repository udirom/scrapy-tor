import scrapy


class TorSpider(scrapy.Spider):
    name = "torspider"

    def start_requests(self):
        urls = [
            'https://3g2upl4pq6kufc4m.onion/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'tor_spider-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)