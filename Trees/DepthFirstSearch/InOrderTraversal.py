class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        def inOrder(root):
            answer = []
            if not root:
                return []
            left = inOrder(root.left)
            right = inOrder(root.right)
            answer += left
            answer.append(root.val)
            answer += right
            return answer
            
        return inOrder(root)