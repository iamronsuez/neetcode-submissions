class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right, best = 0, len(heights) - 1, 0

        while (left < right):
            best = max(min(heights[left], heights[right]) * (right - left), best)
            if heights[left] <  heights[right]:
                left +=1
            else:
                right -=1
        return best     