#2745
import sys

li = sys.stdin.readline().split()
num=[]
result =0

for ch in li[0]:
    if ch.isdigit():
        num.append(int(ch))
    else:
        num.append(ord(ch)-55)

trans = num[::-1]

for i in range (len(trans)):
    result += trans[i] * (int(li[1])**i)
print(result)

#11005


#2720


#2903


#2292


#1193


#2869

