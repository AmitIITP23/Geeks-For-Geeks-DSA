#Driver Code Starts
#Initial Template for Python 3


import math


 # } Driver Code Ends
#User function Template for python3

class Solution:
    def exactly3Divisors(self,N):
        # code here
        ans=0
        def isPrime(k):
            for i in range(2,int(math.sqrt(k)+1)):
                if(k%i==0):
                    return False
            return True
        for i in range(2,int(math.sqrt(N)+1)):
            if(isPrime(i)):
                ans+=1
        return ans
            
            

#{ 
#Driver Code Starts.
def main():
    
    T=int(input())
    
    while(T>0):
        
        N=int(input())
        ob=Solution()
        print(ob.exactly3Divisors(N))
        
        T-=1
    

if __name__=="__main__":
    main()
#} Driver Code Ends
