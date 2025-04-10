N,M=map(int,input().split())
cards=list(map(int,input().split()))
list=[]
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            ans=cards[i]+cards[j]+cards[k]
            if ans>M:
                continue
            else:
                list.append(ans)

print(max(list))
