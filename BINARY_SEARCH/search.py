class Solution:
    def find(self,nums,target):
        l=0
        u=len(nums)-1
        while l<=u:
            mid=(l+u)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l=mid+1
            else:
                u=mid-1
        return -1
        
if __name__=="__main__":
    nums=list(map(int,input('Enter numbers in asc order:').split()))
    target=int(input('Enter target value:'))
    obj=Solution()
    print(obj.find(nums,target))