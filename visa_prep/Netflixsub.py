K,A,V,S = map(int, input().split())
if(K+A>=S) or (K+V>=S) or (A+V>=S):
    print("YES")
else:
    print("NO")
