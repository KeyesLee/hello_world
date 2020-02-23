# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""





print("Hello world")
print(" ")
print("Hello world")

text = """ 안녕하세요 """
print(text)

text2 = ''' 반갑습니다 '''
print(text2)



print(text2,end='\n\n\n')
print(text2)

multi_line_text = """
이렇게 \n
사용해도
될까?
"""
print(multi_line_text)

"""
이런식으로 문자열만 배열하면
주석으로 처리된다.
변수에 넣거나 하지 않았기 때문이다...
"""

int_val = 10
float_val = 10.5
neg_float_val = -1100
neg_int_val = -100000

print(int_val, float_val, neg_float_val, neg_int_val)


a = 1e5
b = 1e-5
c = 1
d = 1.0
e = -5
f = 'abcde'
g = True

"자기가 알아서 데이터 타입이 정해진다."
"True 대소문자 주의"

print( type(a) )
print( type(c) )
print( type(f) )

"""type 을 확인하는 함수는 print 에서만 사용 가능할 듯
변수에 그 결과를 입력하거나 하는 방법으로는 사용이 안됨"""

h = '1.8'
i = '2'
conv_h = float(h)
conv_i = int(i)
print(type(conv_h), h)
print(type(conv_i), i)
print(type(int(conv_h)), int(conv_h))
print(type(int(conv_h)), int(round(conv_h)))


""" str 형으로 정의된 숫자도 float() 등으로 숫자로 변환 된다.
하지만 str 안에 들어가 있는 형태가 변환할 타입과 맞아야 한다.
가령 1.1 은 float로만,  1,2,3 혹은 1.0,2.0... 은 int 로만 변환이 가능하다.
그리고 float 를 int 로 변환하면 소숫점 아래는 버림한다.
반올림 하고 싶으면 round() 사용한다."""

import keyword
print(len(keyword.kwlist))
print(keyword.kwlist,end='\n\n')

"""미리 정해진 키워드가 총 35개가 있고, 이 이름들은 변수로 사용하지 말자"""

종목코드 = '005930'
종목명 = '삼성전자'
상장주식수 = 5969782550
PER = 8.61
PBR = 1.53
상장여부 = True

print(종목코드, 종목명, 상장주식수, PER, PBR, 상장여부)

""" 무려 한글을 변수로 사용 가능하다....!! """



print("Hello, python")
print("Hello, python", 3.14, 1.41e-10)
print(1024 ** 64)
print(2 == 1)


""" f-string 포맷팅 """
""" 변수에 값을 할당 """
a, b, c = 3.1415, 2.8, 0.015

""" 순서대로 할당 """
print(f"x = {a:.2f}, y = {b}, z = {c}")

" {}안에서 변수 연산도 가능 "
print(f"x = {a}, w = {b + c}")

for x in range(1, 200, 20):
    print(f"{x:5d} | {x**2 :5} | {x/x**2 :.4f}")
    