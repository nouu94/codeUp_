'''
다음과 같은 n*n 배열 구조를 출력해보자.

입력이 3인 경우 다음과 같이 출력한다.
3 2 1
6 5 4
9 8 7

입력이 5인 경우는 다음과 같이 출력한다.
5 4 3 2 1
10 9 8 7 6
15 14 13 12 11
20 19 18 17 16
25 24 23 22 21

입력이 n인 경우의 2차원 배열을 출력해보자.
'''

""" n = int(input())

cnt = n

for i in range(1, n + 1):
    cnt = n * i

    for j in range(n):
        print(cnt, end=' ')
        cnt -= 1
    print() """

# 이렇게도 됩니다.

n = int(input())
lst_array = [[0] * n for _ in range(n)]  # 리스트 내포 [[0]이 n만큼 채워집니다.] [[0], [0]]
fill = 1

for i in range(len(lst_array)):
    for j in range(len(lst_array[i]) - 1, -1, -1):
        lst_array[i][j] = fill
        fill += 1

for i in lst_array:
    print(*i, ' ')  # unpacking 패킹된 데이터를 다시 언패킹하여 리스트를
