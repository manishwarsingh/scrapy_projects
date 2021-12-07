import scrapy
from scrapy.selector import Selector
from ..items import OverflowItem
from w3lib.html import remove_tags

class OverflowsSpider(scrapy.Spider):
	name = 'overflow'
	start_urls = ["https://stackoverflow.com/questions"]

	def parse(self, response):
		selector = Selector(response)
		title = response.xpath('//title/text()').extract()
		print(title)

		items = OverflowItem()

		all_Questions = response.xpath('//*[@id="questions"]')

		# for Question in response.xpath('//*[@id="questions"]'):
		# 	yield{
		# 	    'questions':response.css('div.summary h3 ::text').extract(),
		# 		# print (questions)

		# 		'tags': response.css('div.summary a::attr(href)').extract()
		# 		# print(tags)
		# 	}
		for Question in all_Questions:

			questions = response.css('div.summary h3 ::text').extract()
			tags = response.css('div.summary a::attr(href)').extract()
			soluction = selector.css('div.excerpt ::text').extract()
			# remove_tags(soluction)
			post_tags = response.css('div.tags a::text').extract()
			auther_name_href = response.css('div.user-details a::attr(href)').extract()
			auther_name = response.xpath('.//a[@class="user-details"]/text()').extract()

			items['questions'] = questions 
			items['tags'] = tags
			items['soluction'] = soluction
			items['post_tags'] = post_tags
			items['auther_name_href'] = auther_name_href
			items['auther_name'] = auther_name

			yield items
			

		
