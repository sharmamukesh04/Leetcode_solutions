class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evenPos=0
        i=0
        n = len(nums)
        
        while i<n:
            if not nums[i]&1:
                nums[i],nums[evenPos] = nums[evenPos], nums[i]
                evenPos+=1
            i+=1
        
        return nums
