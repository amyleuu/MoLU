import sys
input=sys.stdin.readline
N=int(input())
a,b=map(int,input().split())
M=int(input())
tree=[[] for _ in range (N+1)]
for _ in range (M):
    x,y=map(int,input().split())
    tree[x].append(y)
    tree[y].append(x)

visited=[False]*(N+1)
result=-1

def dfs(v,count):
    global result
    visited[v]=True
    if v==b:
        result=count
        return
    for i in tree[v]:
        if not visited[i]:
            dfs(i,count+1)

dfs(a,0)
print(result)
