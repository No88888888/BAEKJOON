'''
문제
백준시의 시장 최백준은 지난 몇 년간 게리맨더링을 통해서 자신의 당에게 유리하게 선거구를 획정했다. 견제할 권력이 없어진 최백준은 권력을 매우 부당하게 행사했고, 심지어는 시의 이름도 백준시로 변경했다. 이번 선거에서는 최대한 공평하게 선거구를 획정하려고 한다.

백준시는 N개의 구역으로 나누어져 있고, 구역은 1번부터 N번까지 번호가 매겨져 있다. 구역을 두 개의 선거구로 나눠야 하고, 각 구역은 두 선거구 중 하나에 포함되어야 한다. 선거구는 구역을 적어도 하나 포함해야 하고, 한 선거구에 포함되어 있는 구역은 모두 연결되어 있어야 한다. 구역 A에서 인접한 구역을 통해서 구역 B로 갈 수 있을 때, 두 구역은 연결되어 있다고 한다. 중간에 통하는 인접한 구역은 0개 이상이어야 하고, 모두 같은 선거구에 포함된 구역이어야 한다.

아래 그림은 6개의 구역이 있는 것이고, 인접한 구역은 선으로 연결되어 있다.



아래는 백준시를 두 선거구로 나눈 4가지 방법이며, 가능한 방법과 불가능한 방법에 대한 예시이다.

			
가능한 방법

[1, 3, 4]와 [2, 5, 6]으로 나누어져 있다.

가능한 방법

[1, 2, 3, 4, 6]과 [5]로 나누어져 있다.

불가능한 방법

[1, 2, 3, 4]와 [5, 6]으로 나누어져 있는데, 5와 6이 연결되어 있지 않다.

불가능한 방법

각 선거구는 적어도 하나의 구역을 포함해야 한다.

공평하게 선거구를 나누기 위해 두 선거구에 포함된 인구의 차이를 최소로 하려고 한다. 백준시의 정보가 주어졌을 때, 인구 차이의 최솟값을 구해보자.

입력
첫째 줄에 구역의 개수 N이 주어진다. 둘째 줄에 구역의 인구가 1번 구역부터 N번 구역까지 순서대로 주어진다. 인구는 공백으로 구분되어져 있다.

셋째 줄부터 N개의 줄에 각 구역과 인접한 구역의 정보가 주어진다. 각 정보의 첫 번째 정수는 그 구역과 인접한 구역의 수이고, 이후 인접한 구역의 번호가 주어진다. 모든 값은 정수로 구분되어져 있다.

구역 A가 구역 B와 인접하면 구역 B도 구역 A와 인접하다. 인접한 구역이 없을 수도 있다.

출력
첫째 줄에 백준시를 두 선거구로 나누었을 때, 두 선거구의 인구 차이의 최솟값을 출력한다. 두 선거구로 나눌 수 없는 경우에는 -1을 출력한다.

제한
2 ≤ N ≤ 10
1 ≤ 구역의 인구 수 ≤ 100
'''
import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations
# sys.stdin = open('게리멘더링.txt', 'r')

# 연결이 되어있는지 확인하는 함수
def is_connected(group):
    stack = deque()
    stack.append(group[0])
    visited = [0] * (N+1)
    visited[group[0]] = 1

    while stack:
        u = stack.popleft()
        for v in adjlist[u]:
            if v in group and not visited[v]:
                stack.append(v)
                visited[v] = 1
    for g in group:
        if visited[g] == 0:
            return False
    return True

N = int(input())
popular = [0] + list(map(int, input().split()))
adjlist = [[] for _ in range(N+1)]
for i in range(1, N+1):
    temp = list(map(int, input().split()))
    adjlist[i].extend(temp[1:])

