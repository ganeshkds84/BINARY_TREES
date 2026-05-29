class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def isSimilar(self,p,q):
        def solve(node):
            if node is None:
                return [None]
            nodes=[]
            nodes.append(node.data)
            nodes.extend(solve(node.left))
            nodes.extend(solve(node.right))
            return nodes
        return solve(p)==solve(q)
if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    
    node3=TreeNode(1)
    node4=TreeNode(2)
    
    node1.left=node2
    node3.right=node4
    ashu=Solution()
    print(ashu.isSimilar(node1,node3))
        
    