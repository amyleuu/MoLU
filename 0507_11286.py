import sys
import heapq

input=sys.stdin.readline

n=int(input())
q=[]

for i in range(n):
    a=int(input().strip())
    if a!=0:
        heapq.heappush(q,(abs(a),a))
    else:
        if not q:
            print(0)
        else:
            print(heapq.heappop(q)[1])
