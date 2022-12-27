# python program to create a list of tuples from given list having number and its cube in each tuple

# create list
list1=[1,2,3,4]

# using list comprehension to iterate each values in list and create a tuple as specified
# 1 using pow() method
res=[(val,pow(val,3)) for val in list1 ]
print(res)

# 2 using ** operator
res=[(val,pow(val,3)) for val in list1 ]

print(res)