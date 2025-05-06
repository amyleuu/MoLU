import sys
input=sys.stdin.readline

N,M,V=map(int,input().split())
GRAPH=[[] for _ in range(N+1)]

for _ in range (M):
    a,b=map(int,input().split())
    GRAPH[a].append(b)
    GRAPH[b].append(a)
 
for g in GRAPH:
    g.sort()

def dfs(graph,v,visited):
    visited[v]=True
    print(v,end=' ')
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph,neighbor,visited)
visited=[False]*(N+1)
dfs(GRAPH,V,visited)
print()
visited=[False]*(N+1)

from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()
        print(v, end=' ')

        for neighbor in graph[v]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor]=True
bfs(GRAPH,V,visited)
