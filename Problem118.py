#Pascal's triangle with given rows
class Solution:
    def generate(self, numRows: int):
        ans=[[1]]
        for i in range(2,numRows+1):
            cur=[1 for _ in range(i)]
            for j in range(1,i-1):
                cur[j]=ans[-1][j]+ans[-1][j-1]
            ans.append(cur)
        return ans
                