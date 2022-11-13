'''
문제
상근(Albert), 민혁(Barbara), 선영(Casper), 창영(Dinko), 현진(Eustahije)이가 마라톤 틱택토 게임을 하려고 한다. 이 게임은 N×N 보드에서 진행한다.

맨 처음에 보드의 모든 칸은 비어있다. 플레이어는 턴을 번갈아가면서 자신의 영어 이름의 첫 글자를 빈 칸에 적는다. (두 사람의 영어 이름의 첫 글자가 같은 경우는 없다)

게임은 세 글자가 행, 열, 또는 대각선으로 연속할 때, 그 플레이어가 승리하며, 게임이 끝나게 된다.

보드판의 상태가 주어졌을 때, 게임이 끝났는지 아닌지를 결정하고, 끝났다면 승자가 누구인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 보드판의 크기 N이 주어진다. (1 ≤ N ≤ 30)

다음 N개 줄에는 보드판의 상태가 주어진다. '.'는 빈 칸을 나타낸다.

항상 승리한 사람이 많아야 한 명인 경우만 입력으로 주어진다. 

출력
첫째 줄에 게임이 끝났다면, 승리한 사람의 영어 이름의 첫 글자를 출력한다. 그렇지 않다면, "ongoing"을 출력한다. 게임을 승리한 사람이 없는데, 빈 칸이 없는 경우에도 ongoing을 출력해야 한다.
'''
N = int(input())
tic = [list(input()) for _ in range(N)]
delta = [(0,1), (1,1), (1,0), (1,-1)]

for i in range(N):
    for j in range(N):
        if tic[i][j] != '.':                        # 빈칸이 아니면
            for x, y in delta:                      # 가로,세로,대각,역대각 탐색
                for k in range(1,3):                # 해당 위치에서 두칸 뒤까지를 체크
                    di, dj = x * k, y * k
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N: # 범위 내면서
                        if tic[i][j] != tic[ni][nj]:# 하나라도 같지 않다면
                            break                   # break
                    else:                           # 범위 벗어나면
                        break                       # break
                else:                               # 다 같았다면
                    print(tic[i][j])                # 해당 이름 출력
                    exit()
print('ongoing')                                    # 끝까지 아무 이름도 출력 안됐다면 ongoing


# 세글자 연속이 아니라 빙고를 찾는 줄 알고 잘못 푼 풀이
# N = int(input())
# tic = [list(input()) for _ in range(N)]
# tic90 = [[0] * N for _ in range(N)]
# daegak, reversedaedgak = '', ''
# for i in range(N):
#     for j in range(N):
#         tic90[j][i] = tic[i][j]
#         if i == j:
#             daegak += tic[i][j]
#         if i == N - 1 - j:
#             reversedaedgak += tic[i][j]

# for x in range(N):
#     for y in range(N):
#         if tic[x][y] != '.':
#             if x == 0:
#                 if (len(set(tic90[y])) == 1 and tic[x][y] == list(set(tic90[y]))[0]):
#                     print(tic[x][y])
#                     exit()
#                 if y == 0:
#                     if (len(set(tic[x])) == 1 and tic[x][y] == list(set(tic[x]))[0]) or (len(set(daegak)) == 1 and tic[x][y] == list(set(daegak))[0]):
#                         print(tic[x][y])
#                         exit()
#                 elif y == N-1:
#                     if (len(set(reversedaedgak)) == 1 and tic[x][y] == list(set(reversedaedgak))[0]):
#                         print(tic[x][y])
#                         exit()
#             else:
#                 if y == 0:
#                     if len(set(tic[x])) == 1 and tic[x][y] == list(set(tic[x]))[0]:
#                         print(tic[x][y])
#                         exit()
# print('ongoing')
            
                    
                        
                        
                    
        #             if tictactoe[x][y] == list(set(tictactoe[0]))[0] or tictactoe[x][y] == list(set(tictactoe90[0]))[0]:
        #                 print(tictactoe[x][y])
        #                 exit()
        #             # elif tictactoe[x][y] == daegak
        #         # 가로 탐색
        #         # 대각선 탐색
        #         pass
        #     elif y == N-1:
        #         # 역대각선 탐색
        #         pass
        #     # 세로탐색
        # else:
        #     if y == 0:
        #         # 가로 탐색
        #         pass