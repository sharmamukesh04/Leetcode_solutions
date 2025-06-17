class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        i = 0
        j = 0
        ans = []
        while i<len(nums1) and j<len(nums2):
            sum = 0
            if nums1[i][0]>nums2[j][0]:
                ans.append([nums2[j][0],nums2[j][1]])
                j+=1
            elif nums1[i][0]<nums2[j][0]:
                ans.append([nums1[i][0],nums1[i][1]])
                i+=1
            flag = False
            key = -1
            while i<len(nums1) and j<len(nums2) and nums1[i][0] == nums2[j][0]:
                flag = True
                if key !=-1 and key != nums1[i][0]:
                    break
                key = nums1[i][0]
                sum+=nums1[i][1]+nums2[j][1]
                i+=1
                j+=1
            if flag:
                ans.append([key,sum])
                flag = False
                sum = 0
        
        while i<len(nums1):
            ans.append([nums1[i][0],nums1[i][1]])
            i+=1
        
        while j<len(nums2):
            ans.append([nums2[j][0],nums2[j][1]])
            j+=1

        return ans

        