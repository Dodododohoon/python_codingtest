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
import sys

n, m = map(int, sys.stdin.readline().split())
dic_n = dict()
dic_k = dict()

for i in range(1, n + 1):
    a = sys.stdin.readline().strip()
    dic_k[i] = a
    dic_n[a] = i

for i in range(m):
    check = sys.stdin.readline().strip()

    try:
        if int(check):
            print(dic_k.get(int(check)))
    except ValueError:
        print(dic_n.get(check))


# 10816


# 1764


# 1269


# 11478
