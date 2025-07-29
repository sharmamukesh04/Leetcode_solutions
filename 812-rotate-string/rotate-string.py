class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        new_s = s+s
        return True if new_s.find(goal)>=0 else False