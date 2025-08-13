for row in range(10):
	for column in range(10):
		print('<' if row % 2 == 1 else '>', end='')
#both the outer loop and inner first print 10 10 times, so if row % 2 == 1 is moves < else >