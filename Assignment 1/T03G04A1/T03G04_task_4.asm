#name: Daisuke Murakami, Fathin Acyuta Makarim, Lim Rui Shun, Loh Jing Wei
#date: 18th March 2022

# The MIPS code below faithfully translates a python code that performs an insertion sort. 

# Created two global variables to print newline and a white space as a string. 
.data 	
	newline: .asciiz "\n"
	space: .asciiz " "
.text
# In the main() function, the code first initializes a local variable of the array arr
# as to pass it as an argument inside a function called insertion_sort(). 

# Then, after receiving the sorted array from insertion_sort(), the main function utilizes a 
# for loop (main_loop) to loop through the array one by one to print each elements. 
# Since the original python code outputs arr by print(arr[i], end=" "), the translated MIPS
# code has added a blank space after every elements that is printed. 

# The main function is divided into three labels: main, main_loop, and print.
# main was created to initialized the arr variable and the argument to pass into the insertion sort function. 

# Stack frame diagram for main
# arr[i] is at -16($fp)
# length is at -12($fp)
# arr is at -8($fp)
# i is at -4($fp)
# arg 1 is at 0($fp)

main:	
	# Copy stack into frame pointer
	addi $fp, $sp, 0
	
	# Allocate space for 3local variables, 3 * 4 = 12
	addi $sp, $sp, -16
	
	#Initialize locals 
	#Initalize arr of size 5
	addi $v0, $0, 9 # call code to allocate space for array
	addi $t0, $0, 6 # #t0 = 5(size of array) + 1
	sll $a0, $t0, 2 # $a0 = (5 + 1) * 4
	syscall
	sw $v0, -8($fp)
	addi $t0, $0, 5
	sw $t0, ($v0) #First element for the arr array

	lw $t0, -8($fp) # $t0 = Address of arr
	addi $t1, $0, 6
	sw $t1, 4($t0) # arr[0] = 6
	addi $t1, $0, -2
	sw $t1, 8($t0) # arr[1] = -2
	addi $t1, $0, 7
	sw $t1, 12($t0) # arr[2] = 7
	addi $t1, $0, 4
	sw $t1, 16($t0) # arr[3] = 4
	addi $t1, $0, -10
	sw $t1, 20($t0) # arr[4] = -10
	
	# Store first element of the array as length
	lw $t0, -8($fp) # $t0 = address of the array
	lw $t0, ($t0)   # $t0 = array[0]
	sw $t0, -12($fp)# -12($fp) = length of array
	
	#Initialize i 
	sw $t0, -4($fp) # i = 0
	
	#Call function insertion_sort
	#push 1*4 = 4 bytes for one argument
	addi $sp, $sp, -4 
	
	#arg = arr
	lw $t0, -8($fp) #load arr
	sw $t0, 0($sp)  #arg 1 = arr
	
	#Enter insertion_sort function. 
	jal insertion_sort
	
	#Remove the arr 
	addi $sp, $sp, 4 # 1*4=4
		
	# Store returned array as -8($fp)
	sw $v0, -8($fp)

	# Store 0 to i
	sw $0, -4($fp)

# The main_loop prints the arr[i] values that were returned from the insertion_sort function.
# After printin the elements, it also prints a white space to demonstrate the end=" " in the orignal python code, which adds a space.
# Also, this loop by it self increments i by one.
# Stack frame diagram for main
# arr[i] is at -16($fp)
# length is at -12($fp)
# returned version of arr is at -8($fp)
# i is at -4($fp)
# arg 1 is at 0($fp)

