# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.count = 0
        def dfs(root, goLeft, currCount):
            #keep track of curr max count
            self.count = max(self.count, currCount)

            if not root:
                return currCount
            
            if goLeft:
                #continue with zig zag
                dfs(root.left, False, currCount + 1)

                #start new zig zag
                dfs(root.left, True, 0)
            
            else:
                dfs(root.right, True, currCount + 1)

                dfs(root.right, False, 0)

        dfs(root, True, 0)
        dfs(root, False, 0)
        return self.count - 1
