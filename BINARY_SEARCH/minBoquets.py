class Solution:
    def Ashu(self,nums,m,k):
        if m*k>len(nums):
            return -1
        l,u=min(nums),max(nums)
        ans=-1
        while l<=u:
            mid=(l+u)//2
            b,c=0,0
            for i in range(len(nums)):
                if nums[i]<=mid:
                    c+=1
                    if c==k:
                        b+=1
                        c=0
                else:
                    c=0
            if b>=m:
                ans=mid
                u=mid-1
            else:
                l=mid+1
                
        return ans
    
if __name__=='__main__':
    nums=list(map(int,input('Enter the days to bloom a flower:').split()))
    m=int(input('Number of boquets:'))
    k=int(input('Number of days:'))
    ganesh=Solution()
    print(ganesh.Ashu(nums,m,k))