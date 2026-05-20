class Ashu:
    def single(self,nums):
        l,u=0,len(nums)-1
        while l<u:
            mid=(l+u)//2
            if mid%2==1:
                mid-=1
            if nums[mid]==nums[mid+1]:
                l=mid+2
            else:
                u=mid
        return nums[l]
    
if __name__=='__main__':
    nums=list(map(int,input('Enter numbers:').split()))
    ganesh=Ashu()
    print(ganesh.single(nums))
    