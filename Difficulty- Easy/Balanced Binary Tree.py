class Solution:
    def isBalanced(self,root):
        balanced=[True]
        def height(node):
            if not node:
                return 0
            left_height=height(node.left)
            if not balanced[0]:
                return 0
            right_height=height(node.right)
            if abs(left_height-right_height)>1:
                balanced[0]=False
                return 0
            return 1+max(left_height,right_height)
        height(root)
        return balanced[0]
