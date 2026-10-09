# Write a Python program to find the common elements between two lists using sets.
# list1 = [10, 20, 30, 40, 50]
# list2 = [30, 40, 50, 60, 70]

l_1= [10, 20, 30, 40, 50]
l_2 = [30, 40, 50, 60, 70]
list_change_1 = set(l_1)
list_change_2 = set(l_2)

common_elements = list_change_1 & list_change_2 # using intersection operator

print("common elements between two lists using sets:",common_elements)