class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__prev = None
        self.__next = None

    # 소멸자: 객체가 사라지기 전 반드시 호출된다.
    # 삭제 확인용
    def __del__(self):
        print(f"data of {self.data} is deleted")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, p):
        self.__prev = p

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next = n


class DoubleLinkedList:
    def __init__(self):
        # 리스트의 맨 처음과 마지막은 실제 데이터를
        # 저장하지 않는 노드이다. 이를 더미 노드라고 한다.
        self.head = Node()
        self.tail = Node()

        # 초기화
        self.head.next = self.tail
        self.tail.prev = self.head
        # 데이터 개수를 저장할 변수
        self.d_size = 0

    # 비어 있으면 True
    def empty(self) -> bool:
        if self.d_size == 0:
            print("리스트가 비어 있습니다.")
            return True
        return False

    # 요소 개수 반환
    def size(self):
        print(f"data size: {self.d_size}")
        return self.d_size

    # data를 리스트의 맨 앞에 추가
    def add_first(self, data):
        print(f"데이터 삽입 - add_first")
        # 새로운 노드 생성
        new_node = Node(data)

        # next는 더미 노드의 다음 노드, 즉 첫 번째 데이터 노드를 가리키도록 한다.
        new_node.next = self.head.next
        # prev는 리스트의 맨 앞 더미를 가리키도록 한다.
        new_node.prev = self.head

        # 첫 번째 데이터 노드의 prev가 새로운 노드를 가리키도록 하고
        self.head.next.prev = new_node
        # 더미 노드의 next는 새로운 노드를 가리켜 새로운 노드가 삽입되었다.
        self.head.next = new_node

        self.d_size += 1
        print(f"data size : {self.d_size}")

    def add_last(self, data):
        print(f"데이터 삽입 - add_last")
        # 새로운 노드 생성
        new_node = Node(data)

        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

        self.d_size += 1
        print(f"data size : {self.d_size}")

    def insert_after(self, data, node):
        new_node = Node(data)

        new_node.next = node.next
        new_node.prev = node

        node.next.prev = new_node
        node.next = new_node

        self.d_size += 1
        print(f"data size : {self.d_size}")

    def insert_before(self, data, node):
        new_node = Node(data)

        new_node.next = node
        new_node.prev = node.prev

        node.prev.next = new_node
        node.next = new_node

        self.d_size += 1
        print(f"data size : {self.d_size}")

    def search_forward(self, target) -> Node:
        print("데이터 탐색")
        # 데이터 노드를 순회할 cur 변수
        # 첫 번째 노드부터 시작하므로 self.head.next를 가리킨다.
        cur = self.head.next

        # 마지막 요소까지 반복
        # 리스트의 마지막 노드가 더미 노드이므로
        # 더미 노드가 아니라면 아직 데이터 노드이다.
        while cur is not self.tail:
            if cur.data == target:
                print(f"데이터 {target} 탐색 성공")
                return cur
            # 다음 노드로 이동
            cur = cur.next

        return None

    def search_backward(self, target) -> Node:
        print("데이터 탐색")
        cur = self.tail.prev

        while cur is not self.head:
            if cur.data == target:
                print(f"데이터 {target} 탐색 성공")
                return cur
            # 이전 노드로 이동
            cur = cur.prev

        return Node

    def delete_first(self):
        if self.empty():
            return

        # head의 다음 노드를 지정하고
        self.head.next = self.head.next.next
        # 지정한 다음 노드의 이전 노드를 head로 지정
        self.head.next.prev = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            return

        # tail의 이전 노드를 지정하고
        self.tail.prev = self.tail.prev.prev
        # 지정한 이전 노드의 다음 노드를 tail로 지정
        self.tail.prev.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        self.d_size -= 1

