from data_getter import GetDataFrames
from Dictionaries import translatorAM,translatorPM,counts_dict
from pprint import pprint

canon = {}
cube = {}
data = GetDataFrames()

def GetTime(field):
    time = None
    if field in translatorAM:
        time = translatorAM[field]
    if field in counts_dict:
        time = counts_dict[field]
    return time
def GetFiller(field):
    if "VS" in field:
        filler = "V"
    elif "SPEED" in field:
        filler = "S"
    else:
        raise Exception("No valid filler found")
    return filler

def FillDictionary(data_name,dict_to_fill,filler = None):
    dr = data[data_name]
    for q in dr:
        for field in q:
            time = GetTime(field)
            if time:
                if filler == None:
                    filler_type = GetFiller(field)
                else:
                    filler_type = filler
                val = q[field]
                try:
                    key = str(int(q["A"])) + "-" + str(int(q["B"])) + "-{0}-".format(filler_type) + time
                    dict_to_fill[key] = val
                except:
                    key = str(q["A"]) + "-" + str(q["B"]) + "-{0}-".format(filler_type) + time
                    dict_to_fill[key] = val
FillDictionary("data_rows",cube)
FillDictionary("count_rows",canon,"V")
FillDictionary("speed_rows",canon,"S")
