""" # 입출력 함수 print() input()
# 변수 변수 규칙 예약어
# 자료형
# 연산자 산술 비교(관계) 논리 대입
# 문자열함수 upper() lower() title() len()
# 이스케이프코드 \

# 리스트 변수


h = ['lee', 17, 172.5, True]
i = []
print(type(h))
print(type(i))
c = h[1] + h[2]
print(type(c))

singer = ["MEIKO", "KAITO", "하츠네 미쿠", "카가미네 린", "카가미네 렌", "메구리네 루카"]
print(singer)
# append() 값 추가
singer.append("카사네 테토")
print(singer)

#remove() 값 삭제
singer.remove("KAITO")
print(singer)
singer.remove("카가미네 린")
print(singer)
singer.append("메구포이드")
print(singer)

# ['MEIKO', '하츠네 미쿠', '카가미네 렌', '메구리네 루카', '카사네 테토', '메구포이드']

# insert() 값 삽입 원하는 위치에
singer.insert(2, "카후")
print(singer)

# pop() 원하는 위치의 값 삭제
singer.pop(4)

singer.pop(1)
singer.pop(2)
print(singer)
singer.clear() # 모두 지우기
print(singer)

singer.insert(2, "카후")
print(singer)
print(singer[0])

fruit = ["사과", "참외", "수박", "레몬", "오렌지"]

print(type(fruit))
fruit.append("두리안")
fruit.remove("레몬")
fruit.pop(3)
fruit.insert(2, "포도")
print(fruit)

# sort()
fruit.sort()
print(fruit)

score = [90.2, 78.6, 89.5, 67.8, 60.2, 99.5, 53.2]

score.sort(reverse=True)
print(score)
"""
import random
import time

# random() 함수
x = random.random() # 0 이상 1 미만의 난수 생성
print(x)

x = [1,2,3,4,5,6,7,8]
random.shuffle(x) # 마구 뒤섞기
print(x)

y = random.choice(x) # 하나 선택
z = random.sample(x,3) # 정해진 개수만큼 뽑기
print(z)