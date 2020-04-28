class Solution3():
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return
        for i in range(index, len(nums)):
             self.dfs(nums, target - nums[i], i, path + [nums[i]], res)

if __name__ == '__main__':
    nums = [2, 3, 6, 7]
    s = Solution3()
    result = s.combinationSum(nums, 7)
    print(result)
