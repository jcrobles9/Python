def palindrome(string):

	string_rev = string[::-1]  # This is extended slice syntax. It works by
	# doing [begin:end:step] and by leaving begin and end off with a step of -1, 
	# it reverses a string.
	
	if string == string_rev: return True # Then we compare the original string
	else: return False                   # with the reversed string.
	
print "Enter a string to test if it's a Palindrome:"
string = raw_input("> ")

print palindrome(string)
