'''
문제
영선이는 나무꾼으로 나무를 구하러 오전에 산에 오른다. 산에는 n개의 나무가 있는데, 영선이는 하루에 한 나무씩 n일 산에 오르며 나무를 잘라갈 것이다. 하지만 이 산은 영험한 기운이 있어 나무들이 밤만 되면 매우 빠른 속도로 자라는데, 그 자라는 길이는 나무마다 다르다.

따라서, 어느 나무를 먼저 잘라가느냐에 따라서 총 구할 수 있는 나무의 양이 다른데,

나무의 처음 길이와 하루에 자라는 양이 주어졌을 때, 영선이가 얻을 수 있는 최대 나무양을 구하시오.

참고로, 자른 이후에도 나무는 0부터 다시 자라기 때문에 같은 나무를 여러 번 자를 수는 있다.

입력
첫째 줄에는 나무의 개수 n개가 있다.(1≤n≤100,000) 나무는 1번부터 n번까지 있다.

다음 줄에는 첫날 올라갔을 때 나무의 길이들 Hi가 n개가 순서대로 주어진다.(1≤Hi≤100,000)

그 다음 줄에는 나무들이 자라는 길이 Ai가 n개가 순서대로 주어진다.(1≤Ai≤10,000)

출력
영선이가 나무를 잘라서 구할 수 있는 최대 양을 출력하시오.
'''
# 초기값을 다 더해줘버리고 성장속도 가지고 더하는 식
import sys
input = sys.stdin.readline

N= int(input())
tree = sum(list(map(int, input().split())))
zara = sorted(list(map(int, input().split())))

for i in range(N):
    tree += zara[i]*i
print(tree)

# --------------------------------------------------
# 내 본래 풀이
import sys
input = sys.stdin.readline

N= int(input())
tree = sum(list(map(int, input().split())))
zara = sorted(list(map(int, input().split())))
temp = []
jangjak = 0

for i in range(N):
    temp.append((tree[i], zara[i]))     # 나무 본래 길이, 일일 성장 길이 매핑
arr=sorted(temp, key=lambda x:x[1])     # 일일 성장 길이 기준 정렬

for j in range(N):                      # 성장 빠른 나무를 제일 마지막에 자름 
    jangjak += arr[j][0] + arr[j][1]*j  # 본래 나무 길이 + (일일 설장길이 x 일 수)
print(jangjak)                          # 최종 나무양 출력
    
# -----------------------------------------------------
# 수형이 코드
N = int(input())
tree = sorted(list(map(list, zip(*[list(map(int, input().split())) for _ in range(2)]))), key=lambda x: x[1])

sumV = 0
for i in range(N):
	sumV += tree[i][0] + (tree[i][1] * i)

print(sumV)

#pypy 3636ms 나오는 풀이
# for i in range(N):
#     m = zara.index(max(zara))
#     namu += tree[m] + zara[m]*(N-(i+1))
#     zara[m] = 0
# print(namu)

    
#     print(tree)
#     namu += max(tree)
#     print(max(tree))
#     print(namu)
#     tree[tree.index(max(tree))] = 0
#     print(tree)
#     for j in range(N):
#         tree[j] += A[j]
# print(namu)