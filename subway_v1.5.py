# -*- coding: UTF-8 -*-



#create humanclass
class human():
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def buy_card(self):
		self.CardName = raw_input("카드를 구입합니다. 어떤카드를 구입하시겠습니까? : ")
		self.First_charge = input("최초에 얼마 충전하시겠습니까? : ")

		self.CardName = card(self.age, self.First_charge)

	def brain(self):
		self.decision = input("탑승(환승)을 이용하시겠습니까? (Yes = 1, No = 2) :")
		#self.time = input('현재시간은 몇시 몇분입니까? ex)15시 30분 = 15, 30 :')
		
		if self.decision ==1:
			self.destination = input("목적지와 위치는? ex) 'Pangyo', [3,5]  : ")
			self.choice = input("이용하실 대중교통은? (지하철 = 1 / 버스는 2) : ")
			self.time = input("탑승하시는 시간은 어떻게 됩니까? (15시 30분 = 15, 30) : ")
			if self.choice == 2:
				self.choice = input("탑승하시려는 버스 번호는? : ")
			else:
				pass
		else:
			pass

#create cardclass (+history)
class history():

	list_trafiic = []
	list_location = []
	list_time = []
	transfer_num = 0

	def transfer_count(self): 
		self.transfer_num = self.transfer_num+1
		self.transfer_num = self.transfer_num%5

class card():
	def __init__(self, age, money):
		self.generation = age/10
		self.Present_money = money
		self.listcard = history()


#station
class Management_payment():
	def __init__(self):
		if name.CardName.generation ==1:
			self.basic_pirce = 900
			self.transfer_pirce = 50
		else : 
			self.basic_pirce = 1000
			self.transfer_pirce = 50

	def cal_payment(self, station):
		final_transfer = (station.check_transfer.P_transfer()*station.check_time.P_time())*station.check_traffic.P_traffic()
		if final_transfer == 1:
			result = self.basic_pirce*0 + self.transfer_pirce + station.check_distance.payment_distance(station)
			return result
		else:
			result = self.basic_pirce + self.transfer_pirce*0
			return result


class Management_traffic():
	def P_traffic(self):
		_traffic = name.CardName.listcard.list_trafiic
		_num = name.CardName.listcard.transfer_num
		if _traffic[_num] == _traffic[_num-1]:
			_num = 0
			return 0
		else :
			return 1

class Management_time():
	def P_time(self):
		_List=name.CardName.listcard.list_time
		_num=name.CardName.listcard.transfer_num
		if 0< _num <4:
			result_x = _List[_num][0]*60 + _List[_num][1]
			result_y = _List[_num-1][0]*60 + _List[_num-1][1]
			result = result_x - result_y**2
			if -30 < result < 30 :
				return 1
			else:
				_num
				return 0
		else:
			return 0


class Management_transfer():
	def P_transfer(self):
		_num=name.CardName.listcard.transfer_num
		if  0 < _num < 4:
			return 1
		else:
			_num = 0
			return 0

class Management_distance():
	def payment_distance(self,station):
		_location = name.CardName.listcard.list_location
		_num = name.CardName.listcard.transfer_num
		if 0< _num <4:
			result_x = _location[0] - station.location[0]
			result_y = _location[_traffic][1] - station.location[1]
			result = result_x**2 + result_y**2
			if result >= 25 :
				return int(50)
			else:
				return int(0)
		else:
			return int(0)

class Management_view():
	def printVal(self, station):
		if name.CardName.Present_money >= station.payment:
			transfer_Chance = 4 - name.CardName.listcard.transfer_num
			print '\n\n-------카드정보---------' 
			print '비용 : %d' % station.payment
			name.CardName.Present_money = name.CardName.Present_money - station.payment
			print '잔액 : %d' % name.CardName.Present_money
			print '남은 환승횟수 %d :' % transfer_Chance
			print '------------------------------\n\n'

			transfer_num = name.CardName.listcard.transfer_num
			print 'num %d' % name.CardName.listcard.list_trafiic[transfer_num]
			print 'num-1 %d' % name.CardName.listcard.list_trafiic[transfer_num-1]
			print name.CardName.listcard.list_trafiic
			print name.CardName.listcard.list_time
			print name.CardName.listcard.list_location

		else:
			charge = (station.payment - name.CardName.Present_money)
			print '---------------'
			print '잔액이 부족합니다.'
			print '현재 잔액 %s' % name.CardName.Present_money
			print '부족한 금액 %s' % charge
			print '---------------'

class Management_door():
	def __init__(self, station):
		if name.CardName.Present_money >= station.payment:
			self.open_close = 1
		else: 
			self.open_close = 0

class station():
	def __init__(self, location):
		self.payment = 0 
		self.location = location

	def create_class(self):
		self.check_payment = Management_payment()
		self.check_traffic = Management_traffic()
		self.check_time = Management_time()
		self.check_transfer = Management_transfer()	
		self.check_distance = Management_distance()
		self.view = Management_view()
		self.door = Management_door(self)

	def station_payment(self):
		self.payment = self.check_payment.cal_payment(self)
	
	def station_print(self):
		self.view.printVal(self)

#create def
def Call_machine():
	New_money = raw_input("얼마를 충전하시겠습니까?")
	name.CardName.Present_money = name.CardName.Present_money + New_money


#create user
name = raw_input("당신의 이름은 무엇입니까? : ")
age = input("당신의 나이는 몇살입니까? : ")
name = human(name, age)

#buy_card
name.buy_card()

#start
print '------------'
print '시뮬레이션 시작'
print '------------\n\n\n'

name.brain()

#ing
while name.decision == 1:
	StationName = name.destination[0]
	StationName = station(name.destination[1])

	StationName.create_class()
	
	#insert card_history_list_traffic&location
	name.CardName.listcard.list_trafiic.append(name.choice)
	name.CardName.listcard.list_location.append(StationName.location)
	name.CardName.listcard.list_time.append(name.time)

	StationName.station_payment()
	
	while StationName.door.open_close == 0:
		StationName.station_print()
		Call_machine()	

	StationName.station_print()
	name.CardName.listcard.transfer_count()
	name.brain()


#끝인사
print '----------'
print 'Bye Bye'
print '----------'

