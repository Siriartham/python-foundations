'''
Tuple is a muteable data type here we can store different types of sequence data
but tuples cannot add the data or remove the data from the decleared tuple.
So, it does not contain more functions to use.
There is a unqiue speciality in tuple that if we assign a varibale with a sequence of  values without any [],{},() then
the data type of the variable will be the tuple.
'''

tuple2 = (2,3,4,5,6,7)  
tuple1 = (23,3,6,67,9)  
print(tuple1[0])       # we can access the values from the tuples
print(len(tuple2))     # length of the tuple
print(tuple2+tuple1)   # concatenation the two tuples
print((tuple2)*2)      # multiplying the inner values
print(sorted(tuple1))  # sorted tuple in the ascending order
print(sorted(tuple1,reverse=True)) # sorted tuple in the descending order

a = 23,45,78,1,3
print(type(a)) # it will return the tuple data type 
empty_tuple = () # empty tuple 
empty_tuple1 = tuple()  # empty tuple 
print(empty_tuple)

'''
Set's are unodered collection of data.
means it doesn't contain any particular oder to store 
when ever we print the elements in the set it will be in the different order.
it contains some function's like difference and union and intersection. 
'''
empty_set = set() #empty set
set_1={45,89,9,56,77}   #  set is a data type it is mainly used for such function's of intersection and union and difference
set_2={8,9,45,22,77}  
print(set_1)
print(set_2)
print(set_1.difference(set_2)) # will display values which are present in the set_1 which are not present in the set_2
print(set_2.difference(set_1)) # will display values which are present in the set_2 which are not present in the set_1
print(set_1.union(set_2)) # it will display the values of set except the common 
print(set_1.intersection(set_2)) # will display values which are present in the both the sets
