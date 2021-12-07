#User function Template for python3
import math
class Solution:
    def digitsInFactorial(self,N):
        # code here
        if(N==0):
            return 0
        ans=0
        for i in range(2,N+1):
            ans+=(math.log10(i))
        return int(ans)+1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        N=int(input())
        ob=Solution()
        print(ob.digitsInFactorial(N))
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends
