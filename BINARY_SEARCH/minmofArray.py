class ashu:
    def findMin(self,nums):
        l,u=0,len(nums)-1
        while l<u:
            mid=(l+u)//2
            if nums[mid]>nums[u]:
                l=mid+1
            else:
                u=mid
                
        return nums[l]
    
if __name__=='__main__':
    nums=list(map(int,input('Enter the numbers:').split()))
    ganesh=ashu()
    print(ganesh.findMin(nums))