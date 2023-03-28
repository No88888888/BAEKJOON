'''
문제
개구리가 일렬로 놓여 있는 징검다리 사이를 폴짝폴짝 뛰어다니고 있다. 징검다리에는 숫자가 각각 쓰여 있는데, 이 개구리는 매우 특이한 개구리여서 어떤 징검다리에서 점프를 할 때는 그 징검다리에 쓰여 있는 수의 배수만큼 떨어져 있는 곳으로만 갈 수 있다.

이 개구리는 a번째 징검다리에서 b번째 징검다리까지 가려고 한다. 이 개구리가 a번째 징검다리에서 시작하여 최소 몇 번 점프를 하여 b번째 징검다리까지 갈 수 있는지를 알아보는 프로그램을 작성하시오.

입력
첫째 줄에 징검다리의 개수 N(1≤N≤10,000)이 주어지고, 이어서 각 징검다리에 쓰여 있는 N개의 정수가 주어진다. 그 다음 줄에는 N보다 작거나 같은 자연수 a, b가 주어지는 데, 이는 개구리가 a번 징검다리에서 시작하여 b번 징검다리에 가고 싶다는 뜻이다. 징검다리에 쓰여있는 정수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 개구리가 a번 징검다리에서 b번 징검다리로 최소 몇 번 점프하여 갈 수 있는 지를 출력하시오. a에서 b로 갈 수 없는 경우에는 -1을 출력한다.
'''


def jump():
    stack = [a]
    visited = [-1] * (N)    # 점프 횟수 기록
    visited[a] = 0
    while stack:
        node = stack.pop(0)
        for n in range(node, N, bridge[node]):  # 오른쪽으로 뛰기
            if visited[n] == -1:
                stack.append(n)
                visited[n] = visited[node] + 1
                if n == b:              # 목표위치면
                    return visited[n]   # 거기까지 오는데 걸린 점프횟수 출력
        for n in range(node, -1, -bridge[node]):# 왼쪽으로 뛰기
            if visited[n] == -1:
                stack.append(n)
                visited[n] = visited[node] + 1
                if n == b:
                    return visited[n]
    return -1

N = int(input())
bridge = list(map(int, input().split()))    # 징검다리
a, b = map(int, input().split())            # 시작위치, 목표위치
a -= 1          # 인덱싱
b -= 1
print(jump())
    # if s < 0 or s > len(bridge):
    #     return
    # if s == e:
    #     res = min(cnt, res)
    #     print(res)
    #     return
    # n = 1
    # while stack:
    #     x = stack.pop(0)
    #     if 0 <= x - bridge[x]*n:
    #         jump(x - bridge[x]*n, e, cnt + 1)
    #         stack.append(x - bridge[x]*n)
    #     if x + bridge[x]*n <= len(bridge):
    #         jump(x + bridge[x]*n, e, cnt + 1)
    #         stack.append(x + bridge[x]*n)
    #     n += 1
        
    # while s != e:
    #     if 0 <= s - bridge[s]*n:
    #         jump(s - bridge[s]*n, e, cnt + 1)
    #     if s + bridge[s]*n <= len(bridge):
    #         jump(s + bridge[s]*n, e, cnt + 1)
    #     n += 1
            

    # while 0 <= s <= len(bridge):
    #     jump(s + bridge[s]*n, e, cnt + 1)
    #     jump(s - bridge[s]*n, e, cnt + 1)
    #     n += 1
        
        
