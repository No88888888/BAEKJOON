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

N, M = map(int, input().split())
drug = [[] for _ in range(N)]
par = [[] for _ in range(N)]
res = N
for i in range(M):
    x, y = map(str, input().split())
    drug[ord(x)-65].append(ord(y)-65)
    par[ord(y)-65].append(ord(x)-65)
print(drug)
print(par)

# arrest = []
temp = list(input().split())
narcos = temp[1:]
arrest_num = int(temp[0])

for j in range(arrest_num):
    print(ord(narcos[j])-65)
    if par[ord(narcos[j])-65] == []:
        for k in range(len(drug[ord(narcos[j])-65])):
            print(drug[ord(narcos[j])-65][k])
            print(par[drug[ord(narcos[j])-65][k]])
            par[drug[ord(narcos[j])-65][k]].remove(narcos)
print(par)
    
    
#     if par[ord(narcos[k])-65] == []:
#         res += 1
#     arrest.append(ord(narcos[k]) - 65)
# # print(res)
# # print(arrest)
# for j in narcos:
#     stack = []
#     stack.append(ord(j)-65)
#     while stack:
#         v = stack.pop(0)
#         if drug[v]:
#             for w in drug[v]:
#                 if w not in arrest:
#                     arrest.append(w)
#                     stack.append(w)
# print(arrest)
# res -= len(arrest)
# res -= par.count([])
# print(res)