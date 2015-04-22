
import csv
def read_file(file):
	reader = csv.reader(f)
    	for row in reader:
    		print row
#Reading the csv File
with open('/home/user/Desktop/test.csv', 'rt') as f:
	read_file(f)


#Writing the csv FIle
with open('/home/user/Desktop/test1.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow( ('Name', 'Age', 'Place') )
    writer.writerow( ('Athi', '21','Madurai'))
    writer.writerow( ( 'Neha', '23', 'Dehradun'))
f=open('/home/user/Desktop/test1.csv', 'rt')
read_file(f)