k=int(input())
num = 1
for i in range(1,k+1):
    for j in range(i):
        print(num,end=" ")
        num += 1
    print()
