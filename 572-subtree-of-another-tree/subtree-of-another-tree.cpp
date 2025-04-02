/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSimilar(TreeNode* a, TreeNode* b){
        if(!a && !b) return true;
        if(!a || !b) return false;
        if(a->val!=b->val) return false;

        return isSimilar(a->left,b->left) && isSimilar(a->right,b->right);
    }
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!root && !subRoot) return true;
        if(!root || !subRoot) return false;
        bool checkSimilar = isSimilar(root,subRoot);
        if(checkSimilar) return true;

        return isSubtree(root->left,subRoot) || isSubtree(root->right,subRoot);
    }
};