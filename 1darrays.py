'''
1darrays:
treat as lists
using traversal, you kind of get an idea of how to walk through them. 
you also know that since they're lists, they're mutable, so you can change them.
you also know that they're 0 indexed, meaning when you start walking through them, you start
counting at 0
Here's an example
'''

example_array = [1,2,3,4]

def arrExample(arr: list) -> list: 
    '''
    Parameters: 
        - arr: list that's the array we pass in 
    Functionality: 
        - print the first index ([0]) since we start counting from there
        - Substitute 3rd entry for another value
        - walks through the array, printing each item
    Returns: 
        - Array(List) after all modification
    '''
    print(arr[0])
    print(arr[2]) # third, remember we started counting at 0
    arr[2] = 7 # now, it should look likee [1,2,7,4]. let's print to verify
    print(arr)
    for i in arr:
        print(i)
    return arr



print(arrExample(example_array))


'''
your task is to write a similar method to our prior, 
with these requirements

Input: digits of your DOB in YYYY-MM-DD format

Function: 
    - Takes in array of dob as defined prior
    - reorder the array such that the array is now in 
      MM-DD-YYYY format
      Hint: you can access chunks like [0:4] instead of doing them 1 by 1
    - print each item in the array
    - return the array after you sorted it as a string, separated by slashes (given)
'''


dob_arr = [2,0,0,4,0,1,1,9]
slashes = [2, 5] # since expanding the array for the prior slash 
# will offset the place we should put the slash

expected_output = "01/19/2004" # change to fit yours

def dobModify(arr:list)-> str:
    pass


print('yep') if dobModify(dob_arr) == expected_output else print('no')