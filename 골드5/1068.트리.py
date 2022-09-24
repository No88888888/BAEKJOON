'''
문제
트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.

트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.

예를 들어, 다음과 같은 트리가 있다고 하자.



현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.



이제 리프 노드의 개수는 1개이다.

입력
첫째 줄에 트리의 노드의 개수 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 0번 노드부터 N-1번 노드까지, 각 노드의 부모가 주어진다. 만약 부모가 없다면 (루트) -1이 주어진다. 셋째 줄에는 지울 노드의 번호가 주어진다.

출력
첫째 줄에 입력으로 주어진 트리에서 입력으로 주어진 노드를 지웠을 때, 리프 노드의 개수를 출력한다.
'''
# 중간에 -1 나오는 경우가 핵심인 문제(트리가 2개 이상일 수 있다)
def enq(z):
    if z > N-1:
        return
    if ch[z]:           # 자식 노드에게 자식이 있다면
        for i in ch[z]: 
            enq(i)      # 리프 노드까지 내려간다
    if ch[z] == []:     # 리프 노드면
        ch[z].append(1) # 1을 채워준다

N = int(input())
arr = list(map(int, input().split()))
DN = int(input())
ch = [[] for _ in range(N)]

for i in range(N):          # 해당 인덱스(부모)의 자식 인덱스 넣어서 배열 ch만들기
    if arr[i] == -1:
        continue
    ch[arr[i]].append(i)
    
enq(DN)                     # 지우는 노드의 하위 자식,자손 노드들에 값을 채운다

if DN in ch[arr[DN]]:       # 자손들 값을 채워준 후 부모 노드가 있다면(중간 -1인 경우 2번쨰 루트이기 떄문에 부모가 없다)
    ch[arr[DN]].remove(DN)  # 해당 부모 노드에서 자신을 제거해준 후
print(ch.count([]))         # 전체 ch 배열에서 자식 노드가 없는 노드들을 세어준다

#---------------------------------------

# N = int(input())
# arr = list(map(int, input().split()))
# DN = int(input())

# ch1,ch2 = [0]*N, [0]*N
# E = []
# for i in range(N):
#     E.append([arr[i], i])

# for i in range(N):
#     p,c = E[i][0], E[i][1]
#     if p == -1:
#         continue
#     if ch1[p] == 0:
#         ch1[p] = c
#     else:
#         ch2[p] = c 


#----------------------------------

# def enq(z):
#     if z > N-1:
#         return
#     if ch[z]:
#         for i in ch[z]:
#             enq(i)
#     if ch[z] == []:
#         ch[z].append(1)

# N = int(input())
# arr = list(map(int, input().split()))
# DN = int(input())
# ch = [[] for _ in range(N)]

# for i in range(1, len(arr)):
#     ch[arr[i]].append(i)

# for i in range(DN, len(ch)):
#     for j in range(len(ch[i])):
#         if ch[i][0] != -1 and ch[i] != []:
#             if ch[ch[i][j]] == []:
#                 ch[ch[i][j]].append(-1)
        
            
    
# enq(DN)
# if DN == 0:
#     print(0)
# else:
#     ch[arr[DN]].remove(DN)
#     # print(ch)
#     print(ch.count([]))

# minV = 1
# for i in ch:
#     if len(i) > minV:
#         minV = len(i)
#         break
# if minV > 1:
#     enq(DN)
#     print(ch.count([]))
# else:
#     if DN == 0:
#         print(0)
#     else:
#         print(1)

#--------------------------------


# def enq(z):
#     if z > N-1:
#         return
#     if ch1[z]:
#         enq(ch1[z])
#     if ch2[z]:
#         enq(ch2[z])
#     if ch1[z] == 0:
#         ch1[z] = 1
#     if ch2[z] == 0:
#         ch2[z] = 1

# N = int(input())
# arr = list(map(int, input().split()))
# DN = int(input())

# ch1,ch2 = [0]*N, [0]*N
# E = []
# for i in range(N):
#     E.append([arr[i], i])

# for i in range(N):
#     p,c = E[i][0], E[i][1]
#     if p == -1:
#         continue
#     if ch1[p] == 0:
#         ch1[p] = c
#     else:
#         ch2[p] = c 
    
# enq(DN)
# for i in range(N):
#     if ch1[i] == DN and ch2[i] == 0:
#         ch2[i] = 1
#     elif ch1[i] == 0 and ch2[i] == DN:
#         ch1[i] = 1
# cnt = 0
# for i in range(N):
#     if ch1[i] == 0 or ch2[i] == 0:
#         cnt+=1
# print(cnt)

