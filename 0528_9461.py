T=int(input())
N=[int(input())for _ in range(T)]
maxn=max(N)
dp=[0]*(maxn+1)
dp[1]=dp[2]=dp[3]=1
for i in range(4,maxn+1):
    dp[i]=dp[i-2]+dp[i-3]
for i in range(T):
    print(dp[N[i]])
