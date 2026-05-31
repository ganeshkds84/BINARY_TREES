from collections import deque
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def isSymmetric(self,root):
        if root is None:
            return True
        q=deque()
        q.append(root)
        while q:
            level=[]
            size=len(q)
            for i in range(size):
                node=q.popleft()
                if node is None:
                    level.append(None)
                    continue
                level.append(node.data)
                q.append(node.left)
                q.append(node.right)
            reversed_level=list(reversed(level))
            print(level,reversed_level)
            if level!=reversed_level:
                return False
        return True
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(2)
    
    node1.left,node1.right=node2,node3
    Ashu=Solution()
    print(Ashu.isSymmetric(node1))