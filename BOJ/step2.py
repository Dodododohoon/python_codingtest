#1330
"""a, b = map(int, input().split())

if(a>b):
    print('>')
if(a==b):
    print("==")
if(a<b):
    print("<") 
"""

"""
#9498
score = int(input())
if(score >= 90):
    print('A')
elif(80 <= score <= 89):
    print('B')
elif(70<= score and score <= 79):
    print("C")
elif(60<= score <= 69):
    print("D")
else:
    print("F")
    

#2753
year = int(input())
if(year % 4 == 0):
    if(year % 100 != 0 or year % 400 == 0):
        print('1')
    else:
        print('0')
else:
    print('0')
"""
"""
#14681
x= int(input())
y= int(input())

if(x>0 and y>0):
    print('1')
if(x<0 and y>0):
    print('2')
if(x<0 and y<0):
    print('3')
if(x>0 and y<0):
    print('4')
"""    
"""
#2884
h, m = map(int, input().split())

if(m<45):
    if (h==0):
        h=24
    h=h-1
    m=m+60-45
    print(h, m)
else:
    m=m-45
    print(h, m)
"""
"""
#2480 
a = list(map(int, input().split()))
a.sort()
b=a[0]
c=a[1]
d=a[2]
price = 0

if(b==d):
    price = 10000 + b*1000
    print(price)
elif(b==c or c==d):
    price = 1000 + c*100
    print(price)
else:
    price = d
    print(price*100)
어쩌다보니 f-string 알게됐다. 문제에선 필요없지만
print(f"{price*100}원") 이렇게 사용가능.
근데 max라는 함수가 있네? max(b,c,d) 이렇게 쓰면 최대값 나오나보다.
""" 
