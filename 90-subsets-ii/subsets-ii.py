class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        temp = []
        nums.sort()
        n=len(nums)
        def helper(i):
            if i==n:
                ans.append(temp[:])
                return
            temp.append(nums[i])
            helper(i+1)
            temp.pop()
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            helper(i+1)
        helper(0)
        return ans