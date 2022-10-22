import sys
sys.stdin = open('0_BOJ_완전이진트리.txt', 'r')

n = int(input())
nodes = list(map(int, input().split()))

#n개 층의 tree를 생성
tree = [[] for _ in range(n)]

def inorder_reversal(start, end, k):
    #순회하는 곳의 첫 값과 끝 값이 같다면, 
    # => 즉, 노드가 하나 뿐이라면, 방문한 노드를 출력하고 순회를 마친다.
    if start == end:
        tree[k].append(nodes[start])
        return

    #순회하는 곳의 가장 중간 값을 트리의 k층에 append 해준다.
    mid = (start + end) // 2
    tree[k].append(nodes[mid])

    #부모노드의 왼쪽 노드들을 순회한다.
    inorder_reversal(start, mid-1, k+1)
    #부모노드의 오른쪽 노드들을 순회한다.
    inorder_reversal(mid+1, end, k+1)

#중위 순회의 결과값을 통해 완전이진트리를 구상한다.
inorder_reversal(0, len(nodes)-1, 0)

for t in tree:
    print(*t)