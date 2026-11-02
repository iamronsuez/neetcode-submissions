class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        n = len(temperatures)
        stack = []

        for ix, value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                diff =  ix - stack[-1][1]
                answer[stack[-1][1]] = diff
                stack.pop()
            else:
                stack.append([value, ix])
        return answer