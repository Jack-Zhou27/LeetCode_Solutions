# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            #0 children
            if not root.left and not root.right:
                return None
            
            #1 children
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            #2 children
            smallestNodeInRightTree = root.right
            while smallestNodeInRightTree.left:
                smallestNodeInRightTree = smallestNodeInRightTree.left
            root.val = smallestNodeInRightTree.val
            #pass in subtree u want the node deleted in 
            root.right = self.deleteNode(root.right, smallestNodeInRightTree.val)
        return root
