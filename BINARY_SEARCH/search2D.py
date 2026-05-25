class Solution:
    def search(self,mat,target):
        for i in range(len(mat)):
            l,u=0,len(mat[i])-1
            if mat[i][u]<target:
                continue
            while l<=u:
                mid=(l+u)//2
                if mat[i][mid]==target:
                    return True
                elif mat[i][mid]<target:
                    l=mid+1
                else:
                    u=mid-1
                    
        return False
    
if __name__=='__main__':
    matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    target=int(input('Enter target value:'))
    obj=Solution()
    print(obj.search(matrix,target))
    
    