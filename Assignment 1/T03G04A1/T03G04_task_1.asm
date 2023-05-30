#name: Daisuke Murakami, Fathin Acyuta Makarim, Lim Rui Shun, Loh Jing Wei
#date: 18th March 2022

#the code below depicts an operation that the user must enter 3 integers (numbers, first divisor, second divisor) and result depends on the input which
#must satisfy the the conditions and will resulted different integers.
#We used mips instructions such as bne, to compare if condition is false for AND and jump directly to another block of code under the label 'elif'
#another instruction like beq that if either of the conditions is satisfied then jump to OR_satisfy which will add 1 into the divisor for that condition


#Initialising Global Variables
.data
	number: .asciiz "Enter the number:"
	first_divisor: .asciiz "Enter the first divisor: "
	second_divisor: .asciiz "Enter the second divisor: "
	divisor: .word 0
	num: .word 0
	f_divisor: .word 0
	s_divisor: .word 0
	x: .word 0
	y: .word 0
	output: .asciiz "\nDivisors: "
.text
	
	##number = int(input("Enter the number: "))
	#This code will show prompt on the terminal by the user for which they must be able to enter integers
	la $a0, number #$a = number
	addi $v0, $0, 4 #$v0 = 4
	syscall
	#Input for variable number
	#This block of code inputs integers that would be stored in the global varibale 'num'
	addi $v0, $0, 5 #$v0 = 5
	syscall
	sw $v0, num #$v0 = num
	
	
	##first_divisor = int(input("Enter the first divisor: "))
	#This block of code will show prompt on the terminal where the user be able to enter in integers
	la $a0, first_divisor #$a0 = first_divisor
	addi $v0, $0, 4 #$v0 = 4
	syscall
	#in this block of code, we are attempting to input value into first_divisor variable
	addi $v0, $0, 5 # $v0 = 5
	syscall
	sw $v0, f_divisor #$f_divisor = $v0
	
	
	##second_divisor = int(input("Enter the second divisor: "))
	#this block of code would print out group of strings on the terminal where it asks user to input integer for second_divisor
	la $a0, second_divisor #$a0 = second_divisor
	addi $v0, $0, 4 #$v0 = 4
	syscall 
	#second_divisor input
	#the purpose is to input an integer for second_divisor
	addi $v0, $0, 5 #$v0 = 5
	syscall
	sw $v0, s_divisor #s_divisor = $v0
	
	
	#arithmrtic operations
	#our calculation mostly consists of division and taking the remainder and compare their equavalence to 0
	lw $t0, num #$t0 = num
	lw $t1, f_divisor #$t1 = f_divisor
	lw $t2, s_divisor  #$t2 = s_divisor
	
	#this calculation divides num($t0) with f_divisor($1) and result would be mfhi (remainder) and store into new register $t3 under x variable
	div $t0, $t1 #num / f_divisor
	mfhi $t3 #$t3 = mfhi (remainder of num/f_divisor)
	sw $t3, x #$t3 = x
	
	#this calculation divides num($t0) with s_divisor($t2) and result will be mfhi (remainder) and store into new register $t4 under y variable
	div $t0, $t2 #num / s_divisor
	mfhi $t4 #$t4 = mfhi (remainder of num/s_divisor)
	sw $t4, y #$t4 = y
	
	
	##if number % first_divisor == 0 and number % second_divisor == 0: divisors = 2
	#condition for AND
	#This is a conditional block where we first need to compare both conidition must be (true) equavalent to zero (AND)
	#we compare if none of the integers in x($t0) and y($t1) is not equal to 0 which will then jump another label (not_AND_zero)
	#otherwise if both conditions are equal then will direct add 2 into $t2 which will be stored in divisor variable
	lw $t0, x #$t0 = x
	lw $t1, y #$t1 = y
	lw $t2, divisor #$t2 = divisor
	##if number % first_divisor == 0 and number % second_divisor == 0:
	bne $t0, $0, elif # $t0 != 0 then jump to elif
	bne $t1, $0, elif # $t1 != 0 then jump to elif
	addi $t2, $t2, 2 #$t2 = $t2 + 2
	##divisors = 2
	sw $t2, divisor
	
	j end #jump directly to label end, skipping other conditions otherwise will add divisors all together
	
	
	#elif number % first_divisor == 0 or number % second_divisor == 0:
	#in this block, we are comparing if either x or y contains remainder 0
	#if one of their remainder equals to zero, then will jump to another label 'success', otherwise divisor will store value 0 which doesn't satify any of the conditions
	elif:
	lw $t0, x #$t0 = x
	lw $t1, y #$t1 = y
	lw $t2, divisor #$t2 = divisor
	beq $t0, $0, OR_Satisfy #$t0 == 0 jump to OR_Satisfy
	beq $t1, $0, OR_Satisfy #$t1 == 0 jump to OR_Satisfy
	
	
	##else: 
		#divisors = 0
	sw $0, divisor #divisor = 0
	
	j end #jump directly to label end
	
	
        #Under the label 'OR_satisfy' this is when the OR condition is safisfied, either x or y is equal to 0
        #we load the divisor and direct add 1 into the variable and store back in divisor
        OR_Satisfy:
        lw $t0, divisor #$t0 = divisor
        addi $t0, $t0, 1 #$t0 = $t0 + 1
        sw $t0, divisor #divisor == 1
        
        j end #jump directly to end  
        
        
	##print("\nDivisors: " + str(divisors))
	end:
	#printing output prompt
	la $a0, output #$a0 = output
	addi $v0, $0, 4 #$v0 = 4
	syscall	
	#printing divisor
	lw $a0, divisor #$a0 = divisor
	addi $v0, $0, 1 #$v0 = 1
	syscall	
	#exit program
	addi $v0, $0, 10 #$v0 = 10
	syscall #exit