# 정점들
V = [i for i in range(1, N+1)]
rst = float('inf')
# 두 그룹으로 나누기 때문에 N//2+1 이상으로 넘어가면 조합이 중복되어 똑같은 작업을 한다.
for i in range(1, N//2+1):
    # group1에 대해선 itertools사용, group2는 자동적으로 group1을 포함하지 않는 그룹임
    for group1 in combinations(V, i):
        group2 = [j for j in V if j not in group1]
        # 두 그룹에 대해서 연결이 되는 그래프인지 확인을 해봐야된다.
        if is_connected(group1) and is_connected(group2):
            group1_num = sum([popular[g] for g in group1])
            group2_num = sum([popular[g] for g in group2])
            rst = min(rst, abs(group1_num-group2_num))
if rst == float('inf'):
    print(-1)
else:
    print(rst)


# def bfs(arr_A):
#     global min_val, flag
#     for j in range(1, N+1):
#         if j not in arr_A:
#             areaB = [j]
#             stackB = deque()
#             stackB.append(j)
#             while stackB:
#                 v = stackB.popleft()
#                 for w in adjlist[v]:
#                     if w not in areaB and w not in arr_A:
#                         stackB.append(w)
#                         areaB.append(w)
#             if len(arr_A) + len(areaB) == N:
#                 areaA_popular = 0
#                 areaB_popular = 0
#                 for x in arr_A:
#                     areaA_popular += popular[x]
#                 for y in areaB:
#                     areaB_popular += popular[y]
#                 min_val = min(min_val, abs(areaA_popular-areaB_popular))
#                 flag = True
#                 return
            
# def dfs(s, L):
#     visited[s] = 1
#     if len(areaA) == L:
#         bfs(areaA)
#     while stack:
#         v = stack.pop()
#         for w in adjlist[v]:
#             if not visited[w]:
#                 stack.append(w)
#                 areaA.append(w)
#                 dfs(w, L+1)
#                 areaA.pop()
#                 visited[w] = 0
                
# N = int(input())
# popular = [0] + list(map(int, input().split()))
# adjlist = [[] for _ in range(N+1)]
# for i in range(1, N+1):
#     temp = list(map(int, input().split()))
#     adjlist[i].extend(temp[1:])
# min_val = float('inf')
# flag = False
# for i in range(1, N//2):
#     areaA= [i]
#     stack = []
#     stack.append(i)
#     visited = [0] * (N+1)
#     dfs(i, 1)
# print(min_val) if flag else print(-1)

# def bfs(arr_A):
#     global min_val, flag
#     for j in range(1, N+1):
#         if j not in arr_A:
#             areaB = [j]
#             stackB = [j]
#             while stackB:
#                 v = stackB.pop(0)
#                 for w in adjlist[v]:
#                     if w not in areaB and w not in arr_A:
#                         stackB.append(w)
#                         areaB.append(w)
#             if len(arr_A) + len(areaB) == N:
#                 areaA_popular = 0
#                 areaB_popular = 0
#                 for x in arr_A:
#                     areaA_popular += popular[x]
#                 for y in areaB:
#                     areaB_popular += popular[y]
#                 min_val = min(min_val, abs(areaA_popular-areaB_popular))
#                 flag = True
#                 return
            
# def dfs(s, L):
#     visited[s] = 1
#     if len(areaA) == L:
#         bfs(areaA)
#     while stack:
#         v = stack.pop()
#         for w in adjlist[v]:
#             if not visited[w]:
#                 stack.append(w)
#                 areaA.append(w)
#                 dfs(w, L+1)
#                 areaA.pop()
#                 visited[w] = 0
                
# N = int(input())
# popular = [0] + list(map(int, input().split()))
# adjlist = [[] for _ in range(N+1)]
# for i in range(1, N+1):
#     temp = list(map(int, input().split()))
#     adjlist[i].extend(temp[1:])
# min_val = 1000
# flag = False
# for i in range(1, N+1):
#     areaA= [i]
#     stack = []
#     stack.append(i)
#     visited = [0] * (N+1)
#     dfs(i, 1)
# print(min_val) if flag else print(-1)
