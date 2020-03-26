#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin.cheng
@mail: chengcx1019@gmail.com
@time: 2020-03-26 13:02
"""
import os

import scrapy

from common import date_util


class QuotesSpider(scrapy.Spider):
	name = "central_bank"

	def start_requests(self):
		url_pattern = 'https://www.federalreserve.gov/releases/h41/{date_str}/h41.pdf'
		needed_dates = date_util.get_thurdays_from_date_range(4, '1900/1/1', '2020/3/31')
		urls = [url_pattern.format(date_str=item) for item in needed_dates]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		date_str = response.url.split("/")[-2]
		if not os.path.exists('federal_reserve'):
			os.mkdir('federal_reserve')
		filename = 'federal_reserve/%s.pdf' % date_str
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log('Saved file %s' % filename)


if __name__ == '__main__':
	pass
