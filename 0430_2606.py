N=int(input())
M=int(input())

link=[]
for _ in range(M):
    a,b=map(int, input().split())
    link.append((a,b))

virus=set([1])
infected=True

while infected:
    infected=False
    for a,b in link:
        if a in virus and b not in virus:
            virus.add(b)
            infected=True
        elif b in virus and a not in virus:
            virus.add(a)
            infected=True

print(len(virus)-1)
