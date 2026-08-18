from collections import defaultdict, deque
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:


        conn = defaultdict(set)

        cont = defaultdict(int)


        for a, b in edges:

            conn[a].add(b)
            cont[a]+=1
            conn[b].add(a)
            cont[b]+=1
        

        q = deque()

        for node in cont.keys():

            if cont[node] == 1:

                q.append(node)
        
        
        visited = set()

        while q:

            for _ in range(len(q)):

                top = q.popleft()
                visited.add(top)


                for n in conn[top]:

                    cont[n] -=1
                    if cont[n] == 1:

                        q.append(n)
        
        
        for a,b in edges[-1::-1]:
            
            if a not in visited and b not in visited:

                return [a,b]












        
        