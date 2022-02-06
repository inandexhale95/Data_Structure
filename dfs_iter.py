from stack import Stack

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
            
    def iter_dfs(self, v):
        """
        시작 정점으로 돌아가 
        더 이상 방문할 정점이 없어야 종료
        """
        s = Stack()
        self.init_visited()

        s.push(v)
        # 방문 체크 및 방문
        self.visited[v] = True
        print(v, end=' ')

        while not s.empty():
            # 아직 방문하지 않은 정점을 방문했는가
            is_visited = False
            v = s.peek()

            adj_v = self.adj_list[v]
            for u in adj_v:
                if not self.visited[u]:
                    s.push(u)
                    self.visited[u] = True
                    print(u, end=' ')

                    is_visited = True
                    break

            if not is_visited:
                s.pop()


g = Graph(4)

g.add_edge(2, 1)
g.add_edge(2, 3)

g.add_edge(1, 0)

g.iter_dfs(2)
