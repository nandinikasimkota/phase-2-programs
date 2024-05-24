class Solution:
    def findInorderSuccessor(self, root):
        while root.left != None:
            root = root.left 
        return root.val
 
    def deleteNode(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None 
        elif root.val > val:
            root.left = self.deleteNode(root.left, val)
        elif root.val < val:
            root.right = self.deleteNode(root.right, val)
        else:
            if root.left == None and root.right == None:
                return None 
            elif root.left == None:
                return root.right 
            elif root.right == None:
                return root.left 
            else:
                successor = self.findInorderSuccessor(root.right)
                root.val = successor 
                root.right = self.deleteNode(root.right, successor)
        return root