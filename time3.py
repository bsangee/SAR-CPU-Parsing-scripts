import sys
filename = sys.argv[1]
t1 = sys.argv[2]
# open file to read
f = file(filename, 'r')
count=0
flag=0
# iterate over the lines in the file
for line in f:
    # split the line into a list of column values
    columns = line.split(' ')
    # clean any whitespace off the items
    columns = [col.strip() for col in columns]
    # ensure the column has at least one value before printing
    if columns[0] > t1:
    	print  columns[-1]# print the first column
