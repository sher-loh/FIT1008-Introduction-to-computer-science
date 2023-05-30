#name: Daisuke Murakami, Fathin Acyuta Makarim, Lim Rui Shun, Loh Jing Wei
#date: 18th March 2022

		#The main function makes a list called my list with the numbers 2, 4, and 6 in it. 
		#The number three has been assigned to the variable n. 
		#It then invokes the get multiples method, which checks for multiples of n in the list my list, 
		#before returning to the main function to display the output.

		.data
		
prompt1:	.asciiz "The number of multiples of "
prompt2:	.asciiz " is: "

		.text
		
main:		# Stack frame diagram for main:
		# my_list is at -8($fp)
		# n is at -4($fp)

		#set $fp
		addi $fp, $sp, 0 #copy $sp into $fp
		
		#Alloc space for locals
		addi $sp, $sp, -8 #2 locals = 8 bytes

		#Initialize locals

		## my_list = [2,4,6]

		#initialize my_list of size 3
		addi $v0, $0, 9 # call code to allocate space for array
		addi $t0, $0, 4 # $t0 = 3(size of array) +1
		sll $a0, $t0, 2 # $a0 = (3 + 1)*4
		syscall
		sw $v0, -8($fp) 
		addi $t0, $0, 3 
		sw $t0, ($v0) # first element of my_list = 3 (size of array)
		
		lw $t0, -8($fp) #$t0 = Address of my_list
		addi $t1, $0, 2 
		sw $t1, 4($t0) #my_list[0] = 2
		addi $t1, $0, 4
		sw $t1, 8($t0) #my_list[1] = 4
		addi $t1, $0, 6
		sw $t1, 12($t0) #my_list[2] = 6
		
		## n = 3

		#initialize n
		addi $t0, $0, 3
		sw $t0, -4($fp) #n=37
		
		##print("The number of multiples of " + str(n) + " is: " + str(get_multiples(my_list, n)))
		
		#print("The number of multiples of ")
		la $a0, prompt1 #$a0 = address of prompt1
		addi $v0, $0, 4 #call code 4 (print string)
		syscall
		
		#print(str(n))
		lw $a0, -4($fp) #$a0 = n
		addi $v0, $0, 1 #call code 1 (print int)
		syscall
		
		#print(" is: ")
		la $a0, prompt2 #$a0 = address of prompt2
		addi $v0, $0, 4 #call code 4 (print string)
		syscall
		
		#Call function get_multiples
		#Alloc space for 2 arguments
		addi $sp, $sp, -8 # 2*4 = 8 bytes for two arguments
		
		#arg1 = my_list
		lw $t0, -8($fp) # load my_list
		sw $t0, 0($sp) # arg1 = my_list
		
		#arg2 = n
		lw $t0, -4($fp) #load n
		sw $t0, 4($sp) #arg2 = n
		
		#link and goto get_multiples
		jal get_multiples
		
		#Remove arguments
		addi $sp, $sp, 8 #2*4 = 8 bytes
		
		#print(get_multiples(my_list,n) - print count
		addi $a0, $v0, 0 #$a0 = count (from get_multiples)
		addi $v0, $0, 1
		syscall
		
		#Remove locals
		addi $sp, $sp, 8

		#exit
		addi $v0, $0, 10
		syscall
		
get_multiples:	# Stack frame diagram for get_multiples
		# count is at -8($fp)
		# i is at -4($fp)
		# saved fp is at ($fp)
		# saved ra is at +4($fp)
		# arg1(the_list) is at +8($fp)
		# arg2(n) is at +12($fp)

		#save $ra and $fp in stack
		addi $sp, $sp, -8 #make space for $ra and $fp
		sw $ra, 4($sp) #save $ra
		sw $fp, 0($sp) #save $fp
		
		#copy $sp to $fp
		addi $fp, $sp, 0
		
		#Alloc space for 2 local variables
		addi $sp, $sp, -8 #2*4 = 8 bytes
		
		#initialize local variables

		##count = 0
		#initialize count
		sw $0, -8($fp) #count = 0
		
		#initiliaze i
		sw $0, -4($fp) #i = 0
		
		
		
loop:		##for i in range(len(the_list)):
		#while i != size
		lw $t0, 8($fp) # $t0 = address of the_list
		lw $t0, ($t0) #$t0 = length of the_list (1st element)
		lw $t1, -4($fp) #$t1 = n
		beq $t0, $t1, ret_to_main #if i == size, jump to return_to_main
	
		##if the_list[i]%n == 0 and the_list != n:
		
		#if the_list[i] % n != 0, jump to increment_i
		lw $t0, 8($fp) # $t0 = address of the_list
		lw $t1, -4($fp) #$t1 = i - 1
		addi $t1, $t1, 1 # $t1 = i
		sll $t1, $t1, 2 # $t1 = i * 2^2
		add $t0, $t1, $t0 # $t0 = the_list[i] address
		lw $t0, ($t0) # $t0 = the_list[i] 
	
		lw $t1, 12($fp) #$t1 = n
		div $t0, $t1 #the_list[i]/n
		mfhi $t0 # $t0 = the_list[i]%n
		
		bne $t0, $0, increment_i #if the_list[i] % n != 0, jump to increment_i
	
		#if the_list[i] == n, jump to increment_i
		lw $t0, 8($fp) # $t0 = address of the_list
		lw $t1, -4($fp) # $t1 = i - 1
		addi $t1, $t1, 1 # $t1 = i
		sll $t1, $t1, 2 # $t1 = i * 2^2
		add $t0, $t1, $t0 # $t0 = the_list[i] address
		lw $t0, ($t0) # $t0 = the_list[i] 
		lw $t1, 12($fp) # $t1 = n
		beq $t0, $t1, increment_i # if the_list[i] == n, jump to increment_i
		
		##count += 1
		lw $t0, -8($fp)
		addi $t0, $t0, 1
		sw $t0, -8($fp)
	
increment_i:	#increment i 
 		lw $t1, -4($fp) #$t1 = i 
		addi $t1, $t1, 1 #$t1 = i+1
		sw $t1, -4($fp) #store i back to -4($fp)
		j loop
		
ret_to_main:	##return count
		#Return count in $v0
		lw $v0, -8($fp) #$v0 = count
		
		#Remove local var
		addi $sp, $sp, 8
		
		#Restore $fp and $ra
		lw $fp, 0($sp) #restore $fp
		lw $ra, 4($sp) #restore $ra
		addi $sp, $sp, 8 #deallocate
		
		#Return to caller (main function)
		jr $ra
		
		
		
		
		
		
		
		
		
		
		
				
		
		
		
		
		
		
		
		
		
		
