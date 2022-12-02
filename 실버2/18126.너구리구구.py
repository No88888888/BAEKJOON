'''
문제
텔레토비 동산에 사는 너구리 구구는 입구, 거실, 주방, 안방, 공부방, 운동실, 음악실, 음식 창고 등 N개의 방을 가지고 있다. 입구를 포함한 모든 방은 1부터 N까지의 번호가 있고, 입구는 1번이다.  구구의 집으로 들어가는 입구는 한 개이며 입구과 모든 방들은 총 N-1개의 길로 서로 오고 갈 수 있다.

구구는 스머프 동산에서 멜론아 아이스크림을 발견했다. 구구는 무더운 여름 햇살을 피해 최대한 입구에서 먼 방에 아이스크림을 숨기려고 한다.

구구가 집 입구에서 멜론아 아이스크림을 숨기려고 하는 방까지 이동하는 거리를 구하여라.

입력
첫째 줄에 정수 N(1 ≤ N ≤ 5,000)이 주어진다.

다음 N-1개의 줄에 구구의 집의 모든 길의 정보가 정수 A, B, C(1 ≤ A, B ≤ N, 1 ≤ C ≤ 1,000,000,000)로 주어진다.

A번 방과 B번 방 사이를 양방향으로 연결하는 길의 길이가 C임을 의미한다.

출력
구구가 집 입구에서 멜론아 아이스크림을 숨기려고 하는 방까지 이동하는 거리를 구하여라.
'''

# def dfs(po):
#     global dist
#     global visited
#     global stack
#     global res
#     if po == N:
#         res = dist
#         return
#     a =  stack.pop()
#     for w in gugu[a]:
#         if visited[w[0]]:
#             continue
#         dist += w[1]
#         stack.append(w[0])
#         visited[w[0]] = 1
#         po = w[0]
#         dfs(po)
#         dist -= w[1]

# N = int(input())
# gugu = [[] for _ in range(N+1)]
# for _ in range(N-1):
#     a, b, c = map(int, input().split())
#     gugu[a].append((b,c))
# dist = 0
# res = 0
# stack = [1]
# visited = [0] * (N+1)
# visited[1] = 1
# dfs(1)
# print(res)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(po):
    visited[po] = 1
    for i in gugu[po]:
        w = i[0]
        if not visited[w]:
            dist[w] = i[1] + dist[po]
            dfs(w)

N = int(input())
gugu = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, c = map(int, input().split())
    gugu[a].append([b, c])
    gugu[b].append([a, c])

visited = [0] * (N+1)
dist = [0] * (N+1)
dfs(1)
print(max(dist))