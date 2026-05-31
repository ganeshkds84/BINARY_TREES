from collections import deque
class TreeNode:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
class Solution:
    def rightView(self,root):
        if root is None:
            return []
        nodes=[]
        q=deque()
        q.append(root)
        while q:
            size=len(q)
            level=[]
            for i in range(size):
                node=q.popleft()
                level.append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            nodes.append(level[-1])
        return nodes
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    
    node1.left,node1.right=node2,node3
    node2.right=node4
    node4.right=node5
    
    Ashu=Solution()
    print(Ashu.rightView(node1))