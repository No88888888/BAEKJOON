'''
문제
네모는 뿌××× 게임에 깊은 감명을 받아, 직사각형 모양의 격자판과 “넴모”라는 수수께끼의 생물을 이용하는 “넴모넴모”라는 게임을 만들었다. 이 게임의 규칙은 아주 간단하다. 격자판의 비어 있는 칸을 임의로 골라 “넴모”를 하나 올려놓거나, “넴모”가 올라간 칸 네 개가 2 × 2 사각형을 이루는 부분을 찾아 그 위에 있는 “넴모”들을 모두 없애는 것을 질릴 때까지 반복하면 된다.



하지만 안타깝게도 게임은 정말 재미가 없었고, 네모는 아주 빨리 질려 버리고 말았다. 실망한 네모는 게임을 적당히 플레이하다가, “넴모”를 없애고 싶은데 격자판 위에 없앨 수 있는 “넴모”가 없으면 게임을 그만두기로 했다. 네모가 게임을 그만두었을 때 나올 수 있는 “넴모”의 배치의 가짓수를 구하여라.

입력
첫 번째 줄에 격자판의 행의 개수 N, 열의 개수 M(1 ≤ N, M ≤ 25, 1 ≤ N × M ≤ 25)이 공백으로 구분되어 주어진다.

출력
첫 번째 줄에 주어진 격자판에서 나올 수 있는, “넴모”들이 올라간 칸이 2 × 2 사각형을 이루지 않는 모든 배치의 가짓수를 출력한다.
'''

N, M = map(int, input().split())
whole = 2*(N*M)
visited = list([0]*N for _ in range(M))
# print(visited)
cnt = 0
def BT(hap):
    global cnt
    di = [0,-1,-1]
    dj = [-1,0,-1]
    
    if hap < 3:
        return
    if hap == 3:
        cnt += 1
        # hap= 0
        # for k in range(3):
        #     hap += visited[i+di[k]][j+dj[k]]
        #     if hap == 3:
        #         cnt += 1
        #     else:
        #         pass
            
    for i in range(N+1):
        for j in range(M+1):
            visited[i][j] = 1
            for k in range(3):
                ni, nj = i + di[k], j + dj[k]
                if 0<=ni<N and 0<=nj<M:
                    hap += visited[i+di[k]][j+dj[k]]
            BT(hap)
            visited[i][j] = 0
    return cnt
print(BT(3))

# N, K = map(int, input().split())
# W = list(map(int, input().split())) # 중량 증가량
# visited = [0]*N
# cnt = 0

# def BT(SUM):
#     global cnt
    
#     if SUM < 500:                   # 500이하면 다음으로
#         return
    
#     if SUM >= 500 and all(visited): # 500이상이고 N일동안 키트 모두 사용 시
#         cnt += 1                    # cnt + 1
        
    
#     for i in range(N):
#         if not visited[i]:          # 키트 미 사용시
#             visited[i] = 1          # 사용
#             BT(SUM - K + W[i])      # 500 - K + 키트사용을 재귀호출
#             visited[i] = 0          # 중간에 500 이하거나 키트 전사용 시 부모 노드로 돌아가기 위함

# BT(500)
# print(cnt)    