class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans = [x for x in nums]
        neg = 1
        pos = 0

        for i in range(len(nums)):
            if nums[i]>0:
                ans[pos] = nums[i]
                pos+=2
            else:
                ans[neg] = nums[i]
                neg+=2
        return ans

