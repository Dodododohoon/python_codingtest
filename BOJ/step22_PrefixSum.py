#배열의 특정 구간 i~j의 합을 빠르게 구하는 문제.
#매번 sum()으로 더하면 시간초과 나므로,
#누적합(prefix sum) 으로 미리 더해두고 한 번에 처리!

#11659
#import sys
#input=sys.stdin.readline

#n,m = map(int, input().split())

#li = list(map(int, input().split()))

#prefix = [0] * (n+1)
#prefix_sum=0
#for i in range(1,n+1):
#    prefix[i] = prefix[i-1] +li[i-1]

#for _ in range(m):
#    i, j = map(int, input().split())
#    prefix_sum = prefix[j] - prefix[i-1]
#    print(prefix_sum)

#2559
#import sys
#input = sys.stdin.readline

#n, k = map(int, input().split())

#li = list(map(int, input().split()))
#prefix = [0]*(n+1)

#for i in range(1,n+1):
#    prefix[i] = prefix[i-1] + li[i-1]

#prefix_sum = [0] * (n+1)

#for i in range(k,n+1):
#    prefix_sum[i] = prefix[i]-prefix[i-k]

#print(max(prefix_sum[k:])) 
#print(max(prefix[i] - prefix[i - k] for i in range(k, n + 1)))


#초기값 =0 이라서 최대가 음수인 경우에 틀렸다고 하더라.
#출력방법 2가지. but 2번째 방식 꽤 신박하네
#제네레이터 표현식이라고 하네. 적응하면 꽤나 유용할 거 같은데 일단 keep

#16139


#10986


#11660


#25682


