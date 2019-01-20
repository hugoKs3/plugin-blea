from bluepy.btle import Scanner, DefaultDelegate
import time
import logging
import globals

class Tile():
	def __init__(self):
		self.name = 'tile'
		self.ignoreRepeat = False

	def isvalid(self,name,manuf='',data=''):
		if name.lower() == self.name:
			return True
			
	def parse(self,data,mac,name):
		action={}
		action['present'] = 1
		return action
    
	def read(self,mac):
		result={}
		try:
			conn = Connector(mac)
			conn.connect(type='random')
			if not conn.isconnected:
				conn.connect(type='random')
				if not conn.isconnected:
					return
			batteryDatas = bytearray(conn.readCharacteristic('0x17'),type='random')
			result['battery'] = batteryDatas[0]
			result['id'] = mac
			logging.debug(str(result))
            logging.debug('CONNECTOR------Characteristics gotten... '+ str(conn.getCharacteristics())
			return result
		except Exception,e:
			logging.error(str(e))
			conn.disconnect()
		conn.disconnect()
		return result

globals.COMPATIBILITY.append(Tile)