import pandas as pd
from pandas import read_csv
import csv
import math

def GetDataFrameFromCsv(csv_path):
    nan_value = float('nan')
    new_path = csv_path[:-4] + "_revised" + ".csv"

    with open(csv_path,'r') as csvfile:
        with open(new_path,'w') as csvNew:
            reader = csv.reader(csvfile,delimiter=',')
            writer = csv.writer(csvNew, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                new_row = row[0:6] + row[108:138]
                if len(new_row) == 36:
                    writer.writerow(new_row)


    data = read_csv(new_path,names = ['A','B','SPEED','FCLASS','LANES','DISTANCE',
                                  'SPEEDS1_2','SPEEDS2_2','SPEEDS3_2','SPEEDS4_2','SPEEDS5_2','SPEEDS6_2','SPEEDS7_2','SPEEDS8_2','SPEEDS9_2','SPEEDS10_2',
                                  'SPEEDS11_2','SPEEDS12_2','SPEEDS13_2','SPEEDS14_2','SPEEDS15_2','VS1_2','VS2_2','VS3_2','VS4_2','VS5_2','VS6_2','VS7_2','VS8_2',
                                  'VS9_2','VS10_2','VS11_2','VS12_2','VS13_2','VS14_2','VS15_2'])
    return data

if __name__ == '__main__':
    data = GetDataFrameFromCsv(r"C:\Users\CCrowe\Documents\Traffic\Cube\Compare_CSV\AM.csv")
