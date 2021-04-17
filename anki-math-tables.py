#!/usr/bin/env python3

# A python script to generate tables of addition, subtraction and division.

import csv

base_tags = "math math::tables math::tables::calculation"

with open('anki-math-tables.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)

    # Addition table from 1-20
    tags = base_tags + " " + "math::tables::calculation::addition"
    for i in range(1, 21):
        for j in range(1, 21):
            operation = str(i) + "+" + str(j)
            row = [operation, i, j, '+', i+j, tags]
            filewriter.writerow(row)
    
    # Subtraction table from 1-20
    tags = base_tags + " " + "math::tables::calculation::subtraction"
    for i in range(1, 21):
        for j in range(1, i):
            operation = str(i) + "-" + str(j)
            row = [operation, i, j, '-', i-j, tags]
            filewriter.writerow(row)
    
    # Multiplication from 1-20
    tags = base_tags + " " + "math::tables::calculation::multiplication"
    for i in range(1, 21):
        for j in range(1, 21):
            operation = str(i) + "x" + str(j)
            row = [operation, i, j, "x", i*j, tags]
            filewriter.writerow(row)
            
    # Division from 1-20
    tags = base_tags + " " + "math::tables::calculation::division"
    for i in range(1, 21):
        for j in range(2, i):
            if (i%j == 0):
                operation = str(i) + "/" + str(j)
                row = [operation, i, j, "/", i/j, tags]
                filewriter.writerow(row)
            else:
                operation = str(i) + "/" + str(j)
                answer = str(format(i/j, '.3f')) + ", mod=" + str(i%j)
                row = [operation, i, j, "/", answer, tags]
                filewriter.writerow(row)