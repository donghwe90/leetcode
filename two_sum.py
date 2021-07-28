# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

def two_sum(nums, target):
    d = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        if nums[i] in d.keys():
            return [i, d[nums[i]]]
        d[complement] = i


       

        



        
        

        


    

    

    

    print(d)

# arr = [1,2,3]

# two_sum(arr, 1)
