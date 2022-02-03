class CircleQueueMod:
    def __init__(self, queue_size=16):
        self.container = [0] * queue_size
        self.__front = 0
        self.__rear = 0

    def mod(self, x):
        return (x + 1) % len(self.container)

    def is_empty(self):
        if self.__front == self.__rear:
            return True
        return False

    def is_full(self):
        if self.mod(self.__rear) == self.__front:
            return True
        return False

    def enqueue(self, data):
        # if self.is_full():
        #     raise Exception("큐가 가득 찼습니다.")
        self.container[self.__rear] = data
        self.__rear = self.mod(self.__rear)

    def dequeue(self):
        if self.is_empty():
            raise Exception("큐가 비어 있습니다.")
        data = self.container[self.__front]
        self.__front = self.mod(self.__front)
        return data

    def peek(self):
        # if self.is_empty():
        #     raise Exception("큐가 가득 찼습니다.")
        return self.container[self.__front]


test = CircleQueueMod(5)

for i in range(5):
    test.enqueue(i)

test.enqueue(10)
test.enqueue(12)

for i in test.container:
    print(i, end=' ')