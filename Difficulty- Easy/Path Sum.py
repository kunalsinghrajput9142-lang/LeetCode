class Solution:
    def hasPathSum(self,node,targetSum):
        if not node:
             return False
        if not node.left and not node.right:
                return node.val==targetSum
        return(
        self.hasPathSum(node.left,targetSum-node.val) or
        self.hasPathSum(node.right,targetSum-node.val))
