# GStar Navigation -- What happened to OnStar, people ask... GStar -- Like no Other
# Gerrit van Rensburg A.K.A. Hadreezy
# BattleSnake 20-17



#"coords": 
coords = [[3,0], [3,2], [3,3], [3,1], [3,0], [3,4], [3,5], [3,2]]


# Initializing count variable for X column
xC = 0

# Initializing count variable for Y column
yC = 0

head = coords[1][1]
print head


# For loop working through a snakes array of values to find the 'kinks'
# Where snakeBody is the body of the snake (coords), excluding the head (hence body). 


# for l1, l2 in snakeBody(coords, coords[1:]):
for l1, l2 in zip(coords, coords[1:]):
	if l1[:] == l2[:]:
		print l1[:], l2[:]
		# print 'l1[0]:',l1[0], 'l1[1]:', l1[1],'l2[0]:', l2[0], 'l2[1]:', l2[1]
		print "There's a dupe!"
	if l1[:] != l2[:]:
		print 'Mismatch:', l1[:], l2[:]
	
# Looking in the X column (1st column '[X, y]') 		
print "X Column Search Results:"
for x1, x2 in zip(coords[1:], coords[1:]):
	if x1[:] == x2[:]:
		print x1[:], x2[:]
		# print 'l1[0]:',l1[0], 'l1[1]:', l1[1],'l2[0]:', l2[0], 'l2[1]:', l2[1]
		print "There's a 'X' match!"
	if x1[:] != x2[:]:
		print 'Mismatch:', x1[:], x2[:]

# Increment X column counter to find which X column index has a kink
	xC = xC + 1
print xC
	
# Looking in the Y column (1st column '[X, y]') 		
print "Y Column Search Results:"
for y1, y2 in zip(coords[:1], coords[:1]):
	if y1[:] == y2[:]:
		print y1[:], y2[:]
		# print 'l1[0]:',l1[0], 'l1[1]:', l1[1],'l2[0]:', l2[0], 'l2[1]:', l2[1]
		print "There's a 'Y' dupe!"
	if y1[:] != y2[:]:
		print 'Mismatch:', y1[:], y2[:]

# Increment Y column counter to find which Y column index has a kink
	yC = yC + 1
print yC
	
	
# If Statement checks if there are 'kinks' in the the snake
# Variable my_list represents a snakes array 
# if len(set(my_list)) < len(my_list):
    
    
    
    
    	
    
    
    