class Solution:
    def Ashu(self,piles,h):
        l,u=1,max(piles)
        while l<=u:
            mid=(l+u)//2
            hours=0
            for i in range(len(piles)):
                hours+=(piles[i]+mid-1)//mid
            if hours<=h:
                ans=mid
                u=mid-1
            else:
                l=mid+1
        return ans        
        
if __name__=='__main__':
    piles=list(map(int,input('Enter the bananas:').split()))
    h=int(input('Enter the tie in hours:'))
    ganesh=Solution()
    print(ganesh.Ashu(piles,h))