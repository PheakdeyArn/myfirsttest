# learn filter function

# define an even method
def isEven(n):
    return n%2==0

# create a list
nums = [3,2,4,6,6,8,7,9,5]

# filter will take the list and filt it then return the value
# create a filter of nums with even mehtod
even = list(filter(isEven, nums))
print(even)

# second way 
even2 = list(filter(lambda n: n%2==1, nums))
print(even2)
