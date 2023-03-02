'''
문제
세로 R칸, 가로 C칸으로 된 표 모양의 보드가 있다. 보드의 각 칸에는 대문자 알파벳이 하나씩 적혀 있고, 좌측 상단 칸 (1행 1열) 에는 말이 놓여 있다.

말은 상하좌우로 인접한 네 칸 중의 한 칸으로 이동할 수 있는데, 새로 이동한 칸에 적혀 있는 알파벳은 지금까지 지나온 모든 칸에 적혀 있는 알파벳과는 달라야 한다. 즉, 같은 알파벳이 적힌 칸을 두 번 지날 수 없다.

좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성하시오. 말이 지나는 칸은 좌측 상단의 칸도 포함된다.

입력
첫째 줄에 R과 C가 빈칸을 사이에 두고 주어진다. (1 ≤ R,C ≤ 20) 둘째 줄부터 R개의 줄에 걸쳐서 보드에 적혀 있는 C개의 대문자 알파벳들이 빈칸 없이 주어진다.

출력
첫째 줄에 말이 지날 수 있는 최대의 칸 수를 출력한다.
'''
import sys
input = sys.stdin.readline

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)
    visited.add(alpha[x][y])

    for di, dj in delta:
        ni, nj = x + di, y + dj
        if 0 <= ni < R and 0 <= nj < C and alpha[ni][nj] not in visited:
            dfs(ni, nj, cnt+1)
            
    visited.remove(alpha[x][y])

R, C = map(int, input().split())

alpha = [list(input()) for _ in range(R)]
delta = (-1, 0), (0, 1), (1, 0), (0,-1)
visited = set()
ans = 0

dfs(0, 0, 1)
print(ans)

# def dfs():
#     maxdis = 0
#     cnt = 1
#     while stack:
#         x, y = stack.pop()
#         for di, dj in delta:
#             ni, nj = x + di, y + dj
#             if 0 <= ni < R and 0 <= nj < C and visited[x][y] >= visited[ni][nj] and alpha[ni][nj] not in letter:
#                 visited[ni][nj] = visited[x][y] + 1
#                 letter.append(alpha[ni][nj])
#                 stack.append((ni, nj))
#                 cnt += 1
#                 break
#         else:
#             maxdis = max(cnt, maxdis)
#             letter.pop()
#             stack.append((x, y))
#             cnt -= 1
            
            
#     print(visited)
#     # print(stack)
#     # print(cnt)
#     return maxdis

# R, C = map(int, input().split())

# alpha = [list(input()) for _ in range(R)]
# delta = (-1, 0), (0, 1), (1, 0), (0,-1)
# visited = [[0]*C for _ in range(R)]
# visited[0][0] = 1
# stack = [(0,0)]
# letter = []
# letter.append(alpha[0][0])

# print(dfs())