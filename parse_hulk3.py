# open file to read
import sys
f = file(sys.argv[1], 'r')
count=0
flag=0
first_line=0
# iterate over the lines in the file
for line in f:
    if first_line==0:
        f.next()
        first_line=1
    if flag>1:
	for x in range(0, 17):
		f.next()
        flag=0
	count=0		
    # split the line into a list of column values
    columns = line.split(' ')
    # clean any whitespace off the items
    columns = [col.strip() for col in columns]
    # ensure the column has at least one value before printing
    if columns and count<=2:
    	print  columns[0]  + " " +columns[-1]# print the first column
	if count<=2:
		count=count+1
		flag=flag+1
	
		
			
