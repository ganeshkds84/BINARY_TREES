class Solution:
    def NthRoot(self,n,m):
        if n==0:
            return 1
        if m==0:
            return 0
        l,u=0,m
        while l<=u:
            mid=(l+u)//2
            x=pow(mid,n)
            if x==m:
                return mid
            elif x>m:
                u=mid-1
            else:
                l=mid+1
        return-1
if __name__=='__main__':
    n=int(input('Enter nth root value:'))
    m=int(input('Enter the value:'))
    Ashu=Solution()
    print(Ashu.NthRoot(n,m))