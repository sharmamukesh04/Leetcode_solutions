class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        n = len(intervals)
        i=1
        ans.append([intervals[0][0], intervals[0][1]])
        while i<n:
            start = ans[len(ans)-1][0]
            last = ans[len(ans)-1][1]
            if intervals[i][0]<=last:
                ans[len(ans)-1][1] = max(last, intervals[i][1])
            else:
                ans.append([intervals[i][0], intervals[i][1]])
            i+=1

        return ans
