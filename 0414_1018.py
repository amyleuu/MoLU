M, N = map(int, input().split())
chessboard = [list(input().strip()) for _ in range(M)]

counts=[]
for i in range(M-7):
    for j in range(N-7):
        k=chessboard[i][j]
        count=0
        for a in range(8):
            for b in range(8):
                    now=chessboard[i+a][j+b]
                    n=0 if now==k else 1
                    if (n+a+b)%2!=0:
                        count+=1
        counts.append(min(count,64-count))

print(min(counts))
