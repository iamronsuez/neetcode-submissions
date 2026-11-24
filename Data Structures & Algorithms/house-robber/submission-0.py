class Solution:
    def rob(self, nums: List[int]) -> int:
        prev, curr = 0, 0          # mejor botín hasta dos casas atrás / hasta la anterior
        for value in nums:
            prev, curr = curr, max(curr, prev + value)
            #                     saltar  robar
        return curr