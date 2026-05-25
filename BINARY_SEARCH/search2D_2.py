class Solution:
    def search(self,matrix,target):
        temp=len(matrix[0])-1
        while temp>=0 and matrix[0][temp]<target:
            temp-=1
        if temp<0:
            return False
        for i in range(len(matrix)):
            l,u=0,temp
            if matrix[i][u]<target:
                continue
            while l<=u:
                mid=(l+u)//2
                if matrix[i][mid]==target:
                    return True
                elif matrix[i][mid]>target:
                    u=mid-1
                else:
                    l=mid+1
                
        return False
    
if __name__=='__main__':
    matrix= [ [1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30] ]
    target=int(input('Enter the target value:'))
    Ashu=Solution()
    print(Ashu.search(matrix,target))