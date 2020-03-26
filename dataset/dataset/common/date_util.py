#!/usr/bin/env python
# encoding: utf-8

"""
@author: changxin.cheng
@mail: chengcx1019@gmail.com
@time: 2020-03-26 13:06
"""

import pandas as pd


def get_thurdays_from_date_range(week_day: int, start: str = '2020/3/1', end: str = '2020/3/26') -> list:
	date = pd.date_range(start, end, freq='D')
	return [i.strftime('%Y%m%d') for i in date if int(i.strftime("%w")) == week_day]


if __name__ == '__main__':
	pass
