# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        largest = -float('inf')
        tempVal = 0
        tempDepth = 1
        ans = 1

        fringe = [(root, 1)]
        visited = set()

        while len(fringe) > 0:
            currNode, depth = fringe.pop(0)

            if not currNode:
                continue
            
            #update ans
            if depth != tempDepth:
                tempDepth = depth

                #update you depth after you finished traversing a level
                if tempVal > largest:
                    largest = tempVal
                    ans = depth - 1

                tempVal = 0
            
            tempVal += currNode.val

            #update fringe
            if (currNode, depth) not in visited:
                visited.add((currNode, depth))

                if currNode.left:
                    fringe.append((currNode.left, depth + 1))
                if currNode.right:
                    fringe.append((currNode.right, depth + 1))
        
        #final check
        if tempVal > largest:
            ans = tempDepth

        return ans
