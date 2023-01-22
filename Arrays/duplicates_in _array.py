# using set
class Solution(object):
    def findDuplicate(self, nums):
        dups=[]
        seen =set() # seen will contian only unique elements
        for num in nums:
            if num in seen:
                dups.append(abs(num))
            else:
                seen.add(num)
        print(seen, dups)

                
Solution().findDuplicate([3,1,3,4,2,4,8,9])

# using dictionary
class Solution(object):
    def findDuplicate(self, nums):
        dups=[]
        freq ={}
        for num in nums:
            if num in freq:
                freq[num] = freq[num]+1
                dups.append(num)
            else:
                freq[num] = 1  
        print(freq.keys(),dups)
                

Solution().findDuplicate([3,1,3,4,2,4,8,9,2])
