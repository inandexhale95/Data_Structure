from queue import Queue

def levelorder(cur):
    q = Queue()

    q.put(cur)
    while not q.empty():
        cur = q.get()

        # 방문
        print(cur.data, end=' ')
        # 현재 노드의 왼쪽 자식이 있다면 큐에 추가
        if cur.left:
            q.put(cur.left)
        # 현재 노드의 오른쪽 자식이 있다면 큐에 추가
        if cur.right:
            q.put(cur.right)