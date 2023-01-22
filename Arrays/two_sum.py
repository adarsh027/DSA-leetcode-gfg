# naive approach
class Solution:
    def two_sum(self,nums, target): 
       n = len(nums)
       for i in range(0,n):
            for j in range(i+1,n):
                if nums[i] + nums[j]== target:
                    return [i,j]

           
Solution().two_sum([15,2,4,8,9,5,10,23],11)



# using dictionary
# ref: https://www.youtube.com/watch?v=KLlXCFG5TnA&t=326s
class Solution:
    def two_sum(self,nums, target): 
       num_map = {} # dictionary to store already visited numbers
       for i,num in enumerate(nums):
           complement = target - num
           print(num_map, complement)
           if complement in num_map:
               return [num_map[complement],i]
           num_map[num] = i
       
                       
Solution().two_sum([15,2,4,8,9,5,10,23],11)
