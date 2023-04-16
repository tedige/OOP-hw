class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        edges_numb = len(connections)
        graph = {k: [] for k in range(n)}
        for c in connections:
            nodes_1 = graph[c[0]]
            nodes_2 = graph[c[1]]
            nodes_1.append(c[1])
            nodes_2.append(c[0])
            graph[c[0]] = nodes_1
            graph[c[1]] = nodes_2
        comp_numb = 0
        visited = [0] * len(graph)
        for k in graph:
            if visited[k] == 0:
                comp_numb += 1
                dfs(graph, k, visited)
        if edges_numb < n - 1:
            return -1
        else:
            return comp_numb - 1

def dfs(graph, s, visited):
    visited[s] = 1
    for v in graph[s]:
        if visited[v] == 0:
            dfs(graph, v, visited)


def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        v = queue.pop(0)
        if v not in visited:
            visited.add(v)
            queue.extend(graph[v] - visited)

    return visited



import unittest

class TestSolution(unittest.TestCase):
    
    def test_makeConnected1(self):
        sol = Solution()
        n = 4
        connections = [[0,1],[0,2],[1,2]]
        self.assertEqual(sol.makeConnected(n, connections), 1)
        
    def test_makeConnected2(self):
        sol = Solution()
        n = 6
        connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
        self.assertEqual(sol.makeConnected(n, connections), 2)
        
    def test_makeConnected3(self):
        sol = Solution()
        n = 6
        connections = [[0,1],[0,2],[0,3],[1,2]]
        self.assertEqual(sol.makeConnected(n, connections), -1)
        
    def test_makeConnected4(self):
        sol = Solution()
        n = 5
        connections = [[0,1],[1,2],[3,4]]
        self.assertEqual(sol.makeConnected(n, connections), 1)

if __name__ == '__main__':
    unittest.main()
