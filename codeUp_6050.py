'''
두 정수(a, b)를 입력받아
b의 값이 a의 값 보다 크거나 같으면 True 를, 같지 않으면 False 를 출력하는 프로그램을 작성해보자.

참고
어떤 값을 비교하기 위해 비교/관계(comparison/relational) 연산자(operator)를 사용할 수 있다.

비교/관계연산자 <= 는
오른쪽의 계산 결과값이 왼쪽의 계산 결과값보다 크거나 같은 경우 True(참)로 계산하고,
그 외의 경우에는 False(거짓)로 계산한다.

<=, >= 연산자는 같음(==)을 포함한다. 따라서 “작다/크다” 거나 "같다”는 의미를 가진다.
작다(<)/크다(>)/다르다(!) 기호는 등호(=)와 함께 왼쪽에 붙여써야 한다.

비교/관계연산자도 일반적인 사칙연산자처럼 주어진 두 수를 이용해 계산을 수행하고,
그 결과를 True(참), 또는 False(거짓)로 계산해주는 연산자이다.
비교/관계연산자는 <, >, <=, >=, ==(같다), !=(다르다) 6개가 있다.

'''

a, b = input().split()

a = int(a)
b = int(b)

print(a <= b)
