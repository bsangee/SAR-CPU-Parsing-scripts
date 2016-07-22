#!/bin/bash
python time1.py amaranth1 $1 $2 > 1_1
python time2.py amaranth1 $2 $3 > 1_2
python time3.py amaranth1 $3 > 1_3

python time1.py amaranth4 $1 $2 > 1_4
python time2.py amaranth4 $2 $3 > 1_5
python time3.py amaranth4 $3 > 1_6

python time1.py amaranth6 $1 $2 >1_7
python time2.py amaranth6 $2 $3 >1_8
python time3.py amaranth6 $3 >1_9

python time1.py hulk2 $4 $5 >1_10
python time2.py hulk2 $5 $6 >1_11
python time3.py hulk2 $6 >1_12

python time1.py hulk3 $7 $8 >1_13
python time2.py hulk3 $8 $9 >1_14
python time3.py hulk3 $9 >1_15

python time1.py hulk4 $7 $8 > 1_16
python time2.py hulk4 $8 $9 > 1_17
python time3.py hulk4 $9 >1_18

paste 1_1 1_2 1_3 1_4 1_5 1_6 1_7 1_8 1_9 1_10 1_11 1_12 1_13 1_14 1_15 1_16 1_17 1_18 > T1.csv
