class Solution:

    def __init__(self):


        self.res = []


    def dfs(self, para, path, n):

        if len(path) == n*2 and para == '(':

            self.res.append(path)
            return
        

        elif path.count(para) == n:

            return
        
        elif para == ')' and path.count(')') == path.count('('):
            return
        

        path += para

        self.dfs('(', path, n)
        self.dfs(')', path, n)
        

    def generateParenthesis(self, n: int) -> List[str]:

        self.dfs('(', '', n)

        return self.res

        
        