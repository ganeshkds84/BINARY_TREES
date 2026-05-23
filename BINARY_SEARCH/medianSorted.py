class Ashu:
    def median(self,nums1,nums2):
        final=nums1+nums2
        final.sort()
        l,u=0,len(final)-1
        mid=(l+u)//2
        if len(final)%2==1:
            return float(final[mid])
        else:
            return (final[mid]+final[mid+1])/2
        
    
if __name__=='__main__':
    nums1=list(map(int,input('Enter the numbers:').split()))
    nums2=list(map(int,input("Enter numbers in asc order:").split()))
    ganesh=Ashu()
    print(ganesh.median(nums1,nums2))