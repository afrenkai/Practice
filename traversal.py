# different data types in python
from typing import List, Tuple, Dict
'''
Numeric
_______________________________________
int: 
    - represent whole (integer numbers)
    - examples: 1, -3, 7, 50343030, etc. 
float: 
    - represents decimal numbers
    - examples: 0.1, -0.7, 1.7, 1e-12

Text
_______________________________________
str: 
    - sequence of characters
    - example: "Hello World"

Sequence
_______________________________________
list: 
    - ordered, mutable collection of items
    - example: [1, 2, "apple", 2.7]
    - traversal: 
    Option 1: 
    
    for i in list:
        print(i)

    Option 2:

    for j in range (len(list)):
        print(list[j])
    
    IMPORTANT: Lists are 0-indexed in python, so you start counting from 0
tuple:
    - ordered, immutable collection of items
    - example: (1, 2, "apple", 2.7)
range:
    - sequence of numbers
    - example: range(1,5)

Mapping
_______________________________________
Dict:
    - collection of key, value pairsm, 
        where key maps to value using :
    - examples:
        {name: john} 
    - traversal:
        for k, v in dict.items():
            print(k, v)

'''
#variable |type  |assignment operator|value
list:      list   =                   [1, 2, "apple", 2.7]

def traverseList(list:List[float]|List[int], n: int|None) -> None:
    '''
    Parameters: 
        list: List of floats or ints
        n: optional arg integer that 
            represents how many items to print from the list
    Functionality: Loops through list n times if n present, else entire list
    Returns: Nothing, prints the output mid function.
    '''
    if n:
        for i in range(n):
            print('first method value with n')
            print(list[i])
    else:
        for i in range(len(list)):
            print('first method value with no n:')
            print(list[i])

    for j in list:
        print('second method value')
        print(j)



def main():
    list = [1, 2, "apple", 2.7] #change the list to be whatever
    traverseList(list, 3) #change the n to be however many you want, or even none
    traverseList(list, None)


if __name__ == "__main__":
    main()