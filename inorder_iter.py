from stack import Stack

def inter_order(cur):
    s = Stack()

    while True:
        while cur:
            s.push(cur)
            cur = cur.left
        cur = s.pop()
        if not cur:
            break
        # pop한 후에 방문을 한다.
        print(cur.data, end=' ')
        cur = cur.right