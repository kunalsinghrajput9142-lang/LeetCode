class Solution:
    def countNodes(self,root):
        if not root:
            return 0
        l,r=self.getHeight(root.left),self.getHeight(root.right)
        return(1<<l)+self.countNodes(root.right)if l==r\
        else(1<<r)+self.countNodes(root.left)

    def getHeight(self,node):
        h=0
        while node:
            h+=1
            node=node.left
        return h   