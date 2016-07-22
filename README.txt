In order to extract only the CPU idle % field, all that has to be done is to replace the file name in parse.sh
and run parse.sh as below

sh parse.sh

This will create files 1,2,3,4,5,6
these files will have timestamp and idle CPU%

These should then be filtered based on timestamps using time.py
*********************************************

The next thing to do is to filter based on timestamps, for this do as below:

edit time.sh with the time range on which to filter

then run as below:

sh time.sh

The output file is T1.csv

This is the file on which average has to be calculated and subtract the final results from 100 before plotting the graph

*************************************************