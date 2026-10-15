class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        res = 0
        
        for i, n in enumerate(reversed(num1)):
            for j, m in enumerate(reversed(num2)):


                res += (10**j * int(m)) * (10**i * int(n))

        
        return str(res)
        