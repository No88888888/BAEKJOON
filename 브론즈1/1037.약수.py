N = int(input())
div = sorted(list(map(int, input().split())))
if len(div) == 1:
    print(div[0]**2)
else:
    print(div[0]*div[-1])
