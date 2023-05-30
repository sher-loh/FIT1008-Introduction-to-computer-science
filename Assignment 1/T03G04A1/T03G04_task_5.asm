#tutorial: 3
#group: 4
#name: Daisuke Murakami, Fathin Acyuta Makarim, Lim Rui Shun, Loh Jing Wei
#date: 18th March 2022

		#The main function creates the arr list, which contains the numbers 1, 5, 10, 11, and 12. 
		#The variable index is set to the return value of the binary search function 
		#with the parameters list arr, 11, 0, and len(arr)-1. 
		#The binary search function returns the index of the target integer value in the arr list 
		#using the arguments the list, target, low, and high. 
		#The function returns -1 if the target value is not found in the arr list. 
		#The value stored in the variable index is then printed.
		
		.data

		.text
main:		# Stack frame diagram for main:
		# arr is at -8($fp)
		# index is at -4($fp)
		
		#set $fp and make space for locals
		addi $fp, $sp, 0 #copy $sp into $fp
		addi $sp, $sp, -8 #2 locals = 8 bytes
		
		## arr= [1,5,10,11,12]
		#Initialize locals
		#initialize arr of size 5
		addi $v0, $0, 9 # call code to allocate space for array
		addi $t0, $0, 6 # $t0 = 5(size of array) +1
		sll $a0, $t0, 2 # $a0 = (5 + 1)*4
		syscall
		sw $v0, -8($fp) 
		addi $t0, $0, 5
		sw $t0, ($v0) # first element of arr = 5 (size of array)
		
		lw $t0, -8($fp) #$t0 = Address of arr
		addi $t1, $0, 1 
		sw $t1, 4($t0) #arr[0] = 1
		addi $t1, $0, 5
		sw $t1, 8($t0) #arr[1] = 5
		addi $t1, $0, 10
		sw $t1, 12($t0) #arr[2] = 10
		addi $t1, $0, 11
		sw $t1, 16($t0) #arr[3] = 11
		addi $t1, $0, 12
		sw $t1, 20($t0) #arr[4] =12
		
		## index = binray_search(arr, 11, 0, len(arr) - 1)
		#Alloc space for 4 arguments
		addi $sp, $sp, -16 # push 4*4 = 16 bytes for 4 arguments
		
		#arg1 = arr
		lw $t0, -8($fp) # load arr
		sw $t0, 0($sp) # arg1 = arr 
		
		#arg2 = 11
		addi $t0, $0, 11  # $t0 = 11
		sw $t0, 4($sp) # arg2 = 11
		
		#arg3 = 0
		addi $t0 , $0, 0 # $t0 = 0
		sw $t0, 8($sp) # arg3 = 0
		
		#arg4 = len(arr) - 1
		lw $t0, -8($fp) # $t0 = address of arr
		lw $t0, ($t0) # $t0 = first element of arr (size)
		addi $t0, $t0, -1 # $t0 = size of arr - 1
		sw $t0, 12($sp) # arg4 = 4
		
		#link and go to binary_search
		jal binary_search
		
		#store return value in index
		sw $v0, -4($fp) 
		
		##print(index)
		addi $v0, $0, 1 
		lw $a0, -4($fp)
		syscall
		
		#end
		addi $v0, $0, 10
		syscall
		
binary_search:	# Stack frame for binary_search:
		# mid is at -4($fp)
		# saved fp is at ($fp)
		# saved ra is at +4($fp)
		# arg1(the_list) is at +8($fp)
		# arg2(target) is at +12($fp)
		# arg3(low) is at +16($fp)
		# arg4(high) is at +20($fp)

		#save $ra and $fp in stack
		addi $sp, $sp, -8
		sw $ra, 4($sp)
		sw $fp, 0($sp)
		
		#copy $sp to $fp
		addi $fp, $sp, 0
		
		#allocate local variable
		addi $sp, $sp, -4 #1 local = 4 bytes
		
		## if low > high:
		lw $t0, 16($fp) # $t0 = low
		
		lw $t1, 20($fp) # $t1 = high
		slt $t0, $t1, $t0 # if high < low, $t0 = 1
		beq $t0, $0, else #if low > high, jump to else
		
		## return -1
		addi $v0, $0, -1
		
		#jump to end_if
		j end_if
		
