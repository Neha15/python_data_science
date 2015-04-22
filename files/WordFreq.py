from collections import Counter
def Word_freq():
	fpath = open('/home/prodapt/Documents/documentation of tasks.txt')
	print Counter(fpath.read().split()).most_common()

Word_freq()