import sys
sys.setrecursionlimit(100000)

def solution(root, count):
    count += 1
    global now_distance, max_distance
    if len(arr[root]) == 1 and count != 1:
        # print(now_distance)
        max_distance = max(max_distance, now_distance)
        return
    else:
        for number, distance in arr[root]:
            if visited[number]:
                continue
            else:
                visited[root] = 1
                now_distance += distance
                print(f'number:{number}')
                solution(number, count)
                now_distance -= distance
                visited[root] = 0



N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
list_a = []
for _ in range(N-1):
    start, end, distance = map(int, sys.stdin.readline().split())
    arr[start].append((end, distance))
    arr[end].append((start, distance)) # 한방향 => 위쪽 올라가는 형태
print(arr)
for i in arr: # 가운데껀 셀 필요가 없다.
    if len(i) == 1:
        list_a.append(arr.index(i))

# print(list_a)
visited = [0] * (N+1)
max_distance = 0

for i in list_a:
    # print(f"#{i}")
    now_distance = 0
    count = 0 # 첫번째를 방지하기 위한 방법
    solution(i, count)
print(max_distance)