'''
정수(0 ~ 100) 1개를 입력받아 0부터 그 수까지 순서대로 출력해보자.
'''
start_num = 0
n = int(input())

while start_num != n:
    print(start_num, end='\n')
    start_num += 1


if start_num == n:
    print(start_num)
