# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:

        self.ans = 0
        self.targetSum = targetSum
        self.cache = {}
        self.dfs(root, 0)
        return self.ans

    def dfs(self, root, currSum):
        if root is None:
            return
        
        currSum += root.val
        
        if currSum == self.targetSum:
            self.ans += 1
        
        if currSum - self.targetSum in self.cache:
            self.ans += self.cache[currSum - self.targetSum] 
        
        if currSum in self.cache:
            self.cache[currSum] += 1
        else:
            self.cache[currSum] = 1

        self.dfs(root.left, currSum)
        self.dfs(root.right, currSum)

        self.cache[currSum] -= 1
        
    #naive 2 dfs solution
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans = 0
        self.targetSum = targetSum
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if root is None:
            return
        
        self.test(root, 0)

        self.dfs(root.left)
        self.dfs(root.right)

    def test(self, root, currSum):
        currSum += root.val

        if currSum == self.targetSum:
            self.ans += 1
            
        if root.left is None and root.right is None:
            return
        
        if root.left is not None:
            self.test(root.left, currSum)
        if root.right is not None:
            self.test(root.right, currSum)
    """  

        
