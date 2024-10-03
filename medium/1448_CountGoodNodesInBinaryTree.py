# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:

    numGoodNodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(root, currMax):
            if root == None:
                return
            if root.val >= currMax:
                self.numGoodNodes += 1
                currMax = root.val
            dfs(root.left, currMax)
            dfs(root.right, currMax)
        
        dfs(root, root.val)
        return self.numGoodNodes
