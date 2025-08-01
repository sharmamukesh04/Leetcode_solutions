# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, root: Optional[TreeNode], ans: []) -> None:
        if not root:
            return 

        ans.append(root.val)
        self.helper(root.left, ans)
        self.helper(root.right, ans)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        self.helper(root, ans)

        return ans