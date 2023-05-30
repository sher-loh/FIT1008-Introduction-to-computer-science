# Add comments to this file
#This line of code imports "List" and "TypeVar" from the typing module.
#"List" module imports all the relevants list formats
#"TypeVar" module allows you to refer to the same type repeatedly
from typing import List, TypeVar

T = TypeVar('T')

#A function named insertion_sort is created with the parameter list named the_list
def insertion_sort(the_list: List[T]):
    #Since T = TypeVar('T'), the function insertion_sort can take in a list of elements of
    #any types and return a list with element of same type as input list
    #the length of the_list is stored in a variable length
    length = len(the_list)
    #Use for loop to access each element in the_list by index starting from index 1 to the length(exclusive)
    for i in range(1, length):
        #the i-th element in the_list is stored in the variable key
        key = the_list[i]
        #Assigned j as the decremented value of i by 1
        j = i-1
        #while j is greater or equal to 0 and key is smaller than the j-th element in the_list
        while j >= 0 and key < the_list[j]:
            #the j-th element in the_list is stored in the (j+1)th index in the_list 
            the_list[j + 1] = the_list[j]
            #j is decremented by 1
            j -= 1
        #the value in key is stored in the (j+1)th index of the_list
        the_list[j + 1] = key

#A function named main is created 
def main() -> None:
    #An array named arr is created with the values 6,-2,7,4,-10.
    arr = [6, -2, 7, 4, -10]
    #Invoke the insertion_sort function
    insertion_sort(arr)
    #Use for loop to access each element in the arr list by index 
    for i in range(len(arr)):
        #print the i-th element in list arr and with a space  
        print(arr[i], end=" ")
    #print a new line
    print()

#Invoking the main function
main()
