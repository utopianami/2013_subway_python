# -*- coding: UTF-8 -*-

'''
ver 0.1
>나이/환승여부
>5번까지 환승가능

ver 1.0
>지하철간 환승안됨

ver 1.1
>같은 버스 환승안됨

ver 2.0
>카드찍는 기계 클래스 다르게 하기
>환승거리별 요금추가 달리
'''

#ver 0.1

#클래스 1 : 카드 정보


class card():
	name = ''
	age= 0
	transfer_num = 0 #환승수 체크
	transfer_count = 0 #환승값초˙기화
	money = 0
	price = 0

#클래드 2 : 카드 찍는 기계
class machine():
	position = [0,0] #기계위치
	price = 0
	trans_price = 0

	def cal(self): #나이에 따른 요금 책정
		if user.age == 0:
			self.price = 800; self.trans_price = 50
		else:
			self.price = 1000; self.trans_price = 50
	def print_info(self):
		print "-----%s의 카드정보-----" % user.name
		print "비용 : ", self.price
		print "남은돈 : " , user.money
		print "남은 환승횟수 : ", 4-user.transfer_count
		print "-----------------------\n\n\n"

#환승함수
def start():
	start_end = input('교통을 이용하시겠습니까? (탑승 :1, 환승 :2, 내림 0 )')
	return start_end


#객체 생성
user = card()
pangyo = machine()

#정보입력
user.name = raw_input("what is your name ? :  ")
user.age = input("당신의 연령은?(청소년 = 0, 성인 = 1) : ")
user.money = input("얼마를 충전하시겠습니까? : ")
	

#탑승시작
start_end = start()
pangyo.cal() #나이체크
user.transfer_num = user.transfer_num + 1 #환승 수 올리기
user.money = user.money - pangyo.price #잔액
user.transfer_count = user.transfer_num % 5 #환승횟수 초기화
pangyo.print_info()#정보출력
start_end = start()


#지하철 환승
while start_end > 0 :

	user.transfer_num = user.transfer_num + 1 #환승 수 올리기
	user.money = user.money - pangyo.trans_price #잔액
	user.transfer_count = user.transfer_num % 5 #환승횟수 초기화
	pangyo.print_info()#정보출력
	start_end = start()


print '이용해주셔서 감사합니다 :D'
pangyo.print_info()





