#Question 02 Generate two lists of length 10 with random numbers in the range 100 to 200 and output the common elements among them as a list.
#Example: List 1 = [123, 174, 131, 191, 165, 157, 169, 154, 147, 101]
#List 2 = [131, 143, 165, 170, 146, 101, 178, 198, 191, 187]
#Output: [131, 165]



import random

def generate_random_list(length):
    return [random.randint(100, 200) for _ in range(length)] #useing random .randint use for to get the random numbers between range 100 to 200

def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))#using set function to get the list 

# Generate two random lists
list1 = generate_random_list(10) #length is defined 
list2 = generate_random_list(10)

common_elements = find_common_elements(list1, list2) #for common element 

# Print the lists and common number
print(f"List 1 = {list1}")
print(f"List 2 = {list2}")
print(f"Output: {common_elements}")

