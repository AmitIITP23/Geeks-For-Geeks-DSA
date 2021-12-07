#{ 
#Driver Code Starts
#Initial Template for Python 3

import math


 # } Driver Code Ends
#User function Template for python3

class Solution:    
    #Compelte his function
    def termOfGP(self,A,B,N):
        #Your code here
        ratio=B/A
        ans=A
        for i in range(2,N+1):
            ans=ans*ratio
        return ans
            


#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        AB=[int(x) for x in input().strip().split()]
        A=AB[0]
        B=AB[1]
        
        N=int(input())
        ob=Solution()
        print(math.floor(ob.termOfGP(A,B,N)))
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends
