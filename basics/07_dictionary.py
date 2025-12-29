'''
Dictionary in python are used to store the data meaningfully using the key-value pairs
it contains multiple methods such as get,update,items,keys,etc...
'''
grocery_items={
  "Apples":"1kg-90",
  "oranges":60,
  "Grapes":50.67,
  "Mango":500} # here grocery_items variable is a  dictionary data type we can store the data in the form of key and value pairs

# Acessing the items from dictionary
print("Dictionary:", grocery_items)
print("Items:", grocery_items.items())
print("Keys:", grocery_items.keys())
print("Values:", grocery_items.values())
print("Length:", len(grocery_items))


# Using the get function for accessing the items from the dictionary 
print("Price of Grapes:", grocery_items.get("Grapes"))

# delete and pop methods for deleting
del grocery_items["Apples"]
print("After deleting Apples:", grocery_items)

removed_item = grocery_items.pop("Mango")
print("After popping Mango:", grocery_items)
print("Removed item:", removed_item)


# adding items into the dictionary
grocery_items["Crusted apple"] = 600
print("After adding Custard Apple:", grocery_items)

# Updating dictionary
grocery_items.update({
  "Apples":"1kg-90",
  "oranges":90,
  "Grapes":70.67,
  "Mango":800
})
print("After update:", grocery_items)

# Using Loops through Dictionary
for key in grocery_items:
    print(key,end='\n')

for key,value in grocery_items.items():
    print(key,value,end='\n')
