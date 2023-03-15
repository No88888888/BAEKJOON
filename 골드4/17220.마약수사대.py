'''
문제
최근들어 세계적으로 마약과 관련한 사회적 문제들이 많이 발생하고 있다. 이에 따라 경찰은 마약 수사대의 한정된 인력이 허용하는 선에서 최대한 마약공급을 막고자 한다.

마약 공급책들은 서로에게 마약을 공급받는데, 최근 마약수사대는 마약 공급책들 간의 관계도를 일부 파악하였다. 이 관계도는 그래프로 표현될 수 있다. 각 노드는 마약 공급책, 간선은 공급 관계를 표현한다. 예를 들어 아래와 같은 그래프는 다음을 나타낸 것이다.

마약공급책 A가 마약 공급책 B, C, D, E 에게 마약을 공급한다.
마약공급책 F는 B와 C로부터 마약을 공급받아서 I에게 공급한다.
I는 J에게, J는 K에게, D는 G에게, E는 H에게 각각 마약을 공급한다.


마약수사대는 소재를 파악하고 있는 마약 공급책을 검거할 수 있다.

예를 들어, 마약수사대가 B와 C를 검거해도 D, E, G, H는 여전히 마약을 공급받을 수 있다.

마약의 원산지는 '다른 공급책에게 공급받지 않으면서 마약을 공급하는 마약공급책'이다.

마약 공급책들의 관계도에 대한 정보와 마약수사대가 검거한 마약 공급책들이 주어졌을 때 여전히 마약을 공급 받을 수 있는 마약 공급책의 수를 내어주는 프로그램을 작성해보자.

입력
첫 번째 줄에 마약 공급책의 수 N(1 ≤ N ≤ 26)과 마약 공급책의 관계 수 M(1 ≤ M ≤ 600)이 주어진다. 각 마약 공급책은 A부터 순서대로 알파벳 대문자로 표현된다.

두번째 줄부터 M개의 줄에 각 마약 공급책의 관계가 주어진다. (A B : A -> B)

마지막 줄에 경찰이 소재를 파악하고 있는 마약 공급책들의 수와 파악중인 각 마약 공급책이 공백으로 구분되어 주어진다.

출력
마약수사대가 파악중인 마약 공급책을 검거한 후 여전히 마약을 공급 받는 마약 공급책의 수를 출력한다.
'''
import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
ch = [[] for _ in range(N)]             # 내가 마약 공급해주는 사람 리스트   (자식 )
par = [[] for _ in range(N)]            # 나한테 마약 공급해주는 사람 리스트 (부모 )
res = N
for i in range(M):
    x, y = map(str, input().split())
    ch[ord(x)-65].append(ord(y)-65)     # 자식 정보를 int로 변환하여 저장(A:0, B:1 ...)
    par[ord(y)-65].append(ord(x)-65)    # 부모 "

temp = list(input().split())            # 체포당한 사람 정보
arrest_num = int(temp[0])               # 체포당한 사람 수
arrest = []
for t in temp[1:]:
    arrest.append(ord(t)-65)            # 체포당한 사람 정보를 int로 변환하여 저장

stack = deque(arrest[:])
while stack:                            # bfs로 공급받는 사람들 다 잡기                    
    v = stack.popleft()
    par[v] = []                         # 일단 체포당한사람을 마약공급책에서 삭제
    for w in ch[v]:                     # 자식들을 확인
        if w not in arrest:             # 해당 자식이 아직 체포 당하지 않았다면
            par[w].remove(v)            # 마약 공급책에서 삭제
            if par[w] == []:            # 해당사람에게 공급해주는 다른 마약공급책이 없다면
                arrest.append(w)        # 체포하고
                stack.append(w)         # 다음 자식 확인 위해 인스택
res -= par.count([])                    # 전체 숫자에서 체포당한 마약공급책 + 마약 원산지 숫자를 뺀 나머지
print(res)

# for j in range(arrest_num):
#     print(ord(arrest[j])-65)
#     if par[ord(arrest[j])-65] == []:
#         for k in range(len(ch[ord(arrest[j])-65])):
#             print(ch[ord(arrest[j])-65][k])
#             print(par[ch[ord(arrest[j])-65][k]])
#             par[ch[ord(arrest[j])-65][k]].remove(ord(arrest[k])-65)
# print(par)
    
    
#     if par[ord(arrest[k])-65] == []:
#         res += 1
#     arrest.append(ord(arrest[k]) - 65)
# # print(res)
# # print(arrest)
# for j in arrest:
#     stack = []
#     stack.append(ord(j)-65)
#     while stack:
#         v = stack.pop(0)
#         if ch[v]:
#             for w in ch[v]:
#                 if w not in arrest:
#                     arrest.append(w)
#                     stack.append(w)
# print(arrest)
# res -= len(arrest)
# res -= par.count([])
# print(res)