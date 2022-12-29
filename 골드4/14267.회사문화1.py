'''
문제
영선회사에는 매우 좋은 문화가 있는데, 바로 상사가 직속 부하를 칭찬하면 그 부하가 부하의 직속 부하를 연쇄적으로 칭찬하는 내리 칭찬이 있다. 즉, 상사가 한 직속 부하를 칭찬하면 그 부하의 모든 부하들이 칭찬을 받는다.

모든 칭찬에는 칭찬의 정도를 의미하는 수치가 있는데, 이 수치 또한 부하들에게 똑같이 칭찬 받는다.

직속 상사와 직속 부하관계에 대해 주어지고, 칭찬에 대한 정보가 주어질 때, 각자 얼마의 칭찬을 받았는지 출력하시오,

입력
첫째 줄에는 회사의 직원 수 n명, 최초의 칭찬의 횟수 m이 주어진다. 직원은 1번부터 n번까지 번호가 매겨져 있다. (2 ≤ n, m ≤ 100,000)

둘째 줄에는 직원 n명의 직속 상사의 번호가 주어진다. 직속 상사의 번호는 자신의 번호보다 작으며, 최종적으로 1번이 사장이다. 1번의 경우, 상사가 없으므로 -1이 입력된다.

다음 m줄에는 직속 상사로부터 칭찬을 받은 직원 번호 i, 칭찬의 수치 w가 주어진다. (2 ≤ i ≤ n, 1 ≤ w ≤ 1,000)

사장은 상사가 없으므로 칭찬을 받지 않는다.

출력
1번부터 n번의 직원까지 칭찬을 받은 정도를 출력하시오.
'''

# 최저 시간을 위한 코드 156ms

import sys
input = sys.stdin.readline
def gkatn():
    N, M = map(int, input().split())
    emp = [0] + list(map(int, input().split())) # 0 패딩 포함시켜 상하관계 입력
    dp = [0] * (N+1)                            # 직원들 각각의 최종 칭찬량을 담을 배열
    for _ in range(M):
        E, S = map(int, input().split())        # 직원번호와 칭찬량을 받아서 
        dp[E] += S                              # 해당 직원에게 더해줌(동일 직원 2번이상 칭찬할 수 있으므로 +로)
    for i in range(2, N+1):                     # 사장 제외하고 2번 직원부터
        dp[i] += dp[emp[i]]                     # 본인의 직속 상사의 칭찬량과 본인의 칭찬량을 더해 최종 본인 칭찬량을 저장한다
    print(*dp[1:])                              # 패딩 때문에 필요없는 0번을 제외하고 1번부터 출력
gkatn()             # 함수로 호출하는 것이 더 빠름


# 본 코드 216ms

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
emp = [0] + list(map(int, input().split()))                 # 0 패딩 포함시켜 상하관계 입력
com = [list(map(int, input().split())) for _ in range(M)]   # 직원번호, 칭찬 입력
dp = [0] * N                                                # 최종 칭찬량

for E, s in com:          # 최고 직속 상사의 칭찬량을 디폴트값으로 넣어줌
    dp[E-1] += s

for i in range(2, N+1):     # 사장 제외(2번 직원부터 시작)
    dp[i-1] = dp[emp[i]-1] + dp[i-1]    # 본인 직속 상사의 칭찬량과 자신의 칭찬량을 더함
print(*dp)



#19% 시간초과
# import sys
# input = sys.stdin.readline

# def dfs(x, y):
#     stack = [x]
#     while stack:
#         i = stack.pop()
#         if ch[i]:
#             stack.extend(ch[i])
#             for j in ch[i]:
#                 dp[j-1] += y

# N, M = map(int, input().split())
# emp = list(map(int, input().split()))
# com = sorted([list(map(int, input().split())) for _ in range(M)])
# ch = [[] for _ in range(N+1)]
# dp = [0] * N
# for i in range(N):
#     if emp[i] > 0:
#         ch[emp[i]].append(i+1)
# for E, s in com:
#     dp[E-1] += s
#     dfs(E, s)
# print(*dp)

    
    
#21% 시간초과
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# emp = list(map(int, input().split()))
# ch = [[] for _ in range(N+1)]
# dp = [0] * N

# for i in range(N+1):
#     if emp[i] > 1:
#         ch[emp[i]].append(i)
#         stack = [emp[i]]
#         while stack:
#             x = stack.pop()
#             if emp[x] > 1:
#                 ch[emp[x]].append(i)
#                 stack.append(emp[x])
# for _ in range(M):
#     E, s = map(int, input().split())
#     dp[E-1] += s
#     for i in ch[E]:
#         dp[i-1] += s
# print(*dp)   



