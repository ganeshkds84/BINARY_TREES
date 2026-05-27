class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    def maxDepth(self,node):
        if node is None:
            return 0
        left_depth=self.maxDepth(node.left)
        print(left_depth)
        right_depth=self.maxDepth(node.right)
        
        return 1+max(left_depth,right_depth)
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    
    node1.left,node1.right=node2,node3
    node3.left=node4
    node4.right=node5
    
    Ashu=Solution()
    print(Ashu.maxDepth(node1))