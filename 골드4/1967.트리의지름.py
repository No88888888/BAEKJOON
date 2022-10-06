import sys
sys.setrecursionlimit(100000)
def diameter(node):
    global maxV
    global now_distance
    if len(arr[node]) == 1 and now_distance != 0:   # 리프노드이고 현재합이 0이 아니라면(시작리프노드 예외위해)
        if now_distance > maxV:                     # 현재 합이 최대값보다 크면
            maxV = now_distance                     # 최대값 변경
        return                                      # 리턴
    for w in arr[node]:         # 이웃한 노드 중
        if visited[w[0]]:       # 방문했다면
            continue            # 다음 노드 확인
        now_distance += w[1]    # 방문안했으면 가중치 더하고
        visited[w[0]] = 1       # 방문 표시
        diameter(w[0])          # 해당 노드에서 다시 탐색
        now_distance -= w[1]    # return되어 돌아오면 이전 노드로 돌아가기 위해 직전 가중치 뺴고
        visited[w[0]] = 0       # 방문 표시 0으로

N = int(input())
arr = [[] for _ in range(N+1)]
for i in range(N-1):
    start, end, weight = map(int, input().split())  # 부모, 자식, 가중치
    arr[start].append((end, weight))                # 양방향 그래프로 저장
    arr[end].append((start,weight))
    
leaf_node = []              # leaf 노드 인덱스만 list_a에 따로 저장
for i in range(len(arr)):
    if len(arr[i]) == 1:
        leaf_node.append(i)
        
maxV = 0                    # 지름 최대값 저장할 maxV
for i in leaf_node:
    visited = [0]*(N+1)
    visited[i] = 1
    now_distance = 0        # 더해가는 가중치를 저장할 now_distance
    diameter(i)             # 각 리프노드에서 탐색 시작
print(maxV)                 # 최종 maxV에 저장 된 값 출력