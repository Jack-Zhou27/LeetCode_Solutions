# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        #algorithm
        def dfs(root, leaves):
            if root == None:
                return
            if root.left == root.right == None:
                leaves.append(root.val)
                return
            dfs(root.left, leaves)
            dfs(root.right, leaves)
            return leaves

        #create two lists
        leaves1 = []
        leaves2 = []
        dfs(root1, leaves1)
        dfs(root2, leaves2)

        #check if arrays are equal
        if(len(leaves1) != len(leaves2)):
            return False

        for i, j in zip(leaves1, leaves2):
            if i != j:
                return False

        return True
      
        
        
