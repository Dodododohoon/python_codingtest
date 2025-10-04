# 2798
# n, m = map(int, input().split())
# li= list(map(int,input().split()))
# s = set()

# for i in range(n):
#    for j in range(i+1,n):
#        for k in range(j+1,n):
#            if li[i] + li[j] + li[k] == m:
#                s.add(li[i] + li[j] + li[k])
#                break
#            if li[i] + li[j] + li[k] <= m:
#                s.add(li[i] + li[j] + li[k])
#        if li[i] + li[j] + li[k] == m:
#            break
#    if li[i] + li[j] + li[k] == m:
#        break
# print(max(s))

# max를 구하는 문제다 보니 굳이 set을 쓸필요가 없었다. + break를 넣는게 조금 이라도 더 횟수를 줄일 수 있을 거라고 생각 했는데 별 차이 안난다고 하네. 게다가 더 실수가 날 수 있다고 하지마래

# 2231
# n = int(input())
# tmp =n
# k = 0
# num=0

# while tmp !=0:
#     tmp//=10
#     k+=1

# for i in range(max(1,n-9*k), n):
#      digit = list(map(int, str(i)))
#      m=i

#      if m + sum(digit) == n:
#          num=m
#          break

# print(num)

# 처음에는 자리수 10 나머지로 하나하나 뽑아주다가 메모리,시간에러 떠서 digit방식 찾아서 바로 list로 뽑아서 풀었는데, valueError 떠서 빡쳐서 gpt 물어보니 n=10같은 경우에 시작점이 음수여서 list(map(int, str(i))) 여기서 에러가 뜸. 그래서 max(1, )해서 최소 시작점을 1로 만듦.

# 19532
a, b, c, d, e, f = map(int, input().split())
ans = (e * c - f * b) / (a * e - d * b)


for x in range(-999, 1000):
    if x == ans:
        y = (a * f - c * d) / (a * e - b * d)
        print(x, int(y))

# y=(c-ax)/b 이걸로 구하니깐 ZeroError 떠서 걍 아에 깔끔하게 바꾸니깐 돌아간다. 귀찮더라도 저게 맞는 듯.

# 1018


# 1436


# 2839
