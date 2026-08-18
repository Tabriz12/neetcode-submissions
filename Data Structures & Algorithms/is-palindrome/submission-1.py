class Solution:

    def clean(self, s):

        return "".join([c.lower() for c in s if c.isalnum()])
    def isPalindrome(self, s: str) -> bool:

        ss = self.clean(s)
        ln = len(ss)
        return len(ss) < 2 or (ss[:ln//2] == ss[-1:(ln-1)//2:-1])



        