'''
문제
n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n(1 ≤ n ≤ 100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.

출력
첫째 줄에 프리오더를 출력한다.
'''
# 구글링 1
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def find_tree(l_in, r_in, l_post, r_post):
    if l_in > r_in or l_post > r_post:
        return

    root = post_order[r_post]   # r_post는 후위 순회의 결과 중 가장 마지막으로 방문한 노드를 가리키고 있기 때문에 이를 활용하여 루트 노드를 구한다.
    print(root, end=' ')        # 전위순회이기 때문에 구한 루트 노드를 바로 출력한다.
    idx = position[root]        # 루트 노드가 중위 순회에서 몇 번째로 방문했는지를 찾아 idx에 저장하고
    count = idx - l_in          # idx를 기준으로 왼쪽 서브트리에는 몇 개의 노드가 있는지 count에 저장한다

    # 왼쪽 서브트리 
    find_tree(l_in, idx - 1, l_post, (l_post + count) - 1)  # idx와 count를 활용하여 왼쪽 서브트리와 오른쪽 서브트리를 구한다.
    # 오른쪽 서브트리
    find_tree(idx + 1, r_in, l_post + count, r_post - 1)    # 중위 순회와 후위 순회의 범위를 맞춰주어야 한다.
    
N = int(input())
in_order = list(map(int, input().split()))  # 중위순회 입력
post_order = list(map(int, input().split()))# 후위순회 입력
position = [0 for _ in range(N+1)]          # 중위순회 시 특정 노드의 방문 순서를 담을 배열

for i in range(N):
    position[in_order[i]] = i               # position을 활용하여 루트 노드를 기준으로 왼쪽 서브트리와 오른쪽 서브트리를 나누는데 사용된다.

find_tree(0, N-1, 0, N-1)

# 구글링 2
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def preorder(inStart, inEnd, postStart, postEnd):
    if inStart > inEnd or postStart > postEnd:
        return
    
    root = postorder[postEnd]
    
    leftNode = position[root] - inStart
    rightNode = inEnd - position[root]
    
    print(root, end=' ')
    preorder(inStart, inStart+ leftNode - 1, postStart, postStart + leftNode - 1)
    preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

position = [0] * (N+1)
for i in range(N):
    position[inorder[i]] = i
preorder(0, N-1, 0, N-1)


