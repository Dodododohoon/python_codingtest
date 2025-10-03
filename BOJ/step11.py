#24262
#n = int(input())
#print('1')
#print('0')

#24263

#24264
#n=int(input())
#print(n**2)
#print('2')

#24265
#n=int(input())
#print(int((n*(n-1))/2))
#print('2')

#24266
#n=int(input())
#print(n**3)
#print(3)

#24267
#n = int(input())
#print(n*(n-1)*(n-2)//6)
#print(3)

#24313
a1, a2 = map(int, input().split())
c = int(input())
n0 = int(input())

if a1 > c:
    print(0)
elif a1 == c:
    print(1 if a2 <= 0 else 0)
else:  # a1 < c
    print(1 if a1*n0 + a2 <= c*n0 else 0)
