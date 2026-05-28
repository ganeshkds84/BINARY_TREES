from inprepost import TreeNode
from maxDepth import Solution    
class Answer:
    def height(self,node):
        if node is None:
            return 0
        lefty=self.height(node.left)
        righty=self.height(node.right)
        
        return 1+max(lefty,righty)
    def isBalanced(self,root):
        if root is None:
            return True
        left_height=self.height(root.left)
        rigth_height=self.height(root.right)
        
        if abs(left_height-rigth_height)>1:
            return False
        return (
            self.isBalanced(root.left) and
            self.isBalanced(root.right)
        )
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(9)
    node3=TreeNode(10)
    node4=TreeNode(11)
    node5=TreeNode(12)
    
    node1.left,node1.right=node2,node3
    node3.left,node3.right=node4,node5
    
    ashu=Answer()
    print(ashu.isBalanced(node1))

