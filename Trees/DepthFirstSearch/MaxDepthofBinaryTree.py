class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DFS RECURSIVE APPROACH
        #Here you are going to the each leaf,
        #then counting your way back up in both directions and taking the max depth of each direction
        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1



        if not root:
            return 0


        #ITERATIVE SOLUTION
        # stack = [(root, 1)]
        # ans = 0
        
        # while stack:
        #     node, depth = stack.pop()
        #     ans = max(ans, depth)
        #     if node.left:
        #         stack.append((node.left, depth + 1))
        #     if node.right:
        #         stack.append((node.right, depth + 1))
        
        # return ans



        #MY SHITTY SOLUTION
        # if root is None:
        #     return 0
        # # Use lists to simulate nonlocal variables
        # maxDepth = [0]
        # curr = [0]
        # def dfs(node):
        #     if node is None:
        #         return  
        #     # Increment current depth since we're going down one level
        #     curr[0] += 1
        #     # Update maxDepth if current depth is greater
        #     maxDepth[0] = max(maxDepth[0], curr[0])
        #     # Traverse left and right subtree
        #     dfs(node.left)
        #     dfs(node.right)
        #     # Decrement current depth since we're returning to the previous level
        #     curr[0] -= 1
        
        # dfs(root)
        # return maxDepth[0]
