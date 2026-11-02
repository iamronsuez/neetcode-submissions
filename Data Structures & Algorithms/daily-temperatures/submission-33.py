class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        n = len(temperatures)
        stack = []

        for ix, value in enumerate(temperatures):
            while stack and stack[-1][0] < value:
                _, stack_i = stack.pop()
                diff =  ix - stack_i
                answer[stack_i] = diff
            else:
                stack.append((value, ix))
        return answer