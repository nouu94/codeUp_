# 리스트에 값을 하나씩 더해서 새로운 리스트를 만드는 작업
myList = [1, 2, 3, 4, 5]
result1 = []

# for 반복문을 이용한다.
for val in myList:
    result1.append(val + 1)

print(f'result1 : {result1}')


# map 함수를 이용한다.

def add_one(n):
    return n + 1


myList2 = [5, 6, 7, 8]

result2 = list(map(add_one, myList2))  # map 반환을 list로 변환
print(f'result2 : {result2}')
