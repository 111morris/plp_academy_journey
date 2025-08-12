# Step 1: Create an empty list called my_list
my_list = []

# Step 2: Append the following elements to my_list: 10, 20, 30, 40
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# Step 3: Insert the value 15 at the second position in the list
my_list.insert(1, 15)  # index 1 is the second position

print(my_list)

# Step 4: Extend my_list with another list: [50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element from my_list
my_list.pop()

print(my_list)

# Step 6: Sort my_list in ascending order
my_list.sort()
print(my_list)
# Step 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
