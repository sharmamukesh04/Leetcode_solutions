class Solution:
    def largestOddNumber(self, num: str) -> str:
        find_end = len(num)-1
        while find_end>=0:
            if int(num[find_end])%2:
                found = True
                break
            find_end-=1
        return num[:find_end+1]