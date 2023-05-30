# Add comments to this file
#A function named binary_search with parameters the_list, target, low and high is created
def binary_search(the_list: list, target: int, low: int, high: int) -> int:
    #if the value in low is greater high
    if low > high:
        #return the value -1
        return -1
    #if the value in high is greater than low
    else:
        #The integer division of the addition of high and low is assigned to variable mid
        mid = (high + low) // 2
        #if the mid-th index of the_list is equal to the target value
        if the_list[mid] == target:
            #return the index of target in the_list
            return mid
        #else if the mid-th index of the_list is greater than the target value
        elif the_list[mid] > target:
            #call binary_search funtion recursively, argument high is set to mid-1
            return binary_search(the_list, target, low, mid - 1)
        #if the mid-th index of the_list is smaller than target
        else:
            #call binary_search funtion recursively, argument low is set to mid+1
            return binary_search(the_list, target, mid + 1, high)

#A function named main is created
def main() -> None:
    #A list named arr with the values of 1,5,10,11,12 is created
    arr = [1, 5, 10, 11, 12]
    #The return value of the binary_search function with the parameters
    #list arr, 11, 0, and len(arr)-1 is assigned to the variable index
    index = binary_search(arr, 11, 0, len(arr) - 1)
    #print the value stored in index
    print(index)

#Invoke the main function
main()
