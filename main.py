# -*- coding: utf-8 -*-
import hashlib
import web
import lxml
import time
import os
import reply
import receive

class WeixinInterface:

	def __init__(self):
		self.app_root = os.path.dirname(__file__)
		self.templates_root = os.path.join(self.app_root, 'templates')
		self.render = web.template.render(self.templates_root)

	def GET(self):
		#获取输入参数
		data = web.input()
		signature=data.signature
		timestamp=data.timestamp
		nonce=data.nonce
		echostr = data.echostr
		#自己的token
		token="hello123" #这里改写你在微信公众平台里输入的token
		#字典序排序
		list=[token,timestamp,nonce]
		list.sort()
		sha1=hashlib.sha1()
		map(sha1.update,list)
		hashcode=sha1.hexdigest()
		#sha1加密算法

		#如果是来自微信的请求，则回复echostr
		if hashcode == signature:
			return echostr
    
    def POST(self):
		webData = web.data()
		print "Handle Post webdata is ", webData
		#后台打日志
		recMsg = receive.parse_xml(webData)
		if isinstance(recMsg, receive.Msg) :
			if recMsg.MsgType == 'text':
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				content = recMsg.Content
				replyMsg = reply.TextMsg(toUser, fromUser, content)
				return replyMsg.send()
			# 回复图片消息
			elif recMsg.MsgType == 'image':
				toUser = recMsg.FromUserName
				fromUser = recMsg.ToUserName
				mediaId = recMsg.MediaId
				replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
				return replyMsg.send()
			
		elif isinstance(recMsg, receive.EventMsg):
			toUser = recMsg.FromUserName
			fromUser = recMsg.ToUserName
			# 被关注时回复消息
			if recMsg.Event == 'subscribe':
				subscribe_text = '欢迎关注=v='
				content = subscribe_text
				replyMsg = reply.TextMsg(toUser, fromUser, content)
				return replyMsg.send()
			elif recMsg.Event == 'CLICK':
				# 点击“我的订单”
				if recMsg.Eventkey == 'myList':
					content = u"编写中，尚未完成".encode('utf-8')
					replyMsg = reply.TextMsg(toUser, fromUser, content)
					return replyMsg.send()
		else:
			print "暂且不处理"
			return "success"