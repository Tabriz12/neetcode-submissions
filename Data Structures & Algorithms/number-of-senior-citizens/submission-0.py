class Solution:
    def countSeniors(self, details: List[str]) -> int:

        return len([d for d in details if int(d[-4:-2]) >60 ])
        