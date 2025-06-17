class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        curr_index = 0
        zero_index = 0
        count_non_zero = 0
        for i in range(0,len(nums)):
            if nums[i]!=0:
                if curr_index!=zero_index:
                    nums[zero_index] = nums[curr_index]
                zero_index+=1
                count_non_zero+=1
            curr_index+=1

        count_zero = len(nums)-count_non_zero

        e = len(nums)-1
        while count_zero>0:
            nums[e]=0
            e-=1
            count_zero-=1
                
                

        