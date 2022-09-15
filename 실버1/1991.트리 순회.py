'''
문제
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.



예를 들어 위와 같은 이진 트리가 입력되면,

전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)
가 된다.

입력
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다. 둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

출력
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
'''
# 딕셔너리를 안쓰고 싶었지만 못했음
# 입력을 받아오는 것이 어려웠음

def preorder(n):             # 전위 순회
    if n:
        print(n, end='')
        preorder(ch1[A[n]])
        preorder(ch2[A[n]])

def inorder(n):             # 중위 순회
    if n:
        inorder(ch1[A[n]])
        print(n, end='')
        inorder(ch2[A[n]])

def postorder(n):           # 후위 순회
    if n:
        postorder(ch1[A[n]])
        postorder(ch2[A[n]])
        print(n, end='')
        
N = int(input())                # 노드 개수
arr = sorted(list(input().split() for _ in range(N)))   # 트리 정보

A = {}
for i in range(1, 27):
    A[chr(i+64)] = i        # 알파벳과 정수 매핑('A' : 1)

ch1, ch2 = [0]*(N+1), [0]*(N+1) # 자식
par = [0]*(N+1)                 # 부모

for i in range(N):              # 자식 부모 정보 저장
    for j in range(3):
        p, pw = i+1, arr[i][0]
        cw = arr[i][j]
        if cw != '.':
            c = A[cw]
        if j == 1 and cw != '.':
            ch1[p] = cw
            par[c] = pw
        if j == 2 and cw != '.':
            ch2[p] = cw
            par[c] = pw
                
preorder('A')
print()
inorder('A')
print()
postorder('A')
