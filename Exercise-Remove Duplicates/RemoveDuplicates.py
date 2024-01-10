#Remove duplicates from a list by using Set DataStructure
def remove_duplicates(my_list):
    result = set(my_list)
    return result

my_list = [55,55,99,66,77,88,99,100,1,1,2,2,2,3,3,3,4,4,4,4,5,5,5,6,7,8,9,0]
print(remove_duplicates(my_list))
