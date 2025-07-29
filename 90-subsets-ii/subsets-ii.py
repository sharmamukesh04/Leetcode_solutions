class Solution:
    def helper(self, i, nums, temp, ans):
        if i>=len(nums):
            ans.append(temp[:])
            return
        
        temp.append(nums[i])
        self.helper(i+1, nums, temp, ans)
        temp.pop()
        while i+1<len(nums) and nums[i]==nums[i+1]:
            i+=1
        self.helper(i+1, nums, temp, ans)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.helper(0, nums, [], ans)
        return ans