main_loop:
	# if arr.length == i
	lw $t0, -4($fp)
	lw $t1, -12($fp)
	beq $t0, $t1, print #if i == arr.length, jump to print
	
	#print(arr[i])
	lw $t0, -8($fp)
	lw $t1, -4($fp) #$t1 = i-1
	addi $t1, $t1, 1 #$t1 = i
	sll $t1, $t1, 2 #$t1 = i * 2^2
	add $t0, $t1, $t0 #$t0 = arr[i] address
	lw $t0, ($t0) #$t0 = arr[i]
	sw $t0, -16($fp)
	
	#PRINT the elements inside arr[i]
    	lw $a0, -16($fp) 
        addi $v0, $0, 1  
        syscall
	
	#Print space after arr[i]
	la $a0, space   
        addi $v0, $0, 4
        syscall
    	
	#Increment i by 1
	lw $t0, -4($fp)  # Load i 
	addi $t0, $t0, 1 # i = i + 1
	sw $t0, -4($fp)  # store i as i
	
	j main_loop # jump to main_loop


# The insertion_sort() function is faithfully translated by first assigning a variable of 
# length as the length of the arr argument.  

# This function consists of mainly five labels: insertion_sort, insertion_loop,
# while_loop, end_while_loop, and ra_main.

# The function utilizes nested loops to compare the element in the list with the 
# smallest index with each index to insert smaller element to the left, one by one.

# i has been initialized as 1 because the for loop inside the insertion sort ranged inbetween 1 to length

# Stack frame diagram for insertion_sort():
# length is at -16($fp)
# i is at -12($fp)
# j is at -8($fp)
# key is at -4($fp)
# the_length (arg 1) is at +8($fp)  
# saved $fp is at 0($fp) (by convention)
# saved $ra is at 4($fp) (by convention)

insertion_sort:
	#Save $ra and $fp into stack
	addi $sp, $sp, -8
	sw $ra, 4($sp)
	sw $fp, 0($sp)
	
	#copy $sp into $fp
	addi $fp, $sp, 0
	
	#Allocate space for local variables
	addi $sp, $sp, -16
	
	# Load length of the_list
	lw $t0, 8($fp)   # load arr
	lw $t0, ($t0)    # getting the heap 
	sw $t0, -16($fp) # Store the length inside as -16($fp)
	
	#initialize i = 1
	addi $t1, $0, 1
	sw $t1, -12($fp) # i = 1

# This loop first creates a variable length, then performs a for loop assigning key with the index element.
# This has the purpose to set the standard element that will be compared with the others.
 
# Stack frame diagram for insertion_loop:
# length is at -16($fp)
# i is at -12($fp)
# j is at -8($fp)
# key is at -4($fp)
# the_list is at 8($fp)
insertion_loop:
	
	# Loaded the length and i
	lw $t0, -16($fp) # $t0 = length
	lw $t1, -12($fp) # $t1 = i  
	
	# While i == length
	#slt $t2, $t0, $t1  
	beq $t0, $t1, ra_main # i == length, jump to ra_main
	
	#the_list[i]
	lw $t0, 8($fp)   # $t0 = address of the list
	lw $t1, -12($fp) # $t1 = i - 1 
	addi $t1, $t1, 1 # $t1 = i + 1
	sll $t1, $t1, 2  # $t1 = i * 2^2
	add $t0, $t1, $t0 # $t0 = address of the_list[i] 
	lw $t0, ($t0)    # $t0 = the_list[i]
	
	# Key = the_list[i]
	sw $t0, -4($fp)  
		
	#j = i-1
	lw $t0, -8($fp)  # $t0 = j
	lw $t1, -12($fp) # $t1 = i
	subi $t1, $t1, 1 #$t1 = i - 1
	sw $t1, -8($fp) # j = i-1
	
	j while_loop #jump to while loop

# This label performs a while loop with the condition of having j >= 0 and key < the_list[j]
# Then the label performs a loop to assign the next element as the current, and decrements J.
# So in the case of [6, -2, 7, 4, -10]. In the first step of the while loop, the list becomes
# [6, 6, 7, 4, -10]. The -2 is stored as key, and it will be implemented when the while loop ends.

