N=int(input())
stack=[]


import sys
input=sys.stdin.readline

for _ in range(N):
    command=input().strip().split() #strip(): 'push 3\n'라고 입력되기 때문
    
    if command[0]=='push':
        stack.append(int(command[1]))
        
    elif command[0]=='pop':
        print(stack.pop() if stack else -1) #if stack: 'stack이 비어있지 않다.'            
    elif command[0]=='size':
        print(len(stack))
        
    elif command[0]=='empty':
        print(0 if stack else 1) # x if 조건 else y 조건이 참이면 x, 아니면 y
            
    elif command[0]=='top':
        print(stack[-1] if stack else -1) #스택은 LIFO
