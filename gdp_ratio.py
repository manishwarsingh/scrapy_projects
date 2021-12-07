# -*- coding: utf-8 -*-
import scrapy


class GdpRatioSpider(scrapy.Spider):
    name = 'gdp_ratio'
    allowed_domains = ['worldpopulationreview.com/countries/countries-by-national-debt']
    start_urls = ['http://worldpopulationreview.com/countries/countries-by-national-debt/']

    def parse(self, response):
        rows = response.xpath("//tbody[@class='jsx-2642336383']/tr")
        for row in rows:
            Countries_name = row.xpath("//tbody[@class='jsx-2642336383']/tr/td/a/text()").get()
            Gdp_debt = row.xpath("//tbody[@class='jsx-2642336383']/tr/td/text()").get()
            Populatin_Of_Countries = row.xpath("//tbody[@class='jsx-2642336383']/tr/td[3]/text()").get()
            yield {
            'Countries_name' : Countries_name,
            'Gdp_debt' : Gdp_debt,
            'Populatin_Of_Countries' :Populatin_Of_Countries
            }
        
