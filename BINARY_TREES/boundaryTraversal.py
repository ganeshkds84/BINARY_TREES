class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
class Solution:
    def boundaryTraversal(self,root):
        if root is None:
            return []
        def left_traversal(node):
            if node is None:
                return []
            nodes=[]
            if node.left is not None or node.right is not None:
                nodes.append(node.data)
            if node.left:
                nodes+=left_traversal(node.left)
            else:
                nodes+=left_traversal(node.right)
            return nodes
        def leaves(node):
            if node is None:
                return []
            nodes=[]
            if node.left is None and node.right is None:
                nodes.append(node.data)
            nodes+=leaves(node.left)
            nodes+=leaves(node.right)
            return nodes
        def right_traversal(node):
            if node is None:
                return []
            nodes=[]
            if node.right:
                nodes+=right_traversal(node.right)
            else:
                nodes+=right_traversal(node.left)
            if node.left is not None or node.right is not None:
                nodes.append(node.data)
            return nodes
        return ([root.data]+
                left_traversal(root.left)+
                leaves(root.left)+
                leaves(root.right)+
                right_traversal(root.right))
        
if __name__=='__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)

    node1.left, node1.right = node2, node3
    node2.left, node2.right = node4, node5
    node3.left, node3.right = node6, node7
    node5.left, node5.right = node8, node9
    
    Ashu=Solution()
    print(Ashu.boundaryTraversal(node1))