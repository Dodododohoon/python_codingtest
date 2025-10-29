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
import sys

input = sys.stdin.readline

li = input().strip()


# 13305
