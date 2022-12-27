# python program to add tuple to list and vise-versa

# 1 using += operator

#creating list
list1=[1,2,3,4]
print('Original List:-',list1)

# creating tuple
tup=(5,6)

# adding tuple to list
list1 += tup

print('After adding tuple to list:',list1)

# adding list to tuple

res = tuple(list(tup) + list1 )

print('After adding list to tuple:',res)


