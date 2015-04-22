def file_count():
	file_path = open('/home/prodapt/Documents/documentation of tasks.txt')
	num_lines = sum(1 for line in file_path if line.rstrip('\n'))
	print num_lines

file_count()