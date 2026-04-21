# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None or key is None:
            return root
        if key == root.val:
            if root.right and root.left:
                node = root.left
                while node.right:
                    node = node.right
                root.val = node.val
                root.left = self.deleteNode(root.left, root.val)
                return root
            if root.left:
                return root.left
            if root.right:
                return root.right
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        return root
