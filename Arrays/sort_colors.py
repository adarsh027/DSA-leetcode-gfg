#logic
# 1. Iterate and find the count of 0s,1s and 2s in the array.
# 2 Based upon the counts of 0,1 and 2, place 0s,1s and 2s in the array.
class Solution:
    def sortColors(self, nums):
        count0=count1=count2=0
        for num in nums:
            print(num)
            if num==0:
                count0+=1
                print(count0)
            if num==1:
                count1+=1
            if num==2:
                count2+=1
        print(count0,count1,count2)
        i=0        
        while count0>0:
            nums[i]=0
            i=i+1
            count0=count0 - 1
        while count1>0:
            nums[i]=1
            i=i+1
            count1=count1-1
        while count2>0:
            nums[i]=2
            i=i+1
            count2=count2-1
        return nums

Solution().sortColors([2,0,2,1,1,0,1,1])

#optimised solution with only 1 single pass
#Ref : https://www.enjoyalgorithms.com/blog/sort-an-array-of-0s-1s-and-2s 
#Ref: https://www.youtube.com/watch?v=oaVa-9wmpns
class Solution:
    def sortColors(self, nums):
        left, mid, right=  0, 0, len(nums)-1
        
        while mid <= right:
            if nums[mid] == 0:
                nums[mid],nums[left] = nums[left], nums[mid]
                left += 1
                mid+=1

            elif nums[mid]==2:
                nums[mid], nums[right] = nums[right], nums[mid]
                right-=1
            else:# when nums[mid]==1
                mid+=1
        return nums

Solution().sortColors([2,0,2,1,1,0,1,1])

