# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root):
        self.prev = float('-inf')
        
        def inorder(node):
            if not node:
                return True
            
            if inorder(node.left) is False:
                return False
            # 左
            # 根（在這裡比較 node.val 和 self.prev）
            # 右
            if self.prev >= node.val:
                return False
            self.prev = node.val
            if inorder(node.right) is False:
                return False
            return True
        return inorder(root)