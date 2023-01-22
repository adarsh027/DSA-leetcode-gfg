# count no. of subarrays with given sum
#solution 1: Naive approach
class Solution:
    def subArraySum(self,arr, n, s): 
       count = 0
       for i in range(0,n):# i represents start index of each subarray
               cur_sum=0
               for j in range(i,n): # j represents end index of each subarray
                   cur_sum= cur_sum+ arr[j]
                   if cur_sum==s:
                       count+= 1
                       print(i,j)
       print(count)

Solution().subArraySum([15,3,4,8,9,7,14,23],8,7)


#solution 2: prefix sum approach
# refer submitted solution in leetcode
#ref: https://www.youtube.com/watch?v=fFVZt-6sgyo
class Solution:
    def subarraysum(self, nums,n,k):
        res=0 # count of subarrays having given sum
        cur_sum = 0
        prefix_sums={0:1}

        for num in nums:
            cur_sum = cur_sum + num

            if cur_sum-k in prefix_sums:
                res = res + prefix_sums[cur_sum-k]

            if cur_sum not in prefix_sums:
                prefix_sums[cur_sum] = 1
            else:
                prefix_sums[cur_sum] = prefix_sums[cur_sum]+1

        return res

Solution().subarraysum([1,3,3,4,8,9,6,23,15],8,15)







