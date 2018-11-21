# -*- coding: utf-8 -*-
# filename: basic.py
import urllib
import time
import json

class Basic:
	def __init__(self):
		self.__accessToken = ''
		self.__leftTime = 0
	def __real_get_access_token(self):
		# 公众号Appid
		appId = "wxa5a6defe959bd261"
		# AppSecret
		appSecret = "2ae3e583c43dbdf66ea7fb719cc54380"
		# 请求地址，返回{"access_token":"ACCESS_TOKEN","expires_in":7200}
		postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (appId, appSecret))
		urlResp = urllib.urlopen(postUrl)
		urlResp = json.loads(urlResp.read())
		self.__accessToken = urlResp['access_token']
		self.__leftTime = urlResp['expires_in']
	def get_access_token(self):
		if self.__leftTime < 10:
			self.__real_get_access_token()
			return self.__accessToken
	def run(self):
		while(True):
			if self.__leftTime > 10:
				time.sleep(2)
				self.__leftTime -= 2
			else:
				self.__real_get_access_token()