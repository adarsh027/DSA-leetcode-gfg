#Given  length = n and 1<= nums[i] <= n
# Ref: https://www.youtube.com/watch?v=kRrSeAZRD6E

# Note: suppose you have an array of lenght, n =5, then the values in the array can be from 1,2,...5.
# 1. Compute index using each number in the arrays as index = abs(num) - 1
# 2. Number corresponding to the index greater than 0 will be the unique values and will be made as negative in the array .
# 3. Number corresponding to the index less than 0 will be the duplicate values.


class Solution(object):
    def findDuplicate(self, nums):
        unq=[]
        dups=[]
        for num in nums:
            index= abs(num) - 1
            print(index)
            if nums[index] > 0:
                nums[index] = -nums[index]
                unq.append(abs(num))
            else:
                #return abs(num) # use this if you want the 1st duplicate element
                dups.append(abs(num))
        print(unq,dups)
                


Solution().findDuplicate([3,1,2,4,2,1,1,4])
