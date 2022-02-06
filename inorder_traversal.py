from treeNode import TreeNode

def inorder(cur):
    # 현재 노드가 empty node면
    if not cur:
        return

    # 왼쪽 서브 트리로 이동
    inorder(cur.left)
    # 방문
    print(cur.data, end=' ')
    # 오른쪽 서브 트리로 이동
    inorder(cur.right)


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

inorder(n1)