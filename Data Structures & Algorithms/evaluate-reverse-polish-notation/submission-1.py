class Solution:


    def operate(self, a, b, op):
        match op:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return int(a / b)  # important: truncate toward zero
            case _:
                raise ValueError("Unsupported operation")

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()
                stack.append(self.operate(a, b, token))
            else:
                stack.append(int(token))

        return stack[0]






        

