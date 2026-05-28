from inprepost import TreeNode

class Solution:
    def diameter(self,root):
        
        self.diameter=0
        self.height(root)
        return self.diameter
    def height(self,node):
        if node is None:
            return 0
        lefty=self.height(node.left)
        righty=self.height(node.right)
        
        c_d=lefty+righty
        self.diameter=max(self.diameter,c_d)
        
        return 1+max(lefty,righty)
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(9)
    node3=TreeNode(10)
    node4=TreeNode(11)
    node5=TreeNode(12)
    
    node1.left,node1.right=node2,node3
    node3.left,node3.right=node4,node5
    
    Ashu=Solution()
    print(Ashu.diameter(node1))