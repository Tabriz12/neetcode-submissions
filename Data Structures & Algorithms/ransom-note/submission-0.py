from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r, m = Counter(ransomNote), Counter(magazine)

        for k, v in r.items():

            if k not in m or m[k] < v:
                return False

        
        return True


        