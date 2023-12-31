# logic:
# add a empty list to add values which are duplicate
# iterate the list
# check if value in the list repeats more than once add it to empty list
# print the list
def duplicates(list):
    duplicate_values = []
    for item in list:
        if list.count(item) > 1 and item not in duplicate_values:
            duplicate_values.append(item)
    return duplicate_values if duplicate_values else "No duplicate"


result = duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 10, 10])
print(result)
