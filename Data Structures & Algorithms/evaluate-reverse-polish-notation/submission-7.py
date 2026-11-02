class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        total = 0
        operators = {"+", "-", "*", "/"}
        operationStack = []
        for token in tokens:
            if token not in operators:
                operationStack.append(int(token))
            else:
                _total = 0
                b = int(operationStack.pop())
                a = int(operationStack.pop())
                if token == "+":
                    _total = a + b
                if token == "-":
                    _total = a - b
                if token == "*":
                    _total = a * b
                if token == "/":
                    _total = a / b
                operationStack.append(int(_total))

        return operationStack[0]