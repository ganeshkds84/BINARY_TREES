class TreeNode:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None
        
class Solution:
    def InOrder(self,root):
        in_order=[]
        def inOrder(node):
            if node is None:
                return
            inOrder(node.left)
            in_order.append(node.data)
            inOrder(node.right)
            
        inOrder(root)
        return in_order
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    
    node1.left,node1.right=node2,node3
    node2.left=node4
    node3.left=node5
    
    obj=Solution()
    print(obj.InOrder(node1))