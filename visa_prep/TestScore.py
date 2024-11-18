a,b,x = map(int, input().split())
if x%b == 0 and x <= a*x:
    print("YES")
else:
    print("NO")
