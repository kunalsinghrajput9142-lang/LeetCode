class Solution:
    def postorderTraversal(self, root):
        return root and self.postorderTraversal(root.left) + \
               self.postorderTraversal(root.right) + [root.val] or []
               