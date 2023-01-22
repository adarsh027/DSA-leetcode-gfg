# Return start and end index of subarray of given sum
# sliding window approach : applicable to  array containing postive integers only
# references:
#1. submission by user SagarMc for  https://practice.geeksforgeeks.org/problems/subarray-with-given-sum-1587115621/1
#2. https://www.youtube.com/watch?v=Ofl4KgFhLsM
class Solution:
    def subArraySum(self,arr, n, s): 
        start, cur_sum = 0, 0
        for end in range(n):
            cur_sum += arr[end]
            while cur_sum > s and start < end:
                cur_sum -= arr[start]
                start += 1
            if cur_sum == s:
                return [start+1, end+1] # adding 1 to start and end since the problem specifies 1-nased indexing; if it was 0 based indexing, then there is no need for addding 1 to start and end
        return [-1] # implies not found
           
Solution().subArraySum([15,3,4,8,9,7,14,23],8,24)

# altrnatively using while loop
class Solution:
    def subArraySum(self,arr, n, s): 
        start,end, cur_sum = 0, 0,0
        while end<n:
            cur_sum += arr[end]
            while cur_sum > s and start < end:
                cur_sum -= arr[start]
                start += 1
            if cur_sum == s:
                return [start+1, end+1] # adding 1 to start and end since the problem specifies 1-based indexing; if it was 0-based indexing, then there is no need for addding 1 to start and end
            
            end += 1
        return [-1]
    
Solution().subArraySum([15,3,4,8,9,7,14,23],8,15)