"""
Create a function that given a list as a parameter find the even numbers inside the list. The function should then return a list 
Example Input: [2,7,10,5,12]
Example Output: [2,10,12]

"""

def returnEvens(list1):
    list1 = [num for num in list1 if num % 2 == 0]
    print(list1)

returnEvens([1,2,3,4,5,6,7,8,9,10]) # [2,4,6,8,10]
returnEvens([2,7,10,5,12]) # [2,10,12]