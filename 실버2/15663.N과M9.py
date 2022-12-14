'''
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

import sys
input = sys.stdin.readline

# def f(s, t, r):
#     global comb
#     if s == r:
#         comb.add(tuple(p))

#     else:
#         for j in range(t):
#             if used[j] == 0:
#                 used[j] = 1
#                 p[s] = arr[j]
#                 f(s+1, t, r)
#                 used[j] = 0



# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# used = [0]*N
# p = [0]*M
# comb = set()
# f(0,N,M)
# res = []
# for i in comb:
#     res.append(i)
# res.sort()
# for i in res:
#     print(*i)


def nCm():
    if len(s) == M:
        print(*s)
        return

    r = 0
    for i in range(N):
        if used[i] == 0 and r != arr[i]:
            used[i] = 1
            r = arr[i]
            s.append(arr[i])
            nCm()
            s.pop()
            used[i] = 0
        
N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
s = []
used = [0]*(N+1)
nCm()

