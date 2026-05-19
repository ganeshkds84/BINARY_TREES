class Solution:
    def upperBound(self,nums,x):
        l=0
        u=len(nums)-1
        ans=len(nums)
        while l<=u:
            mid=(l+u)//2
            if nums[mid]>x:
                u=mid-1
                ans=mid
            else:
                l=mid+1
        return ans
    
    
if __name__=='__main__':
    nums=list(map(int,input('Enter numbers in asc order:').split(',')))
    x=int(input('Enter the target value:'))
    obj=Solution()
    print(obj.upperBound(nums,x))