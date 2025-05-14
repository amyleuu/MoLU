import sys
input=sys.stdin.readline
A,P= map(int,input().split())
seq=[A]

while True:
    N=seq[-1]
    num=sum([int(c)**P for c in str(N)])
    if num in seq:
        break
    seq.append(num)

print(seq.index(num))
