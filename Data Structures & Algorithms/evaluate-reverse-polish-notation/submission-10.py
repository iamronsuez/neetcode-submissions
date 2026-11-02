class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        operationStack = []
        for token in tokens:
            if token not in operators:
                operationStack.append(int(token))
            else:
                _total = 0
                b = operationStack.pop()
                a = operationStack.pop()
                if token == "+":   operationStack.append(a + b)
                elif token == "-": operationStack.append(a - b)
                elif token == "*": operationStack.append(a * b)
                elif token == "/": operationStack.append(int(a / b))

        return operationStack[0]