# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 11:48:40 2020

@author: K.Lee Home
"""

''' 사칙연산 '''
a = 15
b = 4
print(a + b, a - b, a * b, a / b)


A, B = 745, 20

몫 = A // B
나머지 = A % B

print(몫, 나머지)
print('---------------')

# 제곱연산

print(2 ** 10)

''' 비교연산 '''
print(1<2)
print(2<1)
print( 20 != 20 )
print( 17 < (118 %100) )
print('---------------')

# 문자열 연결(덧셈)
s = "Hello" + ", World"
print(s)

s = "Hello"
s += ", World"
print(s)
print('---------------')

# 문자열 반복 생성 (곱셈)

hline = '*' * 100
print(hline)

print('--*--' * 20)

# in: 문자열에 문자열 포함여부 테스트하는 연산자

print('파이썬' in '인생은 짧아요, 파이썬 쓰세요')
print('파이선' in '인생은 짧아요, 파이썬 쓰세요')

print('---------------')

s = "Hello, Python!"

# 인덱싱
print(s[0]) # 첫번째 문자
print(s[4]) # 5번째 문자

# 슬라이싱
print(s[:]) # 처음 부터 끝까지
print(s[0:5]) # 처음 부터 인덱스 4까지
print(s[7:9]) # 인덱스 7부터, 인덱스 8까지
print(s[-1]) # 마지막 문자
print(s[-5:-1]) # 마지막에서 5번째 부터 마지막 문자 직전까지


print('---------------')

# 문자열 분리(split)

s = "화학,출판,전기제품,제약,은행"
print(s.split(','))



# 문자열 합치기 (join)

sectors = ['화학', '출판', '전기제품', '제약', '은행']
print("|".join(sectors))
print("a".join(sectors))
print("aa".join(sectors))



# 문자열 대체 (replace)
s = "Hello, Python!"
w = s.replace('Python', 'World')
print(w)

s = '1,222,333원'
price = int(s.replace(',', '').replace('원', ''))
print(price)
price_split = s.split(',')
print(price_split)
price_split2 = "|".join(price_split)
price_split3 = price_split2.replace('|','a')
