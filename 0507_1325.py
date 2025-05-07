import sys
from collections import deque

input=sys.stdin.readline

N,M=map(int,input().split())
trust=[[] for _ in range(N+1)]

for _ in range (M):
    a,b=map(int,input().split())
    trust[b].append(a)


def bfs(start):
    queue=deque([start])
    visited=set()
    visited.add(start)
    count=1
    while queue:
        v=queue.popleft()

        for neighbor in trust[v]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                count+=1
    return count


maxCount=0
result=[]
for start in range(1,N+1):
    num=bfs(start)
    if num>maxCount:
        maxCount=num
        result=[start]
    elif num==maxCount:
            result.append(start)

print(' '.join(map(str, result)))
