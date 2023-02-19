'''
문제
크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1,000으로 나눈 나머지를 출력한다.

입력
첫째 줄에 행렬의 크기 N과 B가 주어진다. (2 ≤ N ≤  5, 1 ≤ B ≤ 100,000,000,000)

둘째 줄부터 N개의 줄에 행렬의 각 원소가 주어진다. 행렬의 각 원소는 1,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄부터 N개의 줄에 걸쳐 행렬 A를 B제곱한 결과를 출력한다.
'''

N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr2 = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        arr2[i][j] = arr[j][i]
B = bin(B)[2:]
memo = [arr]
print(memo)
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             start[i][j] = 1
for k in range(1, len(B)):
    start = [[0 for _ in range(N)] for _ in range(N)]

    for x in range(N):
        temp = 0
        for y in range(N):
            temp += memo[k-1][x][y] * memo[k-1][y][x]
        start[i][j] = temp
            # print(start)
    memo.append(start)
print(memo)
for po in range(len(B)-1, -1, -1):
    for x in range(N):
        for y in range(N):
            
                