import scrapy

urls = []
for id in range(1000000,9000000):
    urls.append('https://quizlet.com/' + str(id) + '/chapter-1-system-analysis-flash-cards/')
    id = id + 1

class QuizletSpider(scrapy.Spider):
    name = "quizlet"
    allowed_domains = ['quizlet.com']
    start_urls = urls

    def parse(self, response):
        question = response.css('a.SetPageTerm-wordText span.TermText::text').extract()
        answer = response.css('a.SetPageTerm-definitionText span.TermText::text').extract()
        row_data = zip(question,answer)
        for item in row_data:
            scraped_info = {
                'question' : item[0],
                'answer' : item[1]
            }
            yield scraped_info

