# -*- coding: UTF-8 -*-

#지하철 카드는 어떻게 돌아갈까?
#구성 : 사람, 리더기, 기계, 문
#고려사항 : 나이, 환승횟수

#card 세팅 : 연령, 가진 돈, 환승횟수, 거리
usercard_age = 0 #(청소년 = 0, 일반인 = 1)
usercard_money = 0
usercard_transfer = 0
transfer = 1


#카드 충전 및 카드 상태설정
usercard_money = input("얼마를 충전하시겠습니까? : ")
usercard_age = input("당신의 연령은 ?(청소년 = 0, 어른 =1) : ")

#연령설정에 따른 기본료, 환승료
def age():
	if usercard_age ==0:
		basic_cost = 800
		transfer_cost = 50
	else:
		basic_cost = 1000
		transfer_cost = 100


while transfer == 1:
	if usercard_transfer == 0:
	
		if usercard_age == 0:
			usercard_money = usercard_money - 800
			usercard_transfer = usercard_transfer + 1
			print(usercard_money)
		else: 
			usercard_money = usercard_money - 1000
			usercard_transfer = usercard_transfer + 1
			print(usercard_money)

	else:
		if usercard_age == 0:
			usercard_money = usercard_money - 50
			usercard_transfer = usercard_transfer + 1
			print(usercard_money)
		else:
			usercard_money = usercard_money - 100
			usercard_transfer = usercard_transfer + 1
			print(usercard_money)

	transfer = input("환승하시겠습니까? Yes=1 , No=0 :")


print("이용해주셔서 감사합니다")





#기능추가
# 5회 이상일 경우 다시 초기값 설정 & 중단
# 거리값에 따라 가중치 부가
# 함수로 만들