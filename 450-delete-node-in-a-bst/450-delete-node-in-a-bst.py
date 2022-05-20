# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root == None:
            return root
        
        if root.val == key:
            # do something
            if not root.left and not root.right:
                root = None
                
            elif not root.left:
                return root.right
            
            elif not root.right:
                return root.left
            
            else:
                temp = self.find_successor(root.right)
                root.val = temp.val
                root.right = self.deleteNode(root.right, root.val)
                
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
                
        return root
    
    def find_successor(self, root):
        while root.left:
            root = root.left
            
        return root 
            