from collections import deque
class TreeNode:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
class Solution:
    def zigZag(self,root):
        if root is None:
            return []
        q=deque()
        q.append(root)
        left_to_right=True
        result=[]
        while q:
            size=len(q)
            level=[]
            for i in range(size):
                node=q.popleft()
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            if  not left_to_right:
                level.reverse()
            left_to_right=not left_to_right
            result.append(level)
        return result
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    
    node1.left,node1.right=node2,node3
    node3.left,node3.right=node4,node5
    
    Ashu=Solution()
    print(Ashu.zigZag(node1))