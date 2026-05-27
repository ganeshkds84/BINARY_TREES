from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    def levelOrderTraversal(self,root):
        if root is None:
            return []
        ans=[]
        q=deque()
        q.append(root)
        while q:
            level=[]
            size=len(q)
            for i in range(size):
                node=q.popleft()
                level.append(node.data)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            ans.append(level)
        return ans
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    node6=TreeNode(6)
    node7=TreeNode(7)
    
    node1.left,node1.right=node2,node3
    node2.left,node2.right=node4,node5
    node3.left,node3.right=node6,node7
    
    Ashu=Solution()
    print(Ashu.levelOrderTraversal(node1))