# -*- coding: utf-8 -*-
# filename: menu.py
import urllib
from basic import Basic

class Menu(object):
	def __init__(self):
		pass
	def create(self, postData, accessToken):
		postUrl = "https://api.weixin.qq.com/cgi-bin/menu/create?access_token=%s" % accessToken
		if isinstance(postData, unicode):
			postData = postData.encode('utf-8')
		urlResp = urllib.urlopen(url=postUrl, data=postData)
		print urlResp.read()

	def query(self, accessToken):
		postUrl = "https://api.weixin.qq.com/cgi-bin/menu/get?access_token=%s" % accessToken
		urlResp = urllib.urlopen(url=postUrl)
		print urlResp.read()

	def delete(self, accessToken):
		postUrl = "https://api.weixin.qq.com/cgi-bin/menu/delete?access_token=%s" % accessToken
		urlResp = urllib.urlopen(url=postUrl)
		print urlResp.read()

	#获取自定义菜单配置接口
	def get_current_selfmenu_info(self, accessToken):
		postUrl = "https://api.weixin.qq.com/cgi-bin/get_current_selfmenu_info?access_token=%s" % accessToken
		urlResp = urllib.urlopen(url=postUrl)
		print urlResp.read()

if __name__ == '__main__':
	myMenu = Menu()
	postJson = """
	{
		"button":
		[
			{
				"name": "优品汇",
				"sub_button":
				[
					{
						"type": "view",
						"name": "商城首页",
						"url": "https://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1445241432"
					},
					{
						"type": "click",
						"name": "我的订单",
						"key": "myList"
					}
				]
			},
			{
				"name": "用户中心",
				"sub_button":
				[
					{
						"type": "view",
						"name": "我的账户",
						"url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
					},
					{
						"type": "view",
						"name": "我的积分",
						"url": "http://mp.weixin.qq.com/wiki?t=resource/res_main&id=mp1418702138&token=&lang=zh_CN"
					},
					{
						"type": "view",
						"name": "我的代码",
						"url": "https://github.com/zhebushipinyin/weiyin"
					}
				]
			},
		  ]
	}
	"""
	accessToken = Basic().get_access_token()
	#myMenu.delete(accessToken)
	myMenu.create(postJson, accessToken)