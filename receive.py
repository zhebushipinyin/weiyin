# -*- coding: utf-8 -*-
# filename: receive.py
import xml.etree.ElementTree as ET


def parse_xml(web_data):
	if len(web_data) == 0:
		return None
	xmlData = ET.fromstring(web_data)
	msg_type = xmlData.find('MsgType').text
	if msg_type == 'text':
		return TextMsg(xmlData)
	elif msg_type == 'image':
		return ImageMsg(xmlData)
	# 增加了event 的判定
	elif msg_type == 'event':
		event_type = xmlData.find('Event').text
		# 点击
		if event_type == 'CLICK':
			return Click(xmlData)
		# 关注
		elif event_type == 'subscribe':
			return Subscribe(xmlData)
		# 查看链接
		elif event_type == 'VIEW':
			return View(xmlData)
		elif event_type == 'LOCATION':
			return LocationEvent(xmlData)
		elif event_type == 'SCAN':
			return Scan(xmlData)

# 消息类
class Msg(object):
	def __init__(self, xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		
class TextMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.Content = xmlData.find('Content').text.encode("utf-8")
		self.MsgId = xmlData.find('MsgId').text
		
class ImageMsg(Msg):
	def __init__(self, xmlData):
		Msg.__init__(self, xmlData)
		self.PicUrl = xmlData.find('PicUrl').text
		self.MsgId = xmlData.find('MsgId').text
		self.MediaId = xmlData.find('MediaId').text
		
		
# 增加了event类
class EventMsg(object):
	def __init__(self, xmlData):
		self.ToUserName = xmlData.find('ToUserName').text
		self.FromUserName = xmlData.find('FromUserName').text
		self.CreateTime = xmlData.find('CreateTime').text
		self.MsgType = xmlData.find('MsgType').text
		self.Event = xmlData.find('Event').text
		
class Click(EventMsg):
	def __init__(self, xmlData):
		EventMsg.__init__(self, xmlData)
		self.Eventkey = xmlData.find('EventKey').text

class Subscribe(EventMsg):
	def __init__(self, xmlData):
		EventMsg.__init__(self, xmlData)