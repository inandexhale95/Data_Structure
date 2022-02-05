from queue import Queue

class Graph:
    def __init__(self, vertex_num):
        self.vtx_num = vertex_num
        # 인접 리스트로 구현
        self.adj_list = [[] for _ in range(vertex_num)]
        #방문 여부 체크
        self.visited = [False for _ in range(vertex_num)]
        
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False
            
    def adj(self):
        for i in range(self.vtx_num):
            print(f"[{i}] : {self.adj_list[i]}")
            
    def bfs(self, v):
        q = Queue()
        # 방문 체크 리스트를 초기화 한다.
        self.init_visited()
        
        # 첫 번째 정점을 큐에 넣고, 방문 체크
        q.put(v)
        self.visited[v] = True
        
        while not q.empty():
            v = q.get()
            # 방문
            print(v, end=' ')
            # 인접 리스트를 얻어 온다.
            adj_v = self.adj_list[v]
            for u in adj_v:
                if not self.visited[u]:
                    q.put(u)
                    self.visited[u] = True
                    

g = Graph(vertex_num=5)

g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)

g.add_edge(2, 3)
g.add_edge(3, 4)

g.bfs(2)

print()

g.adj()