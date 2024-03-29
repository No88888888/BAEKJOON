'''
문제
매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.

입력
첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.

출력
세준이가 운전해야하는 거리의 최솟값을 출력하시오.
'''
import sys
input = sys.stdin.readline

N, D = map(int, input().split())                                            # 지름길의 갯수 N, 고속도로의 길이 D
shortCut = [[] for _ in range(D+1)]                                         # 지름길 정보를 담을 배열                
min_dis = [i for i in range(D+1)]                                           # 각 노드까지의 최소길이를 저장할 배열

for i in range(N):                                                          # 시작위치, 도착위치, 지름길의 거리 받기
    S, E, V = map(int, input().split())
    if S <= D:                                                              # 시작위치가 고속도로 끝보다 넘으면 무시
        shortCut[S].append([E, V])

for j in range(D+1):                                                        # 1미터 당 각 노드라고 생각
    if j:                                                                   # 0미터 제외
        min_dis[j] = min(min_dis[j-1] + 1, min_dis[j])                      # 앞까지의 거리 + 1와 현재노드 거리(지름길을 통해 온 길일 수 있음) 중 짧은 거리가 현재오드까지의 최소거리
    if shortCut[j]:                                                         # 현재노드에서 지름길이 있다면
        for adj in shortCut[j]:                                             # 지름길들을 순회
            if adj[0] <= D:                                                 # 도착위치가 고속도로 거리 이하라면
                min_dis[adj[0]] = min(min_dis[adj[0]], min_dis[j]+adj[1])   # 도착위치까지의 최소거리는 지름길 이용 X 떄 거리와 지름길 이용 O 때 거리 중 짧은 거리
print(min_dis[D])                                                           # 최종 고속도로 끝 지점 의 거리 출력
