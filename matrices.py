from typing import List
Matrix = List[List]

'''
Matrices, or 2darrays
___________________________________________________________
What do you think happens when you do a loop in a loop? 
what kind of input do you need for you to be able to do so?
Let's see...
'''


matrix:Matrix = [[1,2], [3,4], [5,6]]

'''
Visually, what we made is as follows. remember that lists are 0-indexed
     
    cols 
rows 0 1
0   |1|2|
1   |3|4|
2   |5|6|

'''
for row in range(len(matrix)):
    print(matrix[row])

'''
Ok, so that gave us 3 1d arrays. great. but how do we get individual values?
Clearly after we step into a 1d array, we need to walk through that one now
we can do this by looping in our loop. 
'''
print('start of nested loops')
for row in range(len(matrix)):
    print(f'row: {row}')
    for col in range(len(matrix[row])):
        print(f'col: {col}')
        print(matrix[row][col])
print('done')
'''
Let's break down what we just did. We start both our row and column count at 0 
this is the top left of the matrix at index 0,0.
the value there is 1. so we print matrix[0][0], which again is 1
next, our bottom more loop increments. col increases by 1 , so we walk through the same array, or 
matrix [0][1], which is 2
now that we're out of columns, we increment the outer number by 1, exit the inner loop
and move to the next row. 
we call matrix [1][0], then increment the bottom number, then call matrix [1][1]. since we're out of 
columns, we exit the bottom loop, increment the top loop, and move down a row. Now, we print
matrix[2][0], increment the bottom row, and print matrix[2][1]. since we're at the upper bound (number of rows), we terminiate
'''






'''
Your exercise is to search a 13x2 string matrix of the alphabet, and return the indices of the letters that create a target phrase

'''

alphabet = [
    ['a', 'b'], 
    ['c', 'd'],
    ['e', 'f'],
    ['g', 'h'],
    ['i', 'j'],
    ['k', 'l'],
    ['m', 'n'],
    ['o', 'p'],
    ['q', 'r'],
    ['s', 't'],
    ['u', 'v'],
    ['w', 'x'],
    ['y', 'z']
]


def alphaSearch(alphabet:Matrix, target_phrase:str) -> Matrix:
    '''
    Hints: how do we ensure that characters that aren't part of the matrix are not ignored?
    What do we need to do to the string to  properly search a matrix for characters in that string?
    Take a look at the string notes if you forgot how to process/handle some aspects of strings.
    how should you store a "match" if you find it?
    Expected Worst Case Time Complexity: (O(n^3) + O(n)) = O(n^3)
    '''
    pass
    
print(alphaSearch(alphabet, "Happy birthday!"))

'''
BONUS (NOT REQUIRED):
The time complexity of your solution to the problem should depend on 3 loops. 
how can we decrease the amount of work we need to do? refer to the section on
dicts in order to determine how best to optimize this.

Expected Worst Case Time Complexity: O(n^2) + O(n) + O(1) = O(n^2)

'''
def alphaSearchOptima(alphabet:Matrix, target_phrase:str)-> Matrix:
    pass

print(alphaSearchOptima(alphabet, "Happy birthday!"))