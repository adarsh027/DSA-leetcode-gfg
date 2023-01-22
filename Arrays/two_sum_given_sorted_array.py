# two pointer approach
#Two pointer approach is handy in problems where a sorted array needs to fulfill certain constraints
# w.r.t a specific array element(as in the case of binary search) or a set of array elements(such as a pair, a triplet, or even a subarray)
# Reference for the above lines about two pointers:https://www.educative.io/blog/coding-interview-leetcode-patterns

# ref : https://www.youtube.com/watch?v=cQ1Oz4ckceM
class Solution:
    def two_sum(self, nums, target):
        left=0
        right=len(nums)-1
        while left<right:
            cur_sum= nums[left]+nums[right]
            if cur_sum==target:
                return [left, right]
            elif cur_sum>target:
                right-=1
            else:
                left+=1
        