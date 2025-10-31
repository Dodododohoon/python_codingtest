# 당장 눈앞에 보이는, 직관적 최선값을 찾는다.

# 11047
# import sys
# input = sys.stdin.readline

# cnt=0
# n,k= map(int, input().split())

# li = [int(input()) for _ in range(n)]
# li.sort(reverse=True)

# for i in range(n):
#    if k==0:
#        break
#    if k // li[i] >0:
#        cnt += k//li[i]
#        k = k%li[i]

# print(cnt)

# 1931
# import sys
# input= sys.stdin.readline

# n= int(input())
# li = [list(map(int, input().split())) for _ in range(n)]


# li.sort(key=lambda x: (x[1], x[0]))

# a=li[0][0]
# b=li[0][1]
# cnt=1

# for i in range(1,n):
#    if li[i][0] >= b:
#        a=li[i][0]
#        b=li[i][1]
#        cnt+=1

# print(cnt)

# 회의시간 끝나는 시간만 보면 된다. 이 아이디어 좀 늦게 확인함.
# 1부터 시작 안해서 처음에 틀림.

# 11399
# import sys
# input= sys.stdin.readline

# n = int(input())

# li = list(map(int, input().split()))
# li.sort()
# k=0
# s =[]

# for x in li:
#    k += x
#    s.append(k)
#
# print(sum(s))

# 아 k +=x, s+=k 하면 s리스트 만들 필요도 없는데 뭘 이렇게 풀었대

# 1541
# import sys

# input = sys.stdin.readline

# li = input().strip()

# num = ""
# number = []
# ops = []

# m = False


# for x in li:
#     if x.isdigit():
#         num += x
#     else:
#         number.append(num)
#         ops.append(x)
#         num = ""
# number.append(num)

# sum = int(number[0])
# for i in range(len(ops)):
#     if ops[i] == "-":
#         m = True
#     if m == True:
#         sum -= int(number[i + 1])
#     else:
#         sum += int(number[i + 1])

# print(sum)

# 일단 풀긴 했음. 근데 gpt 코드 개 간단함.
# expression = input().split('-')

# result = sum(map(int, expression[0].split('+')))
# for part in expression[1:]:
#     result -= sum(map(int, part.split('+')))

# print(result)

# split() 이 특정 기준 문자로 나눠서 리스트로 만들어 주는 거임.

# 13305
import sys

input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
pay = list(map(int, input().split()))

total = 0
min_price = pay[0]

for i in range(n - 1):
    if pay[i] < min_price:
        min_price = pay[i]
    total += dis[i] * min_price

print(total)

# 아이디어 부분에서 조큼 개선 더하니 best 코드.
