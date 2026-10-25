class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph = [[] for _ in range(n)]

        for s, d in edges:

            graph[s].append(d)
            graph[d].append(s)

        self.seen = set()

        def dfs(src):

            self.seen.add(src)

            for n in graph[src]:

                if n in self.seen:
                    continue

                dfs(n)
        

        not_seen = set([i for i in range(n)])
        k = 0
        while not_seen:

            i = not_seen.pop()

            dfs(i)

            not_seen -= self.seen

            k+=1
        
        return k
                


            
        


        

        







        
        