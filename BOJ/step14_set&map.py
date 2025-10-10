# 10815
# import sys

# n= int(sys.stdin.readline())
# s=set(map(int, sys.stdin.readline().split()))
# m=int(sys.stdin.readline())
# li=list(map(int, sys.stdin.readline().split()))

# for x in li:
#    if x in s:
#        print('1', end=' ')
#    else:
#        print('0', end=' ')

# print(' '.join(['1' if x in s else '0' for x in li])) 이렇게도 가능. 컴프리핸션

# 14425
# import sys

# n, m = map(int, sys.stdin.readline().split())
# li=[sys.stdin.readline().strip() for _ in range(n)]
# cnt=0

# for i in range(m):
#    word = sys.stdin.readline().strip()
#    if word in li:
#        cnt+=1
#
# print(cnt)

# set이 훨씬 빠름. list는 인덱스 하나하나 검사해야해서 O(N)
# set은 딕셔너리처럼 해시테이블 형식이라 O(1)

# 7785
# import sys
# input = sys.stdin.readline

# n = int(input())
# s=set()

# for i in range(n):
#    a, b = map(str, input().split())
#    if b=='enter':
#        s.add(a)
#    else:
#        s.remove(a)

# li=list(s)
# li.sort(reverse=True)
# print('\n'.join(map(str, li)))

# 처음에 list로 풀었다가 시간초과 뜸. 입력,삭제만 하면 sort도 해야하는 데 굳이 set -> list보다는 걍 list 써야지 했었음.
# 근데 list에서 삭제할때도 시간이 많이듦. 순차 탐색해야하고, 하나씩 앞으로 당겨야 해서.
# but, set은 O(1)
# join문에서 map() 생략가능. 문자열이니께

# 1620
#import sys

#n, m = map(int, sys.stdin.readline().split())
#dic_n = dict()
#dic_k = dict()

#for i in range(1, n + 1):
#    a = sys.stdin.readline().strip()
#    dic_k[i] = a
#    dic_n[a] = i

#for i in range(m):
#    check = sys.stdin.readline().strip()

#    try:
#        if int(check):
#            print(dic_k.get(int(check)))
#    except ValueError:
#        print(dic_n.get(check))

# 10816
#import sys
#input = sys.stdin.readline

#n= int(input())
#li = map(int, input().split())
#dic = dict()

#for x in li:
#    if x in dic:
#        dic[x]+=1
#    else:
#        dic[x]=1

#m=int(input())
#li=map(int, input().split())

#for x in li:
#    if x in dic:
#        print(dic.get(x),end=' ')
#    else:
#        print('0', end=' ')
    
#딕셔너리 입력할때 dic[x] = dic.get(x,0) +1 하면 없으면 디폴트 0 입력후 +1 있으면 값에서 +1 가능. 훨씬 간편
#마찬가지로 출력도. print(' '.join(str(dic.get(x,0))) for x in li)

# 1764
#import sys
#input  = sys.stdin.readline

#n,m = map(int, input().split())
#dic = {}

#for i in range(n+m):
#    a = input().strip()
#    dic[a]=dic.get(a, 0) +1

#cnt=0
#li=[]
#for x in dic:
#    if dic[x]==2:
#        cnt+=1
#        li.append(x)

#li.sort()
#print(cnt)
#print('\n'.join(li))

#set 교집합(&)으로도 풀린다.

# 1269
#import sys
#input  = sys.stdin.readline

#n, m = map(int, input().split())
#a = set(map(int,input().split()))
#b = set(map(int, input().split()))
#c = a^b

#print(len(c))

# 11478
#word = input()
#n = len(word)
#s=set()

#for i in range(0, n):
#    for j in range(n-i):
#        s.add(word[j:j+i+1])

#print(len(s))