'''
문제
정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.



한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 

두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. w와 h는 50보다 작거나 같은 양의 정수이다.

둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

입력의 마지막 줄에는 0이 두 개 주어진다.

출력
각 테스트 케이스에 대해서, 섬의 개수를 출력한다.
'''
def find_set(x,y):
    while rep[x][y] != (x, y):
        (x,y) = rep[x][y]
    return (x,y)

def union(x,y,a,b):
    rep[a][b] = find_set(x,y)

w, h = 1, 1
while w != 0 and h != 0:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    rep = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            rep[i][j] = (i,j)           # 각 인덱스 별 고유 대표원소 기본값 저장(자기자신, 2차원좌표 튜플형태)
    mmap = [list(map(int, input().split())) for _ in range(h)]  # 지도
    
    visited = [[0]*(w) for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if mmap[i][j] == 1:     # 1이라면
                stack = [[i,j]]     
                while stack:        # 깊이 우선 탐색
                    x, y = stack.pop()
                    for di, dj in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
                        ni, nj = x + di, y+dj
                        if 0<=ni<h and 0<=nj<w and visited[ni][nj] == 0 and mmap[ni][nj]:
                            visited[ni][nj] = 1
                            union(i,j,ni,nj)        # 붙은 땅끼리 union(대표원소 맞춰주기)
                            stack.append([ni,nj])
    res = set()
    for i in rep:
        for j in i:
            res.add(tuple(j))   # rep에서 대표원소들만 set으로 정렬하여 res에 저장
    cnt0 = 0
    for i in mmap:
        cnt0 += i.count(0)      # 지도에서 바다의 개수를 셈
    
    print(len(res)-cnt0)        # res - 바다의 개수 = 섬의 개수



# def find_set(x,y):
#     while rep[x][y] != (x, y):
#         (x,y) = rep[x][y]
#     return (x,y)

# def union(x,y,a,b):
#     rep[a][b] = find_set(x,y)
#     # rep[find_set(a,b)] = find_set(x,y)

# w, h = 1, 1
# while w != 0 and h != 0:
#     w, h = map(int, input().split())
#     if w == 0 and h == 0:
#         break
#     rep = [[0]*w for _ in range(h)]
#     for i in range(h):
#         for j in range(w):
#             rep[i][j] = (i,j)
#     mmap = [list(map(int, input().split())) for _ in range(h)]
#     visited = [[0]*(w) for _ in range(h)]
#     # while 0<= i <= h-1 and 0<= j <= w-1:
#     for i in range(h):
#         for j in range(w):
#             if mmap[i][j] == 1:
#                 for di, dj in [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]:
#                     ni, nj = i + di, j+dj
#                     if 0<=ni<h and 0<=nj<w and visited[ni][nj] == 0 and mmap[ni][nj]:
#                         visited[ni][nj] = 1
#                         union(i,j,ni,nj)
#                         i, j = ni, nj 
#     res = set()
#     for i in rep:
#         for j in i:
#             res.add(tuple(j))
#     cnt0 = 0
#     for i in mmap:
#         cnt0 += i.count(0)
    
#     print(len(res)-cnt0)