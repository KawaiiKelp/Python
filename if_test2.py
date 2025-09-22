""" # 제어문 - 조건문(선택문) if    if~else     if~elif~else

# 1. 단일 선택문(if)
num = int(input("자연수 입력: "))
if num % 2 == 0: # 홀짝판별
    print("*", end='')
print(num)
# 2-1. 이중 선택문(if~else) 홀짝 판별
num = int(input("자연수 입력: "))
if num % 2 == 0: # 짝수라면
    print("짝수입니다람쥐썬더우르릉ㅇㅇ코앙오ㅇㅇ")
else: # 홀수라면
    print("홀수입니다람쥐썬더코ㅗ컼옼오커오카ㅓㅇ카ㅗ아쾅")

age = int(input("나이 입력: "))
if age >= 17:
    print("다컸구나")
else:
    print("많이커라")


# 2-3. 점수를 입력받아 60점 이상이면 합격 그렇지 않으면 불합격 출력
score = int(input("점수 입력"))
if score >= 60:
    print("합격")
    print("신난다")
else: 
    print("불합격")
    print("죽어야겠다")
print("화이팅? NO! 블래킹하자")

# 3-1. 다중 선택문 if~elif~else
# 나이가 8세 미만이라면 "유아" 8세 이상 ~ 19세 이하 "학생" 그 외 "성읹"
age = int(input("나이 입력: "))
if age < 8:
    print("유아")
elif 8 <= age <= 19:
    print("학생")
else:
    print("성인")

# 3-2. 요일별 게임조건 일요일 게임열판하기 토요일 밤새서 게임하기 평일 물한잔하기 => 공부시작
today = str(input("오늘은 무슨 요일? "))
if today == "일요일":
    print("게임 열 판 하기")
elif today == "토요일":
    print("밤 새서 게임하기")
else:
    print("물 한 잔 하기")
print("공부 시작")

"""

# 리조트에 객실당 4명의 손님까지 무료 입장입니다.
# 입장 인원을 입력하여 입장인원이 4명 이하이면 "추가 비용 없습니다"
# 입장 인원이 4명보다 많으면 "추가비용 1인당 1만원입니다"라는 메시지를 출력

import time


total = int(input("투숙객 수를 입력하세요: "))
if total <= 4:
    print("추가 비용 없습니다")
elif 4 <= total < 8:
    print(f"추가 비용 {total-4}인당 {total-4}만원입니다")
else:
    print("입장 인원은 최대 8명입니다")
    

ju = "주상현빡빡이"

while True:
    for i in range(6):
        print(ju[i], end='')
        time.sleep(2/(i+1))
    print("")