'''
6자리의 연월일(YYMMDD)을 입력받아 나누어 출력해보자.

참고
s = input()
print(s[0:2])

를 실행하면 0번째 문자부터 1번째 문자까지 잘라 출력한다.
s[a:b] 라고 하면, s라는 단어에서 a번째 문자부터 b-1번째 
문자까지 잘라낸 부분을 의미한다.

다른 자르기 방법도 있다.
'''

# 년도(YY) 월(MM) 일(DD)을 공백으로 구분해 한 줄로 출력합니다.
s = input()
print(s[0:2], end=' ')
print(s[2:4], end=' ')
print(s[4:6], end=' ')