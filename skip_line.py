# open file to read
import sys
f = file(sys.argv[1], 'r')
# iterate over the lines in the file
for line in f:
    # split the line into a list of column values
    columns = line.split(' ')
    # clean any whitespace off the items
    columns = [col.strip() for col in columns]
    # ensure the column has at least one value before printing
    if columns:
	f.next()
        print  columns[0]  + " " +columns[-1]# print the first column


