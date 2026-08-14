# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def  dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(self.dfs(root.left), self.dfs(root.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_height = self.dfs(root.left)
        right_height = self.dfs(root.right)
        left_to_right = left_height + right_height
        biggest_diameter_in_sons = max(self.diameterOfBinaryTree(root.left),
                            self.diameterOfBinaryTree(root.right))

        return max(left_to_right, biggest_diameter_in_sons)
