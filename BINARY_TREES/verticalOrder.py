class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Solution:
    def verticalOrder(self,root):
        nodes=[]
        def dfs(node,row,col):
            if node is None:
                return
            nodes.append((col,row,node.data))
            dfs(node.left,row+1,col-1)
            dfs(node.right,row+1,col+1)
        dfs(root,0,0)
        nodes.sort()
        ans=[]
        prev_col=None
        for col,row,node in nodes:
            if prev_col!=col:
                ans.append([])
                prev_col=col
            ans[-1].append(node)
            
        return ans

if __name__=='__main__':
    node1=TreeNode(1)
    node2=TreeNode(2)
    node3=TreeNode(3)
    node4=TreeNode(4)
    node5=TreeNode(5)
    node6=TreeNode(6)
    
    node1.left,node1.right=node2,node3
    node3.left,node3.right=node4,node5
    node5.right=node6
    
    Ashu=Solution()
    print(Ashu.verticalOrder(node1))