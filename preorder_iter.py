from stack import Stack

def iter_preorder(cur):
    s = Stack()

    while True:
        # 왼쪽 노드로 반복
        while cur:
            print(cur.data, end=' ')
            s.push(cur)
            cur = cur.left
        """
        pop으로 가져온 노드가
        1. None이면 스택이 비어 있는 경우, 즉 모든 노드를 순회한 경우
        2. 왼쪽 서브 트리가 없거나
        3. 왼쪽 서브 트리를 방문한 상태이다.
        """
        cur = s.pop()
        if not cur:
            break

        # 왼쪽 서브 트리를 방문했으므로 오른쪽 서브 트리를 순회한다.
        cur = cur.right