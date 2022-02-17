'''
다음과 같은 n*n 배열 구조를 출력해보자.

입력이 3인 경우 다음과 같이 출력한다.
1 2 3
4 5 6
7 8 9

입력이 5인 경우는 다음과 같이 출력한다.
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25

입력이 n인 경우의 2차원 배열을 출력해보자.
'''

'''
입력
첫 번째 줄에 배열의 크기 n이 입력된다.
[입력값의 정의역]
1<= n <= 100
'''

'''
출력
n*n 크기의 배열을 설명과 같이 채워 출력한다.
'''
# n 입력 선언
n = int(input())
count = 1

# device and conqual
for i in range(n):
    for j in range(n):
        print(count, end=' ')
        count += 1
    print()

# 아! 카운터라는 변수를 만들고, nested for문 안에 카운터를 넣어서
#  카운터를 1 씩 더해서 출력하게 만드는구나
'''
n = int(input())
 
cnt = 1
for i in range(n):
    for j in range(n):
        print(cnt, end=' ')
        cnt += 1
    print()
'''
