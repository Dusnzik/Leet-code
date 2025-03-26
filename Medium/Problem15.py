#Given an integer array, return all triplets that have different indiecs and no duplicates.
class Solution:
    def threeSum(self, nums):
        nums.sort()
        n=len(nums)
        ans=[]
        if nums.count(0)>=3:
            ans.append([0,0,0])
        for i in range(n-2):
            if  nums[i]==nums[i-1] and i!=0:
                continue
            x=nums[i]
            if x>-1:
                break
            y=n-1
            j=i+1
            while j<y:
                p=nums[j]
                q=nums[y]
                if x+p+q<0:
                    j+=1
                    continue              
                if x+p+q==0:
                    ans.append([x,p,q])
                    j+=1
                    while nums[j]==p and j<y:
                        j+=1
                if q<0:
                    break
                y-=1
        return ans