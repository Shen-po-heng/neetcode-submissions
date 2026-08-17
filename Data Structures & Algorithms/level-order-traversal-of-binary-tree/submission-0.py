# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        queue = [root]
        result = []

        while queue:
            level = []

            # 記住這一層有幾個 node
            level_size = len(queue)

            for _ in range(level_size):
                # 從 queue 前面拿一個 node
                node = queue.pop(0)
                # 把 node.val 放進 level
                level.append(node.val)
                # 有 left → 放進 queue
                if node.left:
                    queue.append(node.left)
                # 有 right → 放進 queue
                if node.right:
                    queue.append(node.right)
            result.append(level)

        return result