# Stack frame diagram for insertion_loop:
# j is at -8($fp)
# key is at -4($fp)
# the_list is at 8($fp)
while_loop:
	# if j < 0, end loop
	lw $t0, -8($fp)  # $t0 = j
	slt $t1, $t0, $0  # 1: if j < 0
	bne $t1, $0, end_while_loop # if $t1 != 0 visit end_while_loop
	
	# if key < the_list[j], end loop
	# the_list[j]
	lw $t0, 8($fp) # $t0 = the_list address
	lw $t1, -8($fp) # $t1 = j - 1	
	addi $t1, $t1, 1 # $t1 = j
	sll $t1, $t1, 2 #$t1 = j * 2^2
	add $t0, $t0, $t1 # $t0 = address of the_list[j]
	lw $t0, ($t0) #$t0 = the_list[j]
	
	
	# key < the_list[j]
	lw $t1, -4($fp)
	slt $t2, $t1, $t0 # if (key < the_list[j]), $t2 = 1
	beq $t2, $0, end_while_loop # if $t2 == 0, then visit end_while_loop
	
 	
	# the_list[j+1] = the_list[j]
	# the_list[j]
	lw $t0, 8($fp) # $t2 = the_list address
	lw $t1, -8($fp) # $t3 = j - 1
	addi $t1, $t1, 1 # $t3 = j
	sll $t1, $t1, 2 #$t3 = j * 2^2
	add $t0, $t0, $t1 # $t2 = address of the_list[j]
 	lw $t2, ($t0) #$t2 = the_list
	
	#the_list[j+1]
	lw $t0, 8($fp) #$t0 = the_list address
	lw $t1, -8($fp) # $t1 = -8($fp)
	addi $t1, $t1, 2 # $t1 = j + 1
	sll $t1, $t1, 2 
	add $t0, $t1, $t0 # $t0 = the_list[j*1] address
	sw $t2, ($t0) # $t0 = the_list[j+1]

	
	# J -= 1
	lw $t0, -8($fp)   # $t0 = j
	addi $t0, $t0, -1 # $t0 = j - 1
	sw $t0, -8($fp)   # j = j-1
	
	j while_loop     # jump to while loop
	

#  This label implements the stored value to the list and swaps the elements.
# For example, [6, 6, 7, 4, -10] would become [-2, 6, 7, 4, -10]
# So, it places the smaller value to the left of the larger value (which is one index smaller)	
# Stack frame diagram for insertion_loop:
# j is at -8($fp)
# key is at -4($fp)
# i is at -12($fp)
# the_list is at 8($fp)
end_while_loop:	
	# Load key
	lw $t2, -4($fp)
	
	# Load the_list[j+1]
	lw $t0, 8($fp) #$t0 = the_list address
	lw $t1, -8($fp)  # $t1 = j - 1	 j = -2, -2, -2, -2
	addi $t1, $t1, 2 # $t1 = j + 1   
	sll $t1, $t1, 2 
	add $t0, $t1, $t0 # $t0 = the_list[j*1] address
	
	# the_list[j+1] = key
	sw $t2, ($t0) 
	
	#Increment i by 1
	lw $t0, -12($fp)
	addi $t0, $t0, 1
	sw $t0, -12($fp)
	
	#Loop back to insertion_loop
	j insertion_loop

# The ra_main label returns the sorted array of the_list to the main function as $v0.
# It also has a job to remove local variables and to restore $fp and $ra.

# Stack frame diagram for insertion_loop:
# the_list is at 8($fp)
ra_main:
	# Return list in sorted format
	lw $v0, 8($fp) #$v0 = arr
		
	#Remove local variables
	addi $sp, $sp, 16
	
	#Restore $fp and $ra
	lw $fp, 0($sp) #restore $fp
	lw $ra, 4($sp) #restore $ra
	addi $sp, $sp, 16 #destroy
	
	#Return to main
	jr $ra
	
# The print label translates the print() in the original python code.
# It adds a newline to replicate the functionality of print() in python. 
# It also has a job of ending the program.
print:	
	# print()
	addi $v0, $0, 4  
    	la $a0, newline   
    	syscall
	
	# End 
	addi $v0, $0, 10
        syscall
	

	
	


	
