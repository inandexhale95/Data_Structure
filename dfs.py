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
            
    def dfs_recursion(self, v):
        # 방문
        print(v, end=' ')
        # 방문 체크
        self.visited[v] = True
        self.adj_v = self.adj_list[v]
        for u in self.adj_v:
            if not self.visited[u]:
                self.dfs_recursion(u)
                

g = Graph(4)

g.add_edge(2, 1)
g.add_edge(2, 3)

g.add_edge(1, 0)

g.dfs_recursion(2)