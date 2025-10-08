# 2750
# n=int(input())
# li=[]
# for i in range(n):
#    li.append(int(input()))
#
# li.sort()
# for i in range(n):
#    print(li[i])

# 입력 받을때 li = [int(input()) for _ in range(n)] 가능
# 출력 for i in li: print(i) 이거도가능

# 2587
# li=[int(input()) for _ in range(5)]
# print(int(sum(li)/5))
# li.sort()
# print(li[2])

# 25305
# n, m  = map(int, input().split())
# li= list(map(int, input().split()))

# li.sort()
# li.reverse()
# print(li[m-1])
# li.sort(reverse=True)하면 한방에 됨.

# 2751
# import sys
# n = int(sys.stdin.readline())
# li = [int(sys.stdin.readline()) for _ in range(n)]

# li.sort()
# for i in li:
#    print(i)
# 본격적으로 stdin 써야하는 문제.
# 추가로 sys.stdout.write('\n'.join(map(str, li)))하면 출력도 더 빨라짐.

# 10989
# import sys

# n=int(sys.stdin.readline().strip())
# li=[0]*10001

# for _ in range(n):
#    k=int(sys.stdin.readline().strip())
#    li[k] +=1

# for i in range(10001):
#    if li[i]!=0:
#        for _ in range(li[i]):
#            print(i)

# 카운팅 정렬. 수 범위가 좀 적을때 유효함.
# N : 데이터 개수, K:값의범위 N>= K 일때 효과적. (K가 100만정도가 거의 마지노선.)
# O(N + K)

# 1427
# n=int(input())
# li=list(map(int,str(n)))
# li.sort(reverse=True)
# print(''.join(map(str, li)))

# 이제좀 join, map에 익숙해 진다.

# 11650
# import sys

# n = int(sys.stdin.readline())
# li=[]
# for i in range(n):
#    li.append(list(map(int, sys.stdin.readline().split())))
# li.sort()

# for i in range(n):
#    print(' '.join(map(str, li[i])))

# 이차원 배열도 sort가 먹을 줄 몰랐는데 실험 해보니깐 되더라 ?!
# append할때 처음에 그냥 readline().split()만 먹여서 한자리일 땐 잘 돌아 갔는데 두자리 되니깐 에러 떴음. why? - str이라서. 10 이 2보다 더 작게 됨.
# 그리고 int로 바꿔주니 clear

# 1651
# import sys

# n = int(sys.stdin.readline())
# li = []
# for i in range(n):
#     x, y = map(int, sys.stdin.readline().split())
#     li.append([y, x])
# li.sort()
# for i in range(n):
#     print(li[i][1], li[i][0])

# 1181 - 중복처리 해야함.
#import sys

#n = int(sys.stdin.readline())
#s = set()
#li = []

#for i in range(n):
#    a = sys.stdin.readline().strip()
#    len_a = len(a)
#    s.add((len_a,a))

#li = list(s)
#li.sort()

#for i in range(len(li)):
#    print(li[i][1])

#막 그렇게 어렵진 않았는데, set, list, tuple, dictionary 이것들 좀 여러가지 써봐야겠다.

# 10814
#import sys

#n = int(sys.stdin.readline())
#li=[]

#for i in range(n):
#    a = sys.stdin.readline().split()
#    li.append([int(a[0]),i,a[1]])

#li.sort()

#for i in range(n):
#    print(li[i][0], li[i][2])

# lambda쓰면 따로 인덱스 안 먹여도 된대 다음엔 람다도 한번 써보자.

# 18870
#import sys

#n = int(sys.stdin.readline())
#li = list(map(int, sys.stdin.readline().split()))

#li_s=list(set(li))
#li_s.sort()

#dic=dict()
#for i in range(len(li_s)):
#    dic[li_s[i]] = i

#for x in li:
#    print(dic[x], end=' ')

#딕셔너리 거의 처음 써본 듯. 적응할 필요 있을 거 같은데.

#sorting : list, set, tuple, dict 잘 가지고 놀줄 알아야 할 거 같다.
#enumerate, join, lambda, 컴프리핸션 등등 빠삭하게 이해 필요하다.