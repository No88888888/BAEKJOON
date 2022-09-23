'''
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''
# def nCm():
#     if len(s) == M:
#         comb.add(tuple(s))
#     else:
#         for i in arr:
#             if i in s:
#                 continue
#             else:
#                 s.append(i)
#                 nCm()
#                 s.pop()

# from collections import deque
# N, M = map(int, input().split())
# arr = sorted(list(map(int, input().split())))
# s = []
# comb = set()
# nCm()
# print(comb)



def f(s,t,k):
    global comb
    if s == k:
        h = sorted(p)
        comb.add(tuple(h))
    else:
        for j in range(t):
            if used[j] == 0:
                used[j] = 1
                p[s] = arr[j]
                f(s+1,t,k)
                used[j] = 0

N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
used = [0]*N
p = [0]*M
comb = set()
f(0,N,M)
for i in sorted(list(comb)):
    print(*i)