""" 
# 복습
# 이스케이프 코드
food = "Python\'s favorite food is perl"
say = "\"Python is very easy\" he says."

print(food)
print(say)

# upper() lower() title()

print(food.upper())
print(say.lower())
print(say.title())
# calculator 만들기

num1 = int(input("첫 번째 숫자를 입력하세요: "))
num2 = int(input("두 번째 숫자를 입력하세요: "))

add_result = num1 + num2
sub_result = num1 - num2
mul_result = num1 * num2
div_result = num1 / num2

print(f"덧셈 결과: {add_result}")
print(f"뺄셈 결과: {sub_result}")
print(f"곱셈 결과: {mul_result}")
print(f"나눗셈 결과: {round(div_result, 2)}")

# round 반올림
pi = 3.1415926535
print(round(pi, 2))
print(round(pi))
print(round(pi, 5)) 
"""
import keyword
import datetime
import calendar

# 달력보기
print(calendar.month(2009, 10))

print(keyword.kwlist)

today = datetime.date.today()
print(today.year)
print(today.month)
print(today.day)
print(today.weekday()) # 월요일 0 일요일 6

print(f"오늘은 {today.year}년 {today.month}월 {today.day}일 입니다.")

now = datetime.datetime.now()
print(f"지금은 {now.hour}시 {now.minute}분 {now.second}초 입니다.")
