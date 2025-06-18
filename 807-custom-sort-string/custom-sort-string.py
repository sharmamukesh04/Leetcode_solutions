class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mpp = {}
        for ch in s:
            if ch not in mpp:
                mpp[ch] = 1
            else:
                mpp[ch]+=1

        ans = ""
        for ch in order:
            if ch in mpp:
                ans=ans+ch*mpp[ch]
            mpp[ch]=0
        
        print("ans is ", ans)
        for i in s:
            if mpp[i]>0:
                ans+=i
        return ans

