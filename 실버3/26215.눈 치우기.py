'''
문제
지난 밤 겨울 숲에는 눈이 많이 내렸다. 당신은 숲의 주민들을 위해 눈이 오지 않는 동안 모든 집 앞의 눈을 치우고자 한다.

당신은 1분에 한 번씩 두 집을 선택해서 두 집 앞의 눈을 각각 1만큼 치우거나, 한 집을 선택해서 그 집 앞의 눈을 1만큼 치울 수 있다.

모든 집 앞의 눈을 전부 치울 때까지 걸리는 최소 시간은 얼마일까?

입력
첫 줄에 집의 수를 의미하는 정수 $N$ ($1 \leq N \leq 100$)이 주어진다.

다음 줄에는 각각의 집 앞에 쌓여 있는 눈의 양을 나타내는 정수 $a_{i}$ ($1 \leq a_{i} \leq 2000$)이 주어진다.

출력
모든 집 앞의 눈을 치우는 데 최소 몇 분이 걸리는지를 출력한다. 24시간(1440분)이 넘게 걸릴 경우 -1을 출력한다.
'''
from heapq import heapify, heappush, heappop

N = int(input())
snow = list(map(lambda x: -int(x), input().split()))    # 최대힙 만들기 위해 - 붙여서 snow 생성
time = 0        # 눈 치우는데 걸린 총 시간
heapify(snow)   # heapify로 최소힙을 만든다(- 붙어있기 때문에 사싱상 최대힙을 만들기 위함)

while snow:     # 눈을 다 치울 동안
    if len(snow) <= 1:          # 치울 집이 하나 남았다면
        time += abs(snow[0])    # 해당 집만 치우면 되기 때문에 시간에 해당 집 눈의 양 더하고 끝낸다
        break
    a, b = heappop(snow), heappop(snow) # 2개 이상 집 남았다면 최소 값 두개를 가져온다(사실 상 눈이 제일 많이 남은 집 2개)
    time += abs(b)                      # 2집을 동시에 치우는 시간 = 두 집중 눈이 적게 남은 집의 눈의 양
    heappush(snow, a-b)                 # 2개 집 치우고 눈이 더 많았던 집의 남은 눈의 양을 다시 snow에 넣어준다
    
print(time if time < 1441 else -1)      # 총 걸린 시간이 1441분 미만이라면 해당 시간, 이상이면 -1 출력

N = int(input())
snow = sorted(list(map(int, input().split())), reverse=True) # 눈 양 내림차순 정렬
time = 0    # 눈 치우는데 걸린 총 시간

while snow:             # 눈 다치울 때까지
    if len(snow) <= 1:  # 치울 집 하나 밖에 안남았다면
        time += snow[0] # 해당 집 남은 눈 양 시간에 더하고 끝낸다
        break
    snow[0] -= 1        # 가장 많이 남은 두집에서 눈 치우고
    snow[1] -= 1
    time += 1           # 시간 + 1
    snow.sort(reverse=True) # 다시 내림차순 정렬
    while snow and snow[-1] == 0:   # 다 치운집 버린다
        snow.pop()
print(time if time < 1441 else -1)  # 1441분 미만이면 해당 시간, 이상이면 -1 출력