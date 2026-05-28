class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    def maxPathSum(self,root):
        self.global_sum=float('-inf')    
        self.pathSum(root)
        return self.global_sum
        
    def pathSum(self,node):
        if node is None:
            return 0
        lefty=max(0,self.pathSum(node.left))
        righty=max(0,self.pathSum(node.right))
        current_sum=node.data+lefty+righty
        self.global_sum=max(self.global_sum,current_sum)
        
        return node.data + max(lefty,righty)

if __name__=='__main__':
    node1=TreeNode(20)
    node2=TreeNode(9)
    node3=TreeNode(-10)
    node4=TreeNode(15)
    node5=TreeNode(7)
    
    node1.left,node1.right=node2,node3
    node3.left,node3.rigth=node4,node5
    
    ashu=Solution()
    print(ashu.maxPathSum(node1))
    