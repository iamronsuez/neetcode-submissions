class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures) - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:   # ← 1
                stack.pop()
            if stack:
                days[i] = stack[-1] - i                                   # ← 2
            stack.append(i)
        return days