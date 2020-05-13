import scrapy

class OneMotoringSpider(scrapy.Spider):
    name = "onemotoring"
    allowed_domains = ["onemotoring.com.sg"]
    start_urls = [
        'https://www.onemotoring.com.sg/content/onemotoring/home/driving/traffic_information/traffic-cameras/woodlands.html/'
    ]

    def parse(self, response):
        title = response.css('div.col-md-6').css('div.card').css('div.card-text h6::text').extract()
        datetime = response.css('div.col-md-6').css('div.card').css('div.card-text span::text').extract()
        image = response.css('div.col-md-6').css('div.card').css('img::attr(src)').extract()
        row_data = zip(title,datetime,image)
        for item in row_data:
            scraped_info = {
                'title' : item[0],
                'datetime' : item[1],
                'image' : item[2]
            }
            yield scraped_info