import two_sum_long_input as tsli

"""
Single Loop with dictionary
Think concept: a+b = b+a
formula: b = target - a
"""
def two_sum(nums, target):
      cache = {}
      for (i, num) in enumerate(nums):
        # formula 
        othernum = target - num
        
        if othernum in cache:
            # if b exists already in dict, then retrieve its val (index) 
            # and send it along with current index 
            return [cache[othernum] , i ]
        else:
            # store current index in cache. keyed by current num
            cache[num] = i
      
      # return empty if combinations are not possible
      return []

assert [9998,9999] == two_sum(tsli.long_input, tsli.long_input_target)
assert [0, 3] == two_sum([2,3,7,9], 11) 
assert [] == two_sum([2,3,7,9], 19) 

print('done')