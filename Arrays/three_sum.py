# Ref: https://www.youtube.com/watch?v=8uWRUyWpy8M(Timothy H Chang)
# Ref: https://www.youtube.com/watch?v=n2_HLNY8e_Q(Sai Anish Malla)
# Ref: https://www.youtube.com/watch?v=6qgC-dqKElA(thecodingworld)
# Ref: https://www.youtube.com/watch?v=qJSPYnS35SE (Nick White)
# Ref: https://www.youtube.com/watch?v=jzZsG8n2R9A(NeetCode)
# Ref:https://www.youtube.com/watch?v=hNRS81I1OZ8&t=1298s(DataDaft)

#Brute force solution
class Solution:
    def three_sum(self, nums, target):
        n = len(nums)-1 
        res=[]
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    cur_sum = nums[i] + nums[j] + nums[k] 
                    if (cur_sum== target):
                        triplets=tuple(sorted([nums[i],nums[j],nums[k]]))# sorting so that duplicate triplets can be identified and removed.
                        res.append(triplets)

        return list(set((res)))
             
                       
Solution().three_sum([15,15,0,10,2,4,-10,8,9,5,5,5,0,-10,0],0)

# two-pointer solution
class Solution:
    def three_sum(self, nums, target):
        res= []
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left<right:
                cur_sum= nums[i] + nums[left]+nums[right]
                if cur_sum==target:
                    res.append([nums[i],nums[left], nums[right]])
                    while left< right and nums[left]==nums[left+1] :# to make sure duplicates are ignored for the left pointer  
                        left+=1
                    while left< right and nums[right]==nums[right-1] :# to make sure duplicates are ignored for the right pointer
                        right-=1
                    left+=1
                    right-=1
                    
                elif cur_sum>target:
                    right-=1
                else:
                    left+=1
        return res
            
                       
Solution().three_sum([15,15,0,10,2,4,-10,8,9,5,5,5],0)