from collections import deque
class Solution:


    def diff_is_one(self, a, b):

        diff = 0

        for i in range(len(a)):

            if a[i] != b[i]:

                if not diff: diff = 1

                else: return False
        
        return True



    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0


        visited = set()

        wordList.insert(0,endWord)

        step = 0

        q = deque([beginWord])

        while q:

            for _ in range(len(q)):

                ref = q.popleft()

                if self.diff_is_one(ref, endWord):
                    return step+2

                for word in wordList:

                    if word in visited:
                        continue
                    
                    if self.diff_is_one(ref, word):

                        visited.add(word)

                        q.append(word)
            
            step+=1
        

        return 0
        