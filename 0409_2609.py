a, b = map(int, input().split())
x, y = (b, a) if a < b else (a, b)

cd = []
for i in range(1, y + 1):
    if a % i == 0 and b % i == 0:
        cd.append(i)

G = max(cd)
L = (a * b) // G

print(G, L)
