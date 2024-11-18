A, R, S = map(int, input().split())
if A > S:
    print(0)
elif A + R <= S:
    print(2)
else:
    print(1)
