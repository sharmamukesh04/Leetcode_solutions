class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:

        ans = []
        mpp = {}

        for l in nums1:
            if l[0] not in mpp:
                mpp[l[0]] = []

            mpp[l[0]].append(l[1])

        for l in nums2:
            if l[0] not in mpp:
                mpp[l[0]] = []

            mpp[l[0]].append(l[1])

        for key, values in mpp.items():
            sum = 0
            for num in values:
                sum+=num
            
            ans.append([key, sum])

        ans.sort()
        return ans

        