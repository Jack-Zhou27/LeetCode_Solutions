# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        #init
        graph = defaultdict(list) #graph is based on values!

        def build_graph(root):
            if not root:
                return
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                build_graph(root.right)
        
            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                build_graph(root.left)
            
        build_graph(root)

        
        #bfs
        ans = []
        fringe = []
        fringe.append((target.val, 0)) #(node val, dist)
        visited = set()
        visited.add(target.val)
        
        while fringe:
            val, dist = fringe.pop(0)
            if dist == k:
                ans.append(val)
            elif dist < k:
                for neighbor in graph[val]:
                    if neighbor in visited:
                        continue
                    else:
                        fringe.append((neighbor, dist + 1))
                        visited.add(neighbor)
        #algo
        return ans
        
