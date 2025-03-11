# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []
        fringe = [(root, 0)]
        visited = set()

        while len(fringe) > 0:
            currNode, depth = fringe.pop(0)

            if currNode is None:  # Ensure we don't process None values
                continue
                
            #check if it's rightmost
            if len(fringe) == 0 or depth != fringe[0][1]:
                ans.append(currNode.val)

            if currNode not in visited:
                visited.add((currNode, depth))

                if currNode.left:
                    fringe.append((currNode.left, depth + 1))
                
                if currNode.right:
                    fringe.append((currNode.right, depth + 1))
        return ans

