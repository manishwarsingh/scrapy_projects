# -*- coding: utf-8 -*-
import scrapy


class CountriesSpider(scrapy.Spider):
    name = 'countries'
    allowed_domains = ['www.worldometers.info/population']
    start_urls = ['http://www.worldometers.info/population/']

    def parse(self, response):
        countries = response.xpath("//div[2]/div/ul[8]/li/a")
        for country in countries:

            title = country.xpath("//h1/text()").getall()
            headings = country.xpath("//div[2][@class='ulspaced ulnone']/ul/li/a/text()").getall()
            countries_name = country.xpath("//div[2]/div/ul[8]/li/a/text()").getall()
            countries_href = country.xpath("//div[2]/div/ul[8]/li/a/@href").getall()


        yield {
            'title' : title,
            'headings' : headings,
            'countries_name' : countries_name,
            'countries_href' : countries_href
        }
