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
    int sumOfLeftLeaves(TreeNode* root)
    {
        int sum = 0;

        if (root == NULL)
        {
            return 0;
        }
        preOrder(root, false, sum);

        return sum;
    }

    void preOrder(TreeNode* root, bool isleft, int& sum)
    {
        if(isleft == true && root->left == NULL && root->right == NULL)
        {
            sum += root->val;
        }
        if(root->left != NULL)
        {
            preOrder(root->left, true, sum);
        }
        if(root->right != NULL)
        {
            preOrder(root->right, false, sum);
        }
    }
};