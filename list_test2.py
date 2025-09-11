""" # 리스트 변수 인덱싱
# 여러개의 값 저장, 값을 변경, []
# append() insert() remove() pop()

food = ["햄버거", "탕수육", "피자", "간장게장", "만두", "초밥"]
print(food)
food.append("나폴리탄")
print(food)
food.insert(3, "몽블랑")
print(food)
food.remove("피자")
print(food)
food.pop(5)
print(food)
food.sort()
print(food)
food.reverse()
print(food)
food.clear()
print(food)
 """

# 문자열변수 인덱싱
name_list = ["박명수", "유재석", "하하", "응애", "까까", "12"]
print(name_list)
# ['박명수', '유재석', '하하', '응애', '까까', '12']
print(name_list[4])
# 까까
name_list[2] = "조리퐁"
print(name_list)
# ['박명수', '유재석', '조리퐁', '응애', '까까', '12']
print(name_list[0:4])
# ['박명수', '유재석', '조리퐁', '응애']
print(name_list[1:4])
# ['유재석', '조리퐁', '응애']
print(name_list[4:6])
# ['까까', '12']
print(name_list[::2])
print(name_list[3:])
print(name_list[:3])

print(name_list[:-2])

# 포함 in 미포함 not in
print(name_list[:-2])
print(len(name_list))
print("까까" in name_list)
print("양파깡" not in name_list)
print("12" not in name_list)
print("새우깡" in name_list)

i = [5, 4, 6, 3]
print(9 in i)
print(3 not in i)