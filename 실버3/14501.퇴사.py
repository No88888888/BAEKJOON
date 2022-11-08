'''
문제
상담원으로 일하고 있는 백준이는 퇴사를 하려고 한다.

오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 하려고 한다.

백준이는 비서에게 최대한 많은 상담을 잡으라고 부탁을 했고, 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

N = 7인 경우에 다음과 같은 상담 일정표를 보자.

 	1일	2일	3일	4일	5일	6일	7일
Ti	3	5	1	1	2	4	2
Pi	10	20	10	20	15	40	200
1일에 잡혀있는 상담은 총 3일이 걸리며, 상담했을 때 받을 수 있는 금액은 10이다. 5일에 잡혀있는 상담은 총 2일이 걸리며, 받을 수 있는 금액은 15이다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 예를 들어서 1일에 상담을 하게 되면, 2일, 3일에 있는 상담은 할 수 없게 된다. 2일에 있는 상담을 하게 되면, 3, 4, 5, 6일에 잡혀있는 상담은 할 수 없다.

또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.

상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N (1 ≤ N ≤ 15)이주어진다.

둘째 줄부터 N개의 줄에 Ti와 Pi가 공백으로 구분되어서 주어지며, 1일부터 N일까지 순서대로 주어진다. (1 ≤ Ti ≤ 5, 1 ≤ Pi ≤ 1,000)

출력
첫째 줄에 백준이가 얻을 수 있는 최대 이익을 출력한다.
'''
'''
전체, 재귀 탐색
첫 for문으로 상담 시작날 지정
소요 날을 더해 N보다 커지면 return
상담 가능한 경우의 수 중 수입 가장 큰 것을 저장
'''
import sys
input= sys.stdin.readline

def jaegui(day, ssum):
    global maxV
    if ssum > maxV:
        maxV = ssum
    if day >= N:
        return
    if day + counseling[day][0] <= N:
        jaegui(day + counseling[day][0], ssum + counseling[day][1])
    jaegui(day + 1, ssum)

N = int(input())
counseling = [list(map(int, input().split())) for _ in range(N)]
maxV = 0

for i in range(N):
    jaegui(i, 0)
print(maxV)
    
    
    
    
    
    
    
    
    
    
    
    
    
#     if i + counseling[i][0] >= N:
#         break
#     sum = counseling[i][1]
#     while i < N:
#         if i + counseling[i][0] >= N:
#             break
#         i += counseling[i][0]
#         print(i)
#         sum += counseling[i][1]
#     if sum > maxV:
#         maxV = sum
# print(sum)