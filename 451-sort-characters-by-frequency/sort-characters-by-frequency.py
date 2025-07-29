class Solution:
    def frequencySort(self, s: str) -> str:
        mpp = {}
        for i in range(len(s)):
            if s[i] in mpp:
                mpp[s[i]]+=1
            else:
                mpp[s[i]]=1

        sorted_dict = sorted(mpp.items(), key=lambda item: item[1], reverse=True)

        ans = ""
        for key, value in sorted_dict:
            ans += key * value
        return ans
