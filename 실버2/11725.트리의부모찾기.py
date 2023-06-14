'''
문제
루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 노드의 개수 N (2 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N-1개의 줄에 트리 상에서 연결된 두 정점이 주어진다.

출력
첫째 줄부터 N-1개의 줄에 각 노드의 부모 노드 번호를 2번 노드부터 순서대로 출력한다.
'''
import sys
input = sys.stdin.readline

N =int(input())                         # 노드의 개수
tree = [[] for _ in range(N+1)]         # 트리 정보를 담을 배열
par = [0] * (N+1)                       # 최종 부모 노드 정보 담을 배열

for i in range(N-1):
    a, b = map(int, input().split())     # 일단 양방향 간선으로 입력 받음
    tree[a].append(b)
    tree[b].append(a)

stack = [1]                             # 루트 노드 1이라 가정, 루트노드부터 아래로 내려가며 탐색
while stack:
    v = stack.pop()                     # 현재 노드 v
    for w in tree[v]:                   # 연결된 노드들 w를 탐색
        if par[w]:                      # w의 부모 노드가 이미 결정되어 있다면
            continue                    # 넘어가고
        par[w] = v                      # 없다면 현재노드 v가 w의 부모 노드
        stack.append(w)                 # 다음 탐색을 위해 stack 추가
        
for k in range(2, N+1):                 # 2번 노드부터 부모 노드 정보 출력
    print(par[k])