# Find the size of a tuple in python

# 1 using getsizeof() function
import sys
tuple1=('A',1,'B',2,'C',3)
tuple2=('Geeks', 'For', 'Geeks',2.0)
tuple3=((1,'Lion'),(2,'Tiger'),(3,'Wolf'))

print('size of Tuple1'+str(sys.getsizeof(tuple1)))
print('size of Tuple2'+str(sys.getsizeof(tuple2)))
print('size of Tuple3'+str(sys.getsizeof(tuple3)))

print('\n\n')

# 2 using __sizeof__() function

print('size of Tuple1'+str(tuple1.__sizeof__()))
print('size of Tuple1'+str(tuple2.__sizeof__()))
print('size of Tuple1'+str(tuple3.__sizeof__()))