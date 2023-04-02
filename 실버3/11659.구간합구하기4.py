'''
문제
수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N과 합을 구해야 하는 횟수 M이 주어진다. 둘째 줄에는 N개의 수가 주어진다. 수는 1,000보다 작거나 같은 자연수이다. 셋째 줄부터 M개의 줄에는 합을 구해야 하는 구간 i와 j가 주어진다.

출력
총 M개의 줄에 입력으로 주어진 i번째 수부터 j번째 수까지 합을 출력한다.

제한
1 ≤ N ≤ 100,000
1 ≤ M ≤ 100,000
1 ≤ i ≤ j ≤ N
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
number = list(map(int, input().split()))
memo = [0] * (N)                     # 0번부터 해당 인덱스까지의 합 저장할 배열
memo[0] = number[0]

for n in range(1, N):
    memo[n] = number[n] + memo[n-1]  # 앞까지의 누적합 + 현재 인덱스의 숫자
for _ in range(M):
    i, j = map(int, input().split())
    i -= 1                           # 인덱스 위해 -1
    j -= 1
    if i == 0:                       # 시작 부터면
        ans = memo[j]                # j인덱스의 누적합을 출력
    else:                            # 중간부터라면
        ans = memo[j] - memo[i-1]    # j까지의 누적합에서 i전까지의 누적합을 빼서 ans를 구한다
    print(ans)