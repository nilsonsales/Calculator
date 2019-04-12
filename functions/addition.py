def addition(num1, num2):

	# Make sure num2's length is larger than num1's
	if len(num1)> len(num2): 
		temp = num1 
		num1 = num2 
		num2 = temp 

	# Create an empty string to store the result
	num3 = "" 

	# Calculate lenght of both strings and the difference
	l1 = len(num1) 
	l2 = len(num2) 
	l_diff = l2 - l1 

	# Initialy set carry as zero 
	carry = 0

	# Traverse from end of both strings 
	for i in range(l1-1,-1,-1): 
	
		# Compute the sum of digits and carry
		# (use 'ord' to get the int corresponding to the string)
		
		sum = ((ord(num1[i])-ord('0')) + int((ord(num2[i + l_diff])-ord('0'))) + carry) 
	
		num3 = num3 + str( sum % 10 ) 
		
		# Ignore the decimal part
		carry = sum//10

	# Add remaining digits of num2[] 
	for i in range(l2-l1-1, -1, -1): 
	
		sum = ((ord(num2[i])-ord('0'))+carry) 
		num3 = num3 + str( sum%10 ) 
		carry = sum//10

	# Add last carry, if it exist
	if (carry): 
		num3 + str(carry + '0') 

	# Reverse the string
	num3 = num3[::-1] 

	return num3 
