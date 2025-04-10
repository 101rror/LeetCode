/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:
    vector<int> solve(TreeNode* root, vector<int> res, int lvl) {
        if (root == NULL) {
            return res;
        }
        if (res.size() == lvl) {
            res.push_back(root->val);
        }
        res = solve(root->right, res, lvl + 1);
        res = solve(root->left, res, lvl + 1);
        return res;
    }

    vector<int> rightSideView(TreeNode* root) {
        vector<int> ans;
        ans = solve(root, ans, 0);

        return ans;
    }
};