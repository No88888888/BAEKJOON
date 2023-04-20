'''
문제
세로 두 줄, 가로로 N개의 칸으로 이루어진 표가 있다. 첫째 줄의 각 칸에는 정수 1, 2, …, N이 차례대로 들어 있고 둘째 줄의 각 칸에는 1이상 N이하인 정수가 들어 있다. 첫째 줄에서 숫자를 적절히 뽑으면, 그 뽑힌 정수들이 이루는 집합과, 뽑힌 정수들의 바로 밑의 둘째 줄에 들어있는 정수들이 이루는 집합이 일치한다. 이러한 조건을 만족시키도록 정수들을 뽑되, 최대로 많이 뽑는 방법을 찾는 프로그램을 작성하시오. 예를 들어, N=7인 경우 아래와 같이 표가 주어졌다고 하자.



이 경우에는 첫째 줄에서 1, 3, 5를 뽑는 것이 답이다. 첫째 줄의 1, 3, 5밑에는 각각 3, 1, 5가 있으며 두 집합은 일치한다. 이때 집합의 크기는 3이다. 만약 첫째 줄에서 1과 3을 뽑으면, 이들 바로 밑에는 정수 3과 1이 있으므로 두 집합이 일치한다. 그러나, 이 경우에 뽑힌 정수의 개수는 최대가 아니므로 답이 될 수 없다.

입력
첫째 줄에는 N(1≤N≤100)을 나타내는 정수 하나가 주어진다. 그 다음 줄부터는 표의 둘째 줄에 들어가는 정수들이 순서대로 한 줄에 하나씩 입력된다.

출력
첫째 줄에 뽑힌 정수들의 개수를 출력하고, 그 다음 줄부터는 뽑힌 정수들을 작은 수부터 큰 수의 순서로 한 줄에 하나씩 출력한다.
'''

# 시간초과
import sys
input = sys.stdin.readline
def gkatn(start, temp, lth):
    global max_length, ans
    if len(temp) == lth:
        arr = []
        for i in range(lth):
            if ch[temp[i]] in arr:
                return
            arr.append(ch[temp[i]])
        A, B = sorted(arr), sorted(temp)
        if A == B:
            max_length = max(len(arr), max_length)
            ans = A
        return
    for j in range(start, N+1):
        if used[j] == 0:
            used[j] = 1
            temp.append(j)
            gkatn(j, temp, lth)
            temp.pop()
            used[j] = 0
N = int(input())
ch = [0] + [int(input()) for _ in range(N)]

max_length = 0
ans = []
for k in range(1, N+1):
    used = [0]*(N+1)
    gkatn(1, [], k)
print(max_length)
for r in ans:
    print(r)

import sys

input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N + 1)]

for i in range(1, N + 1):
    adj[i].append(int(input()))


# DFS로 탐색하다가 사이클 발생한 것들을 다 더하면 된다 !!

def dfs(num):
    if visited[num] == False:
        visited[num] = True
        for a in adj[num]:

            tmp_up.add(num)
            tmp_bottom.add(a)
            print(tmp_up)
            print(tmp_bottom)
            if tmp_up == tmp_bottom:
                ans.extend(list(tmp_bottom))
                return

            dfs(a)
    visited[num] = False


ans = []

for i in range(1, N + 1):
    visited = [False] * (N + 1)  # 위에 값 기준으로
    tmp_up = set()
    tmp_bottom = set()

    dfs(i)

ans = list(set(ans))
ans.sort()

print(len(ans))
for a in ans:
    print(a)

# def comb(temp, length):
#     global cnt
#     if len(temp) == length:
#         print(temp)
    
#     for i in range(1, N+1):
#         if visited[i] == 0:
#             temp.append(i)
#             visited[i] = 1
#             comb(temp, cnt)
            
#             visited[temp.pop()] = 0
#             print(visited)
#     cnt += 1
# N = int(input())
# dict = {}
# for i in range(1,N+1):
#     dict[i] = int(input())
# number = [i for i in range(1,N+1)]
# cnt = 1
# visited = [0 for _ in range(N+1)]
# comb([], cnt)