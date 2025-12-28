'''list's in python are similar to the array 
   the main difference between the array and list is
   list stores the all type of sequence data 
   and array stores the one type of sequence data 
   and list can allocate the memory dynamically and
   array is used to store fixed type of data
   list is versitle in nature.'''

list_items = ["Siri","Rajitha","Nagaraju","Eshwar"] #storing the list elements
print(list_items)
print(list_items[0])#acessing the list elements using the index value is known as indexing
print(list_items[0:3])#accesing the range of values from the list is a slicing
list_items.append("Rama Kistaiah") #adding a elemnet at the end of the list
print(list_items)
list_items.insert(0,"Balamani")#insert method will insert the item at the particular index
print(list_items)
list_items2 = ["Nagaraju","Sravanthi","Omkari","Lahari"]
list_items.extend(list_items2)#extend method is used to extend the list of items indivigually to the listcompre to the 
#where insert and append methods adds the entire list to the exisiting one
print(list_items)
list_items.append(list_items2)
print(list_items)

'''Removing methods in the list '''
list_items.remove('Siri')#remove method removes the particular item from the list 
print(list_items)
list_items.pop()#pop method removes a particular item from the list and returns the removed item
print(list_items)
a = list_items.pop()
print(a)

'''Sorting and reversing methods'''
list_items2.reverse()#reverse method rever's the entire list
print(list_items2)
list_items.sort()#sort method will sort the entire list in alphabetical or numeric in ascending order
print(list_items)
list_items.sort(reverse=True)# if in sort method revrse = True then it will be sorted in the descending order
print(list_items)
sorted_list = sorted(list_items2)
print(sorted_list)
numbers = [1, 2, 3, 4, 5, 6]
print(min(numbers))#min method returns the min number from the list
print(max(numbers))#max method returns the max number from the list
print(sum(numbers))#sum method returns the total value of the  number from the list
print(numbers.index(5))#index method returns the provided value index

'''join and split methods'''
list_as_a_str=' - '.join(list_items)#join method will make the list items to the string at the first you should mention how you want to seprate it.thenafter in themethod pass the list variable as the argument
print(list_as_a_str)
new_list= list_as_a_str.split('-')#split method is used to break a string into a list first mention the string after '.' the split and function takes a argument that where to divide like if a scentence contains spcaes their if we specify to divide the scentence depending upon te spaces into a list as it is here depending upon the '-' it will divide into the list
print(new_list)

'''for loop'''
for item in list_items:#this function will return the each item in the list
    print(item)

for index,item in enumerate(list_items):#this function will return the index as well as the items in the list
    print(index, item)

for index,item in enumerate(list_items(start=1)):#this function will return the index and here the index starts at the 1 as well as the items in the list
    print(index, item)

''' list using a range function '''
list_1 = list(range(1,11,1))
print(list_1)
for i in list_1:
    print(i,end=',\n')
list_items = list(range(1,11,2))
i = 0
while i<len(list_items):
    print(list_items[i],end='\n')
    i+=1
