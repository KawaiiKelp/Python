# 입출력문 연습

""" 
print("Hello World!")

print("\n-------------\n")



message = "케르프"
hi = "안녕하세요 저는 켈프입니다.
저는 태어났을때부터 세계를 일주하는 힘을 가지고 있었으며,
현재는 100m 달리기를 0.0001초만에 완주할 수 있는 정도의 힘을 지니고 있습니다"
print(message)



print("\n-------------\n")

print("\nGoodbye World.") 

# 변수 만들기 - 자료형의 이해

a = 4 # 정수형
b = 2.5 # 실수형
c = "Hello" # 문자열
d = True # 논리형

print("a 변수에 들어있는 값은", a, "입니다")
print(type(a))
print(type(b))
print(type(c))
print(type(d))


name = input("이름을 입력하세요: ") # 키보드로부터 입력
print("입력하신 이름은", name, "입니다")
age = input("나이를 입력하세요: ")
print("나이는", age, "살입니다")

# 이름과 나이를 입력받고 결과
# 제 이름은 OOO이고 나이는 nn살입니다
print("이름은", name, "이고 나이는", age, "살입니다")
"""

# 두 수의 덧셈(키보드로부터 수를 입력받기)
a = int(input("첫 번째 수 입력: "))
b = int(input("두 번째 수 입력: "))
c = a+b
print("계산 결과:", c)
print(type(a))