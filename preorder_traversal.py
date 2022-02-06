from stack import Stack
from treeNode import TreeNode

def preorder(cur):
    # 현재 노드가 empty node라면
    if not cur:
        return

    # 방문
    print(cur.data, end=' ')
    # 왼쪽 서브 트리로 이동
    preorder(cur.left)
    # 오른쪽 서브 트리로 이동
    preorder(cur.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

n1.left = n2
n1.right = n3

n2.left = n4
n2.right = n5

n3.left = n6
n3.right = n7

preorder(n1)