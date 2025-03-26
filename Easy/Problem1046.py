# Given array of strings 'smash' two elements with the highest values removing them from the array.
# If their difference is not equal to 0, add result to the array. 
# Return last element in the array or 0 if it does not exist
class Solution:
    def lastStoneWeight(self, T) -> int:
        def build(T,n):
            for i in range(n//2-1,-1,-1):
                heapify(T,n,i)
        def heapify(T,n,i):
            m=i
            while True:
                a=2*i+1
                b=a+1
                if a<n and T[a]>T[m]:
                    m=a
                if b<n and T[b]>T[m]:
                    m=b
                if m==i:
                    return
                T[i],T[m]=T[m],T[i]
                i=m
        def extract(T,n):
            res=T[0]
            T[0]=T[n-1]
            heapify(T,n-1,0)
            return res
        def insert(T,n,v):
            T[n]=v
            i=n
            while True:
                p=(i-1)//2
                if p<0 or T[p]>v:
                    return
                T[i],T[p]=T[p],T[i]
                i=p
        n=len(T)
        build(T,n)
        while n>1:
            a=extract(T,n)
            n-=1
            b=extract(T,n)
            n-=1
            c=a-b
            if c!=0:
                insert(T,n,c)
                n+=1
        return 0 if n==0 else T[0]