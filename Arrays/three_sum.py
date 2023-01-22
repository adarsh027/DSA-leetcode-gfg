# using dictionary
class Solution:
    def threeSum(self, nums, target):
        res=[]
        for i in range(len(nums)-2):
            num_map = {}
            for j in range(i + 1, len(nums)):
                complement = target - (nums[i] + nums[j])
                if complement in num_map:
                    print(nums[i], nums[j], complement)
                    triplets= tuple(sorted([nums[i], nums[j], complement])) # sorting so that duplicate triplets can be identified and removed.
                    res.append(triplets)
                else:
                    num_map[nums[j]]=1
                
        return list(set(res))

Solution().threeSum([15,15,0,10,2,4,-10,8,9,5,5,5],0)

# using set

class Solution:
    def threeSum(self, nums, target):
        res=[]
        for i in range(len(nums)-2):
            num_map = set()
            for j in range(i + 1, len(nums)):
                complement = target - (nums[i] + nums[j])
                if complement in num_map:
                    print(nums[i], nums[j], complement)
                    triplets= tuple(sorted([nums[i], nums[j], complement])) # sorting so that duplicate triplets can be identified and removed.
                    res.append(triplets)
                else:
                    num_map.add(nums[j])
                
        return list(set(res))

Solution().threeSum([15,15,0,10,2,4,-10,8,9,5,5,5],0)