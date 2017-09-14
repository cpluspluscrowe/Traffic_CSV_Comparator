import os
import pandas as pd
from pandas import read_csv
from pprint import pprint
import unittest
import numpy
import math
from Format_CSV import GetDataFrameFromCsv
data_path = r"C:\Users\CCrowe\Documents\Traffic\Cube\Compare_CSV\AM_OUT.csv"
counts_path = r"C:\Users\CCrowe\Documents\Traffic\Cube\Compare_CSV\Counts.csv"
speeds_path = r"C:\Users\CCrowe\Documents\Traffic\Cube\Compare_CSV\Speeds.csv"
data = GetDataFrameFromCsv(r"C:\Users\CCrowe\Documents\Traffic\Cube\Compare_CSV\AM_OUT.csv")
counts = read_csv(counts_path)
speeds = read_csv(speeds_path)

class Tester(unittest.TestCase):
    def __init__(self):
        self.numeric_columns = ["A","B","12:00 AM","12:15 AM","12:30 AM",
                            "12:45 AM","1:00 AM","1:15 AM","1:30 AM",
                            "1:45 AM","2:00 AM","2:15 AM","2:30 AM",
                            "2:45 AM","3:00 AM","3:15 AM","3:30 AM",
                            "3:45 AM","4:00 AM","4:15 AM","4:30 AM",
                            "4:45 AM","5:00 AM","5:15 AM","5:30 AM",
                            "5:45 AM","6:00 AM","6:15 AM","6:30 AM",
                            "6:45 AM","7:00 AM","7:15 AM","7:30 AM",
                            "7:45 AM","8:00 AM","8:15 AM","8:30 AM",
                            "8:45 AM","9:00 AM","9:15 AM","9:30 AM",
                            "9:45 AM","10:00 AM","10:15 AM","10:30 AM",
                            "10:45 AM","11:00 AM","11:15 AM","11:30 AM",
                            "11:45 AM","12:00 PM","12:15 PM","12:30 PM",
                            "12:45 PM","1:00 PM","1:15 PM","1:30 PM",
                            "1:45 PM","2:00 PM","2:15 PM","2:30 PM",
                            "2:45 PM","3:00 PM","3:15 PM","3:30 PM",
                            "3:45 PM","4:00 PM","4:15 PM","4:30 PM",
                            "4:45 PM","5:00 PM","5:15 PM","5:30 PM",
                            "5:45 PM","6:00 PM","6:15 PM","6:30 PM",
                            "6:45 PM","7:00 PM","7:15 PM","7:30 PM",
                            "7:45 PM","8:00 PM","8:15 PM","8:30 PM",
                            "8:45 PM","9:00 PM","9:15 PM","9:30 PM",
                            "9:45 PM","10:00 PM","10:15 PM","10:30 PM",
                            "10:45 PM","11:00 PM","11:15 PM","11:30 PM",
                            "11:45 PM","DISTANCE","SPEEDS1_2","SPEEDS2_2",
                            "SPEEDS3_2","SPEEDS4_2","SPEEDS5_2","SPEEDS6_2",
                            "SPEEDS7_2","SPEEDS8_2","SPEEDS9_2","SPEEDS10_2",
                            "SPEEDS11_2","SPEEDS12_2","SPEEDS13_2","VS1_2",
                            "VS2_2","VS3_2","VS4_2","VS5_2","VS6_2","VS7_2",
                            "VS8_2","VS9_2","VS10_2","VS11_2","VS12_2","VS13_2"]
    def TestValue(self,att,value):
        if att in self.numeric_columns:
            try:
                val = int(value)
                self.assertTrue(str(val).isnumeric())
            except:
                try:
                    if not numpy.isnan(value):
                        print("Not a number: " + str(value))
                except:
                    print("Not a number: " + str(value))


class Quantity():
    def __init__(self):
        pass
    def SetData(self,row,test):
        for att,value in zip(row._fields,row):
            test.TestValue(att,value)
            setattr(self,str(att),value)

def GetDataRows(data):
    test = Tester()
    data_rows = []
    for row in data.itertuples():
        q = Quantity()
        q.SetData(row,test)
        data_rows.append(q)
    return data_rows

def GetDataFrames():
    return {
'data_rows':GetDataRows(data),
'count_rows':GetDataRows(counts),
'speed_rows':GetDataRows(speeds)}










