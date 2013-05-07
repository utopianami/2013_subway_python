# -*- coding: UTF-8 -*-
'''
worn file
222222


ver 1.1
>지하철간 환승안됨

ver 1.2
>같은 버스 환승안됨

ver 2.0
>카드찍는 기계 클래스 다르게 하기
>환승거리별 요금추가 달리
'''

#human_class
class human():
	def __init__(self, name, age, select_traffic):
		self.name = name
		self.age = age
		self.traffic = select_traffic

	def brain(self): #환승여부 생각
		self.decision = input ('탑승(환승) 하시겠습니까? (yes = 1, no = 2)')
		if self.decision == 1:
			self.traffic_transfer = input ('버스? 지하철? (버스 = 1, 지하철 = 2)')

	def complete_transfer(self): #환승 후 이전교통정보를 환승교통정보로 변경 
		self.traffic = self.traffic_transfer

	def get_name(self):
		return self.name

#card_class
class card():
	def __init__(self, age, money): #나이를 연령으로 변경
		self.money = money
		self.generation = age/10
		self.transfer_num = 0
	
	def transfer_count(self): #환승카운트 올리기
		if self.transfer_num <0: #처음에 돈이 없어서 문이 열리지 않을때
			self.transfer_num = 0
		elif 0 <= self.transfer_num < 4: #환승할때
			self.transfer_num = self.transfer_num + 1
		else: # 4초과시 0으로 초기화
			self.transfer_num = 0
			print "환승 횟수가 초과되어, 다음번엔 환승이 적용 되지 않습니다."

#Station_class

class station(card):
	payment = 0

	def __init__(self, generation): #연령에 따라 기본요금/환승요금 설정
		if self.generation == 1:
			self.basic_price = 900
			self.transfer_price = 50
		else:
			self.basic_price = 1000
			self.transfer_price = 100

	def check_traffic(self): # 같은 버스끼리 환승안됨 // 지하철에서 지하철 환승안됨 //
		if userName.traffic_transfer == 2:
			if userName.traffic ==2:
				cardName.transfer_num = 0

	def check_payment(self):
		if 0 < cardName.transfer_num <= 4: #환승일 경우 기본비용 0만들기
			self.payment = self.basic_price*0 + self.transfer_price
		else: #환승이 아닐경우 환승비용을 0으로 만들기
			self.payment = self.basic_price + self.transfer_price*0

	def activity_door(self):
		if  self.payment <= cardName.money:
			print "\n\n-----%s의 카드정보-----" % userName.name
			print "비용 : ", self.payment
			cardName.money = cardName.money - self.payment#잔액만들기
			print "잔액 : " , cardName.money
			print "남은 환승횟수 : ", 4-cardName.transfer_num
			print "-----------------------\n\n"

		else:
			print '요금이 부족합니다. error ---'
			print '현재 잔액 : ', cardName.money
			print '필요 금액', self.payment, '\n\n'
			cardName.money = input('얼마를 충전하시겠습니까? : ')
			cardName.transfer_num = cardName.transfer_num -1 #환승카운트 올리지 않기
	def exit_message(self):
		print "\n\n이용해주셔서 감사합니다."

'''
activity_door 클래스 내부의 
cardName.money 를 card.money로 쓸 수 없을까?
'''

#bascic_info
print '-------------------------'
print '------지하철기본정보-----'
print '-------------------------'

userName = raw_input("당신의 이름은 무엇입니까?? : ")
userAge = input("당신의 나이는 몇살입니까? (ex: 17, 22) : ")
cardName= raw_input("어떤카드를 사용하십니까??\n(ex Tmoney / credit_card / student_card) : ")
Charege_money = input("얼마를 충전하시겠습니까? : ")
select_traffic = input ('어떤 교통을 이용하시겠습니까?(버스=1, 지하철=2) : ')

#making object
userName = human(userName, userAge, select_traffic)
cardName = card(userName.age, Charege_money)
stationName = station(card)

while 1:

	stationName.check_payment() #요금 체크
	stationName.activity_door() #프린트
	cardName.transfer_count() #환승카운트
	userName.brain() #환승여부 물어보기
	stationName.check_traffic() #환승수단에 따라 환승카운트 조절
	userName.complete_transfer()
	if userName.decision ==2:
		break

stationName.exit_message()