else:		## else:
		## mid = (high + low) // 2
		lw $t0, 16($fp) # $t0 = low
		lw $t1, 20($fp) # $t1 = high
		add $t0, $t0, $t1 # $t0 = high + low
		addi $t1, $0, 2 # $t1 = 2
		div $t0, $t1 # (high + low)/2
		mflo $t0 # $t0 = (high + low)//2
		sw $t0, -4($fp) # mid = (high + low)//2
		
		## if the_list[mid] == target:
		lw $t0, 8($fp) # $t0 = address of arr
		lw $t1, -4($fp) # $t1 = mid - 1
		addi $t1, $t1, 1 # $t1 = (mid - 1) + 1
		sll $t1, $t1, 2 # $t1 = i * 2^2
		add $t0, $t0, $t1 # $t0 = the_list[mid] address
		lw $t0, ($t0)    # $t0 = the_list[mid]
		lw $t1, 12($fp) # $t1 = target
		bne $t0, $t1, elif # if the_list[mid] != target, jump to elif
		
		## return mid
		lw $v0, -4($fp) # $v0 = mid
		#jump to end_if
		j end_if
		
elif:		## elif the_list[mid] > target:
		lw $t0, 8($fp) # $t0 = address of arr
		lw $t1, -4($fp) # $t1 = mid - 1
		addi $t1, $t1, 1 # $t1 = (mid - 1) + 1
		sll $t1, $t1, 2 # $t1 = i * 2^2
		add $t0, $t0, $t1 # $t0 = the_list[mid]
		lw $t0, ($t0)
		lw $t1, 12($fp) # $t1 = target
		slt $t0, $t1, $t0 # if target < the_list[mid], $t0 = 1
		beq $t0, $0, else2 # if target >= the_list[mid], jump to else2 
		
		## return binary_search(the_list, target, low, mid -1)
		#recursive call - alloc space for 4 arguments
		#4*4 = 16 bytes arg
		addi $sp, $sp, -16 #alloc space
		
		#arg1 = arr
		lw $t0, 8($fp) # load the_list
		sw $t0, 0($sp) # arg1 = the_list
		
		#arg2 = 11
		lw $t0, 12($fp) # $t0 = target
		sw $t0, 4($sp) # arg2 = target
		
		#arg3 = 0
		lw $t0, 16($fp) # $t0 = low
		sw $t0, 8($sp) # arg3 = low
		
		#arg4 = mid - 1
		lw $t0, -4($fp) # $t0 = mid
		addi $t0, $t0, -1 # $t0 = mid - 1
		sw $t0, 12($sp) # arg4 = mid - 1
		
		#call binary_search
		jal binary_search
		
		#deallocate arguments
		addi $sp, $sp, 16
		
		j end_if
		
else2:		## else:
		## return binary_search(the_list, target, mid + 1, high)
		#recursive call
		#4*4 = 16 bytes arg
		addi $sp, $sp, -16 #alloc space
		
		
		#arg1 = arr
		lw $t0, 8($fp) # load the_list
		sw $t0, 0($sp) # arg1 = the_list
		
		#arg2 = 11
		lw $t0, 12($fp) # $t0 = target
		sw $t0, 4($sp) # arg2 = target
		
		#arg3 = mid + 1
		lw $t0, -4($fp) # $t0 = mid - 1 
		add $t0, $t0, 1 # $t0 = mid + 1
		sw $t0, 8($sp) # arg3 = mid + 1
		
		
		#arg4 = high
		lw $t0, 20($fp) # $t0 = high
		sw $t0, 12($sp) # arg4 = high
		
		#call binary_search
		jal binary_search
		
		#deallocate arguments
		addi $sp, $sp, 16
		
end_if:		#function return
		#Deallocate local variable
		addi $sp, $sp, 4
		#Restore $fp and $ra
		lw $ra, 4($sp) #restore $ra
		lw $fp, 0($sp) #restore $fp
		addi $sp, $sp, 8 # deallocate
		#return 
		jr $ra
		
		
		
		
		
		
		
		
		
		
		
		
