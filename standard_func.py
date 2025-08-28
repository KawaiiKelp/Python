# 표준 함수
name = "케르프"
age = 17

# 여러 줄의 문자 입력: '''
profile = '''
1. 성명: 케르프
2. 소속: KECD
3. 취미: 코딩, 게임
4. 특기: 공중제비 연속 80바퀴
'''

# print 포매팅

print("내 📛이름📛은: ✨", name, "✨")
print("내 🎂나이🎂는: ✨", str(age), "세✨")

print("📛이름📛: ✨%s✨, 🎂나이🎂: ✨%d✨ 1"%(name, age))
print("📛이름📛: ✨{}✨, 🎂나이🎂: ✨{}✨ 2".format(name, age))
print(f"📛이름📛: ✨{name}✨, 🎂나이🎂: ✨{age}✨ 3")

# len() - 문자열의 길이를 구함, 공백 포함

profile = '''
1. 성명: 케르프
2. 소속: KECD
3. 취미: 코딩, 게임
4. 특기: 공중제비 연속 80바퀴'''

name = "케 르 프"

print(len(profile))
print(len(name))
#max() - 제일 큰 값, min() - 제일 작은 값
a = '1234'
print(max(a))
numbers = [1, 5 -2, 0, 6]
print("가장 큰 값은", max(numbers),"입니다")
print("가장 작은 값은", min(numbers),"입니다")
# sum() - 합계 구하기
print("합계는", sum(numbers),"입니다")
# avg() - 평균 구하기
print("평균은", sum(numbers)/len(numbers),"입니다")

# 제곱 구하기 pow()
print("2의 3승은", pow(2, 3)) # (2**3)

# 알파벳을 대문자나 소문자로 변경
a = "I Love You❤️"
b = "enjoy"
print(a.upper())
print(a.lower())

# join() - 구분자 넣기
s1 = ['Hello', 'Python', '!']
s2 = "_".join(s1)

print(s2)