class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        for i in range(len(strs[0])):
            for j in range(0,len(strs)):
                if strs[j][i]!=strs[0][i]:
                    return strs[0][:i]
        return strs[0]