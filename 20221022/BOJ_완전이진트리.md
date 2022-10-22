## [BOJ9934 / 완전 이진 트리]

### 문제

- 중위 순회 결과값을 보고 완전 이진 트리를 구현할 수 있어야 한다.
- 이때, 각 층마다 노드 수가 꽉 차 있다.



### 내가 생각해준 방법

- 중위 순회의 원리를 알아야 한다.

  => 중위 순회는 **각 노드들의 왼쪽 노드들을 모두 순회 -> 해당 노드 -> 오른쪽 노드들을 모두 순회**



### 내가 짠 코드

(원리)

- 항상 중간 값이 해당 노드
- 중간 값의 왼쪽 값들이 왼쪽 노드들
- 중간 값의 오른쪽 값들이 오른쪽 노드들

```python
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
```
