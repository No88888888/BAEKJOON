'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
RGB = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N):
    # 첫번째 집 무시하고 두번째집부터
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]   # 빨간색 집을 칠햇을때 최솟값
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]   # 초록색을 칠했을 때 최솟값
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]   # 파란색을 칠햇을 때 최솟값
print(min(RGB[N-1])) # 두번쨰집을 빨,초,파 로 칠햇을때 최소값들이 구해져 있다(완전 탐색) / 그 중 최소값을 출력한다


    
# dis = 0
# for i in range(N):
#     if i == 0:
#         min_value = 2001
#         for j in range(3):
#             if j == 0:
#                 temp = min(RGB[i][j] + RGB[i+1][j+1],  RGB[i][j] + RGB[i+1][j+2])
#                 if temp <= min_value:
#                     location = 0
#                 min_value = temp
#             elif j == 1:
#                 temp = min(RGB[i][j] + RGB[i+1][j-1], RGB[i][j] + RGB[i+1][j+1])
#                 if temp <= min_value:
#                     location = 1
#                 min_value = temp
#             elif j == 2:
#                 temp = min(RGB[i][j] + RGB[i+1][j-2], RGB[i][j] + RGB[i+1][j-1])
#                 if temp <= min_value:
#                     location = 2
#                 min_value = temp
#         dis += RGB[i][location]
#     elif i == N-1:
#         del RGB[i][location]
#         dis += min(RGB[i])
#     else:
#         if location == 0:
#             if min(RGB[i][1] + RGB[i+1][0], RGB[i][1] + RGB[i+1][2]) > min(RGB[i][2] + RGB[i+1][0], RGB[i][2] + RGB[i+1][1]):
#                 location = 2
                
#             elif min(RGB[i][1] + RGB[i+1][0], RGB[i][1] + RGB[i+1][2]) < min(RGB[i][2] + RGB[i+1][0], RGB[i][2] + RGB[i+1][1]):
#                 location = 1
#             else:
#                 location = RGB[i].index(min(RGB[i][1], RGB[i][2]))
#             dis += RGB[i][location]
#         elif location == 1:
#             if min(RGB[i][0] + RGB[i+1][1], RGB[i][0] + RGB[i+1][2]) > min(RGB[i][2] + RGB[i+1][0], RGB[i][2] + RGB[i+1][1]):
#                 location = 2
#             elif min(RGB[i][0] + RGB[i+1][1], RGB[i][0] + RGB[i+1][2]) < min(RGB[i][2] + RGB[i+1][0], RGB[i][2] + RGB[i+1][1]):
#                 location = 0
#             else:
#                 location = RGB[i].index(min(RGB[i][0], RGB[i][2]))
#             dis += RGB[i][location]
#         else:
#             if min(RGB[i][0] + RGB[i+1][1], RGB[i][0] + RGB[i+1][2]) > min(RGB[i][1] + RGB[i+1][0], RGB[i][1] + RGB[i+1][2]):
#                 location = 1
#             elif min(RGB[i][0] + RGB[i+1][1], RGB[i][0] + RGB[i+1][2]) < min(RGB[i][1] + RGB[i+1][0], RGB[i][1] + RGB[i+1][2]):
#                 location = 0
#             else:
#                 location = RGB[i].index(min(RGB[i][0], RGB[i][1]))
#             dis += RGB[i][location]
# print(dis)