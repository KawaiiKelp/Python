""" # 제어문 연습 (중첩 if문) - 놀이동산 요금계산
# 주간, 야간, 대인, 소인 요금 구분하기

k = int(input("구분: 1. 주간 2. 야간?"))
m = int(input("대상: 1. 대인 2. 소인?"))


if k == 1:
    if m == 1:
        pay = 50000
    else:
        pay = 40000
else:
    if m == 1:
        pay = 30000
    else:
        pay = 20000
print(f"당신의 입장료는 {pay}원입니다")
# for 반복문
# 3. 리스트 변수를 이용한 반복문

fruit = ['apple', 'grape', 'orange', 'banana']
print(fruit[2])

count = 0

match fruit:
    case ['apple']:
        print("사과입니다")
    case ['grape']:
        print("포도입니다")
    case ['orange']:
        print("맛있겠다")
    case ['banana']:
        print("바나나입니다")
    case _:
        print("니얼굴")
    
for f in fruit: # 리스트 변수의 개수만큼 반복
    print(f)
    count += 1
    print(count)
print(fruit)

# 튜플 변수를 이용한 반복
food = ("치킨", "피자", "햄버거", "보쌈", "고추장찌개")
print(type(food))

for f in food:
    print(f)

# 리스트 변수 안에 있는 정수 값이 홀수인지 짝수인지 판별하는 코드 작성

# OO는 짝수입니다 or OO는 홀수입니다

num = [273, 32, 103, 57, 52, 241, 21421, 21, 51, 91, 72]
for n in num:
    if n % 2 == 0:
        print(f"{n}는 짝수입니다")
    else:
        print(f"{n}는 홀수입니다")

# 자릿수 273은 3자리수입니다

for n in num:
    print("{}는 {}자리수입니다".format(n, len(str(n))))

"""

""" # 5명의 정보처리기능사 자격증 필기 점수가 리스트에 담겨있습니다.
# 이때 각 점수가 합격 점수인지 불합격 점수인지 판별하여 출력하시오. (60점 이상 합격)

score_list = [98, 58, 65, 78, 44]
sum_score = 0

student = 1
for score in score_list:
    sum_score += score
    if score >= 60:
        print(f"{student}번 학생은 {score}점으로 합격입니다")
    else:
        print(f"{student}번 학생은 {score}점으로 불합격입니다")
    student += 1

print(f"총점은 {sum_score}입니다")
print(sum(score_list))
 """

# range() 함수를 이용한 반복
# 1 ~ 10까지의 합을 구하기

합 = 0
곱 = 1
for n in range(1, 11):
    합 += n
    곱 *= n
print(f"1~10까지의 합은", 합, "입니다")
print(f"1~10까지의 곱은", 곱, "입니다")

import random as 랜덤
난수 = 랜덤.randint(1, 100)
이 = 2
영 = 0

def 출력(값):
    print(값)

def 반환(값):
    return 값

if 난수 % 이 == 영:
    출력("짝수")
else:
    출력("홀수")

if 난수 % 이 == 영:
    출력("짝수")
    반환(난수)
else:
    출력("홀수")
    반환(난수)
