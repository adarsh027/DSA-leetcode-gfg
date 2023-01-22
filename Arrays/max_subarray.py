# brute force or naive appraoch
class Solution:
    def subArraySum(self,arr, n): 
       max_sum=arr[0] # note: if max_sum is set to 0, then it won't work when all the values in the array are negative.
       #max_sum=float('-inf') # alternativley, set max_sum to minus infinity
       for i in range(0,n):#
               cur_sum=0
               for j in range(i,n): 
                   cur_sum= cur_sum+ arr[j]
                   max_sum = max(max_sum,cur_sum)
       print(max_sum)

Solution().subArraySum([-5,-7,-2,-7,-6,-23],5)


#Kadane's algorithm
# Ref https://www.youtube.com/watch?v=5WZl3MMT0Eg
# ref https://www.youtube.com/watch?v=HCL4_bOd3-4
class Solution:
    def subArraySum(self,arr, n): 
        cur_sum = 0
        max_sum = arr[0] # note: if max_sum is set to 0, then it won't work when all the values in the array are negative.
        #max_sum=float('-inf') # alternativley, set max_sum to minus infinity
        for x in arr:
            if cur_sum <0:
                cur_sum = 0
            cur_sum+=x
            max_sum = max(max_sum,cur_sum)
        return max_sum
    
Solution().subArraySum([-9,-7,-3,-1,-23],5)