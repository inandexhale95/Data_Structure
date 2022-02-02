class CircleQueue:
    MAXSIZE = 10

    def __init__(self):
        self.container = [None for _ in range(CircleQueue.MAXSIZE)]
        self.front = 0
        self.rear = 0

    def is_empty(self):
        if self.front == self.rear:
            return True
        return False

    # front나 rear를 뒤로 이동했을 때 동적 배열을 벗어난다면
    # 동적 배열의 맨 처음으로 이동시킨다.
    def __step_forward(self, x):
        x += 1
        if x >= CircleQueue.MAXSIZE:
            x = 0
        return x

    def is_full(self):
        next = self.__step_forward(self.rear)
        if next == self.front:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            raise Exception("큐가 가득 찼습니다.")
        self.container[self.rear] = data
        self.rear = self.__step_forward(self.rear)

    def dequeue(self):
        if self.is_empty():
            raise Exception("큐가 비어 있습니다.")
        data = self.container[self.front]
        self.front = self.__step_forward(self.front)
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("큐가 비어 있습니다.")
        return self.container[self.front]
