#!/usr/bin/python
# -*- coding: utf-8 -*-
#


from lib.request import *

class Shodan(Request):
	key = "UNmOjxeFS2mPA3kmzm1sZwC0XjaTTksy"
	def __init__(self,ip):
		Request.__init__(self)
		self.ip = ip

	def search(self):
		url = "https://api.shodan.io/shodan/host/{}?key={}".format(self.ip,self.key)
		try:
			resp = self.send(
				method = "GET",
				url = url
				)
			return resp.content
		except Exception,Error:
			pass