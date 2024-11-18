w = int(input())
for _ in range(0,w):
    s,r=map(int,(input().split()))
    if s>r:
        print(s-r)
    else:
        print(0)
