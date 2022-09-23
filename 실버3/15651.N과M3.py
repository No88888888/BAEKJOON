'''
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''
from collections import deque
import sys
input = sys.stdin.readline

def nPm():
    s_app = s.append
    s_pop = s.pop
    if len(s) == M:
        print(*s)
        return
    else:
        for i in arr:
            s_app(i)
            nPm()
            s_pop()


N, M = map(int, input().split())
arr = [ i for i in range(1,N+1)]
s = deque()
nPm()

#--------------------------------------------------

N, M = map(int, input().split())
arr = [ i for i in range(1,N+1)]
subsets = [[]]  # 부분집합을 담을 녀석


# def d_sup():
#     for sub in subsets:
#         if sum(sub) == 10:
#             print(sub)


for num in arr:
    for i in range(len(subsets)):
        subsets.append(subsets[i] + [num])  # [1, 2, 3, 4]
subsets.sort()    
for i in subsets:
    if len(i) == M:
        print(*i)
# print(f'{num} : {subsets}')