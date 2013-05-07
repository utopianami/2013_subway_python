# -*- coding: UTF-8 -*-

#station dict
station_dict = {'konkuk' : [8,5], 'jamsil' : [8,2],'pangyo' : [6,0], 'gangnam' : [6,3], 'sinsa' : [6, 5], 'hongdae' : [1,7], 'dahakro' : [7,7], 'sindorim' : [1,2]}



#human class -> brain Class & traffic_card Class
class human():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def getCard(self):
		print "------------------"
		print "-카드를 구입하셨습니다-"
		print "------------------"

		self.first_charge = input ("최초에 얼마를 충전하시겠습니까?")
		cardName = card(self.age, self.first_charge)

class brain(human):
	def get(self):
		dicision = input("탑승(환승)을 이용하시겠습니까")

		if self.decision ==1:
			print station_dict
			self.destination = raw_input("목적지는 어디입니까?")
			self.traffic = raw_input("이용하실 대중교통은?")
			if self.choice == '버스':
				self.traffic = input("탑승하려는 버스번호는?")

class card(human):
	def __init__(self, age, money):
		self.generation = age/10
		self.present_Money = money

#core System class : getInfo & payment class & door class
	
class coreSystem():
	def __init__(self):
		self.paymentSystem = payment()
		self.getInfoSystem = getInfo()
		self.doorSystem = door()

	def start(self):
		paymentSystem.

class door():
	pass

class print_door(door):
	pass

class getInfo():
	def __init__(self):
		self.userinfo = {}
		transfer_num = 0

	def transfer_count():
		pass

	def addInfo(self, destination):
		pass

	def resetInfo(self):
		pass




	#payment class
class payment():
	def __init__(self):
		self.payment = 0
		if name.cardName.generation == 1:
			self.basic_price = 900
			self.transfer_price == 50
		else:
			self.basic_price = 1000
			self.transfer_price = 100

	def cal_payment(self):
		trasferPriceVal = check_time.Val() * check_traffic.Val() * check_count.Val()

		if trasferPriceVal == 0:
			self.payment = self.basic_price + self.transfer_price * 0
		else:
			self.payment = self.basic_price*0 + self.transfer_price + check_distnace.Val()


class check_time(payment):
	def Val(self):
		pass

class check_traffic(payment):
	def Val(self):
		pass

class check_count(payment):
	def val(self):
		pass

class check_distnace(payment):
	def val(self):
		pass



#create class
name = raw_input("what's your name?")
name = human()





