from inprepost import TreeNode

class Solution:
    def preOrder(self,root):
        pre_order=[]
        def preTraversal(node):
            if node is None:
                return
            pre_order.append(node.data)
            preTraversal(node.left)
            preTraversal(node.right)
        preTraversal(root)
        
        return pre_order

if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(4)
    node3=TreeNode(4)
    node4=TreeNode(2)
    
    node1.left=node2
    node2.left,node2.right=node3,node4
    
    obj=Solution()
    print(obj.preOrder(node1))