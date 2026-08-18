from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:




        reqs = defaultdict(set)

        dep = defaultdict(int)
        for c, r in prerequisites:

            reqs[r].add(c)

            dep[c]+=1
        

        q = deque([i for i in range(numCourses) if dep[i]==0])

        completed = 0
        
        while q:


            top = q.popleft()
            completed += 1


            for req in reqs[top]:

                dep[req] -=1

                if dep[req] == 0:

                    q.append(req)
        


        return completed == numCourses
            



        