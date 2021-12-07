#User function Template for python3

import math

class Solution:
	def quadraticRoots(self, a, b, c):
	    
        # code here
        d=(b*b)-(4*a*c)
        if(d<0):
            return (['Imaginary'])
        else:
            sqrtD=math.sqrt(d)
            root1=(-b+sqrtD)//(2*a)
            root2=(-b-sqrtD)//(2*a)
            return int(max(root1,root2)),int(min(root1,root2))



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    for _ in range(tc):
        abc=[int(x) for x in input().strip().split()]
        a=abc[0]
        b=abc[1]
        c=abc[2]
        ob = Solution()
        ans = ob.quadraticRoots(a,b,c)
        if len(ans)==1 and ans[0]==-1:
            print("Imaginary")
        else:
            for i in range(len(ans)):
                print(ans[i], end=" ")
            print()

# } Driver Code Ends
