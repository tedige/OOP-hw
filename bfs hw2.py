class Solution:
def makeConnected(self, n: int, connections: List[List[int]]) -> int:
if len(connections) < n - 1:
return -1    graph = [[] for _ in range(n)]
    for a, b in connections:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]:
            count += 1
            q = [i]
            visited[i] = True
            while q:
                curr = q.pop(0)
                for neighbor in graph[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)
    
    return count - 1 if count > 1 else 0



    def test_make_connected():
    s = Solution()

    assert s.makeConnected(4, [[0,1],[0,2]]) == -1
    assert s.makeConnected(5, [[0,1],[1,2],[2,3],[3,4],[4,0]]) == 0
    assert s.makeConnected(6, [[0,1],[0,2],[2,3],[3,4],[1,5]]) == 1
    assert s.makeConnected(7, [[0,1],[0,2],[2,3],[3,4],[1,5],[1,6]]) == 2
