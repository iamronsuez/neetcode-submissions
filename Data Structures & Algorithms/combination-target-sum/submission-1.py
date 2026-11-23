class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(i, total):
            if total == target:
                res.append(path[:])          # copia de path
                return
            if total > target or i == len(nums):
                return

            # A) usar nums[i] y quedarse en i
            path.append(nums[i])
            dfs(i, total + nums[i])
            path.pop()

            # B) no usar más nums[i]
            dfs(i + 1, total)

        dfs(0, 0)
        return res