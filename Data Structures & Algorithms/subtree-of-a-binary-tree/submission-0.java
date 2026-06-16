/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {  
    public boolean isSubtree(TreeNode root, TreeNode subRoot) {
        // going down thre tree and looking for a subtree thats the same as the given subtree
        if (subRoot == null) return true;
        
        if (root == null) return false;

        if (isSameTree(root, subRoot)) {
            return true;
        } 

        return isSubtree(root.right, subRoot) || isSubtree(root.left, subRoot);

        
    }

    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;

        if (p != null && q != null && p.val == q.val) {
            return isSameTree(p.right, q.right) && isSameTree(p.left, q.left);
        }

        return false;
    }
}
