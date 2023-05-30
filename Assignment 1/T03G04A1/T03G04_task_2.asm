#name: Daisuke Murakami, Fathin Acyuta Makarim, Lim Rui Shun, Loh Jing Wei
#date: 18th March 2022

	#The code takes the length of the array inputed from the user and stores it in the variable,  size. 
	#The variable size is used to create a list named the_list. 
	#The variable n is filled with a user input. 
	#The count variable is set to 0 by default. 
	#The user adds values to the list during the for loop. 
	#Count is incremented by one if the_list entry is not divisible by n and not equal to n. 
	#In the end, the function returns the number of multiples in the_list that do not include itself.
	
	.data
	
size: 	.word 0
n: 	.word 0
count:	.word 0
the_list:.word 0
i:	.word 0
prompt1:.asciiz "Enter array length: "
prompt2:.asciiz "Enter n: "
prompt3:.asciiz "Enter the value: "
prompt4:.asciiz "\nThe number of multiples (excluding itself) = "

	.text

	##size = int(input("Enter array length: ")) 
	#print("Enter array length: ")
	addi $v0, $0, 4
	la $a0, prompt1
	syscall
	#size=int(input())
	addi $v0, $0, 5
	syscall
	sw $v0, size # size = int input by user
	
	##the_list = [None]*size
	addi $v0, $0, 9 # call code to allocate space for array
	lw $t0, size
	addi $t0, $t0, 1 # $t0 = size + 1 (first item in array indicate length of array)
	sll $a0, $t0, 2 # $a0 = (size + 1)*4
	syscall
	sw $v0, the_list # the_list = address of array
	lw $t0, size 
	sw $t0, ($v0) # first element of the_list = size 
	
	##n = int(input("Enter n: "))
	#print("Enter n: ")
	addi $v0, $0, 4
	la $a0, prompt2
	syscall
	#n = int(input())
	addi $v0, $0, 5
	syscall
	sw $v0, n # n = int input by user
	
loop:	##for i in range(len(the_list)):
	#while i != size
	lw $t0, size
	lw $t1, i
	beq $t0, $t1, end_loop #if i == size, jump to end_loop
	
	##the_list[i] = int(input("Enter the value: "))
	#print("Enter the value: ")
	addi $v0, $0, 4
	la $a0, prompt3
	syscall
	
	#input into the_list[i]
	lw $t0, the_list #$t0 = address of the_list
	lw $t1, i # $t1 = i - 1
	addi $t1, $t1, 1 # $t1 = i
	sll $t1, $t1, 2 # $t1 = i * 2^2
	add $t0, $t1, $t0 # t0 = the_list[i] address

	addi $v0, $0, 5 # call code 5 to input integer
	syscall
	sw $v0, ($t0) # the_list[i] = int input by user

	##if the_list[i] % n == 0 and the_list[i] != n:

	#the_list[i] % n
	lw $t0, the_list # $t0 = address of the_list
	lw $t1, i #$t1 = i - 1
	addi $t1, $t1, 1 # $t1 = i
	sll $t1, $t1, 2 # $t1 = i * 2^2
	add $t0, $t1, $t0 # $t0 = the_list[i] address
	lw $t0, ($t0) # $t0 = the_list[i] 
	lw $t1, n # $t1 = n
	div $t0, $t1
	mfhi $t0 # $t0 = the_list[i]%n
	
	#if the_list[i] % n != 0, jump to increment_i
	bne $t0, $0, increment_i
	
	#if the_list[i] == n, jump to increment_i
	lw $t0, the_list # $t0 = address of the_list
	lw $t1, i # $t1 = i - 1
	addi $t1, $t1, 1 # $t1 = i
	sll $t1, $t1, 2 # $t1 = i * 2^2
	add $t0, $t1, $t0 # $t0 = the_list[i] address
	lw $t0, ($t0) # $t0 = the_list[i]
	lw $t1, n # $t1 = n
	beq $t0, $t1, increment_i 
	
	##count += 1
	lw $t0, count
	addi $t0, $t0, 1
	sw $t0, count
	
increment_i:	#i += 1
	 	lw $t1, i
		addi $t1, $t1, 1
		sw $t1, i
		j loop
	
		
end_loop:	##print("\nThe number of multiples (excluding itself) = ") + str(count)
		addi $v0, $0, 4
		la $a0, prompt4
		syscall
		lw $a0, count
		addi $v0, $0, 1
		syscall	
		
		#end program
		addi $v0, $0, 10
		syscall
