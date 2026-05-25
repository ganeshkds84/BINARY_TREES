class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def tree_traversal(self,root):
        in_order=[]
        pre_order=[]
        post_order=[]
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            in_order.append(node.data)
            inorder(node.right)
            
        def preorder(node):
            if node is None:
                return
            pre_order.append(node.data)
            preorder(node.left)
            preorder(node.right)
            
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            post_order.append(node.data)
            
        inorder(root)
        preorder(root)
        postorder(root)
        
        return [in_order,pre_order,post_order]    
    
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(3)
    node3=TreeNode(4)
    node4=TreeNode(5)
    node5=TreeNode(2)
    node6=TreeNode(7)
    node7=TreeNode(6)
    
    node1.left,node1.right=node2,node3
    node2.left,node2.right=node4,node5
    node3.left,node3.right=node6,node7
    
    Ashu=Solution()
    print(Ashu.tree_traversal(node1))
    
                

    
    