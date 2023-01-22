#Ref:
#https://www.youtube.com/watch?v=wjYnzkAhcNk
# https://www.youtube.com/watch?v=PvrxZaH_eZ4&list=PL3edoBgC7ScV9WPytQ2dtso21YrTuUSBd&index=6
class Solution:
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        fast = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
        

