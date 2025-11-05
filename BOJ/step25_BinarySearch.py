    #1920
    import sys
    input = sys.stdin.readline
    
    n = int(input())
    li_n = list(map(int, input().split()))
    m = int(input())
    li_m = list(map(int, input().split()))
    
    li_n.sort()
    
    def search(k,left,right):
        mid = (left + right)//2
        
        if k == li_n[mid]:
            return '1'
        if d == 0:
            return '0'   
        
        if k < li_n[mid]:
            return search(k, left, mid)
        else:
            return search(k, mid, right)
    
    for x in li_m:
        print(search(x,0,len(li_n)))
    
#10816


#1654


#2805


#2110


#1300


#12015