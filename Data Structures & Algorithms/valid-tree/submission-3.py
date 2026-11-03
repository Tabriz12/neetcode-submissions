from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        visited = set()

        adj = [[] for _ in range(n)]

        for u, v in edges:

            adj[u].append(v)
            adj[v].append(u)
        

        q = deque([(0,0)])



        while q:

            u, p = q.popleft()

            if u in visited: return False

            visited.add(u)


            for nei in adj[u]:

                if nei == p:
                    continue

                q.append((nei, u))
            
        
        return len(visited) == n

                




        