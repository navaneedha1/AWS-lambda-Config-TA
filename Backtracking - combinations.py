class comb:
  def combine(self, n, k):
    res = []
    self.dfs(range(1, n + 1), k, 0, [], res)
    return res


  def dfs(self, nums, k, index, path, res):
    # if k < 0:  #backtracking
    # return
    if k == 0:
        res.append(path)
        return  # backtracking
    for i in range(index, len(nums)):
        self.dfs(nums, k - 1, i + 1, path + [nums[i]], res)


if __name__ == '__main__':
    ob1 = comb()
    out1 = ob1.combine(4,2)
    print(out1)