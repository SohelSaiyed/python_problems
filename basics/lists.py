# double the value only if for odd numbers in list
# takes a list and returns a list
def odd_doubles(nums):
    print(f"calculating odd doubles (v1) for {nums}")
    result = []
    for num in nums:
      if num % 2 !=  0:
        # double the number and add to the list 
        num = num * num
        result.append(num)
      else:
        # just add to the list
        result.append(num) 
    print(f" returning result: {result}") 
    return result          

# small tidy up
def odd_doubles_v2(nums):
    print(f"calculating odd doubles (v2) for {nums}")
    result = []
    for num in nums:
      if num % 2 !=  0:
        # double the number and add to the list 
        num = num * num
    
      result.append(num)

    print(f" returning result: {result}") 
    return result          

# list comprehension with conditions - pythonic way
# reference: https://stackoverflow.com/a/4260304
def odd_doubles_v3(nums):
    print(f"calculating odd doubles (v3 - list comprehension) for {nums}")
    
    # For filtering out odd numbers as well. below will return just the doubles (of odd nums)
    # result = [num * num for num in nums if num % 2 == 1 ]
    
    # double if odd else just return num for the sequence
    result = [num * num if num % 2 == 1 else num for num in nums]
    
    print(f"returning result: {result}")
    return result

input = [1, 2, 3, 4, 5, 6]
output = [1, 2, 9, 4, 25, 6]
assert output == odd_doubles(input)
assert output == odd_doubles_v2(input)
assert output == odd_doubles_v3(input)