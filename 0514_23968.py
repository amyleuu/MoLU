import sys
input=sys.stdin.readline
N,K=map(int,input().split())
A=list(map(int,input().split()))
count=0
ans=-1
def bubble_sort(arr):
    global count,ans
    for i in range(len(arr)-1,0,-1):
        for j in range (i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count+=1
                if count==K:
                    ans=(arr[j],arr[j+1])
                    return

bubble_sort (A)
if ans==-1:
    print(-1)
else:
    print(*ans)
