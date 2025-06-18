class Solution:

    def helper(self, i, ans, nums):
        if i==len(nums):
            ans.append(nums[:])
            return 
        
        for idx in range(i, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            self.helper(i+1, ans, nums)
            nums[i], nums[idx] = nums[idx], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=1:
            return [nums]
        
        ans = []
        self.helper(0, ans, nums)

        return ans