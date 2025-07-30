class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        temp = []
        ans = []
        n = len(candidates)
        def helper(i,target):
            if target == 0:
                ans.append(temp[:])
                return 
            if target<0:
                return

            for j in range(i, len(candidates)):
                temp.append(candidates[j])
                helper(j, target-candidates[j])
                temp.pop()

        helper(0, target)
        return ans