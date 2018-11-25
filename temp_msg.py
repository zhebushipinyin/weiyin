# -*- coding: utf-8 -*-
# filename: menu.py
import urllib
import json
import datetime
from basic import Basic

# 模板消息
class TemplateMsg(object):
	def __init__(self):
		pass
	def send(self, postData, accessToken):
		postUrl = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % accessToken
		if isinstance(postData, unicode):
			postData = postData.encode('utf-8')
		urlResp = urllib.urlopen(url=postUrl, data=postData)
		print urlResp.read()
		return urlResp.read()

class TmpMsg_buy(TemplateMsg):
	def __init__(self, touser, url = '', keyword1= 'xx门店',keyword2 = '0元',keyword3 = '微信支付',keyword4 = '+0积分'):
		self.openid = touser
		self.url = url
		self.keyword1 = keyword1  # 门店
		self.keyword2 = keyword2  # 金额
		self.keyword3 = keyword3  # 支付方式
		self.keyword4 = keyword4  # 积分
		self.keyword5 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		Data = {
			"touser":self.openid,
			"template_id":"M7oKNwj6hImTEAehQD__DFSPbvKVya9S98aZt3EDKXM",
			"url":"http://weixin.qq.com/download",  
			"data":{
				"first": {
					"value":"恭喜你购买成功！您在%s的消费给您带来了新的积分！"%self.keyword1,
					"color":"#173177"
				},
				"keyword1":{
					"value":self.keyword1,
					"color":"#173177"
				},
				"keyword2": {
					"value":self.keyword2,
					"color":"#173177"
				},
				"keyword3": {
					"value":self.keyword3,
					"color":"#173177"
				},
				"keyword4": {
					"value":self.keyword4,
					"color":"#173177"
				},
				"keyword5": {
					"value":self.keyword5,
					"color":"#173177"
				},
				"remark":{
					"value":"欢迎再次购买！",
					"color":"#173177"
				}
			}
		}
		self.postData = json.dumps(Data)