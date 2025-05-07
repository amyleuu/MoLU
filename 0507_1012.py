import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)
T=int(input())

def dfs(x,y):
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if (0<=nx<M) and (0<=ny<N) and field[ny][nx]==1:
            field[ny][nx]=0
            dfs(nx,ny)



for _ in range(T):
    M,N,K=map(int,input().split())
    
    field=[[0 for _ in range (M)] for _ in range(N)]
            
    for _ in range(K):
        x,y=map(int,input().split())
        field[y][x]=1

    count=0
    for x in range(M):
        for y in range(N):
            if field[y][x]==1:
                field[y][x]=0
                dfs(x,y)
                count+=1

    print(count)
