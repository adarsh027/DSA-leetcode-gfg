# print all non-empty sub arrays and its count
# Note: no of subarrays in an array of length n = n*(n+1)/2
# note: no. of subsets in an array is diferent than no. of subarrays in an array.
# note: no. of subsets in an arrya of lenght n = 2^n (ie, 2 to the power of n)
class Solution:
    def sub_arrays(self,arr, n): 
       count = 0
       lst= [[]]
       for i in range(0,n):# i represents start index of each subarray
            for j in range(i,n):# j represents end index of each subarray
                count=count+1
                lst.append(arr[i:j+1])
                print(arr[i:j+1])# Here, j+1 means that jth index element is considered for each subarray
       print(count, lst)

           
Solution().sub_arrays([15,2,4,8,9,5,10,23],8)


# Equivalent code using only while loops
class Solution:
    def sub_arrays(self,arr, n): 
       i=0
       while i<n:
           j=i
           while j<n:
               print(arr[i:j+1])
               j+=1
           i+=1
        
Solution().sub_arrays([15,2,4,8,9,5,10,23],8)

# Obtain list of all subarrays, including the empty array[]
class Solution:
    def sub_arrays(self,arr, n): 
       lst= [[]]     # using a list initialized with an empty list in order to include an empty list in the output(ie, list of subarrays)
       for i in range(0,n):
            for j in range(i,n):
                lst.append(arr[i:j+1])
       return lst

           
Solution().sub_arrays([15,2,4,8,9,5,10,23],8)

# To display each subarray element individually, use an additional loop 
class Solution:
    def sub_arrays(self,arr, n): 
       count = 0
       for i in range(0,n):
            for j in range(i,n):
                for k in range(i,j+1):
                    print(arr[k])
                print("")
       print(count)
           
Solution().sub_arrays([15,2,4,8,9,5,10,23],8)



