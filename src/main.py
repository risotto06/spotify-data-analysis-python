import os
from glob import glob
import zipfile
from pandas import json_normalize
import pandas as pd
import json

def data_retreaval():
    global initiated_data_retreaval
    initiated_data_retreaval = "dasda"
    unzipped_dir = "..\\data\\unzipped"
    zipdir = "..\\data\\zipped"
    zipname = os.listdir(zipdir)
    global jsonfiles
    jsonfiles = []

    with zipfile.ZipFile(zipdir + "\\" + str(zipname[0]), 'r') as zip_ref:
        zip_ref.extractall(unzipped_dir)

    for file in glob("..\\data\\unzipped\\**\\*History*.json"):
        jsonfiles.append(file)
    print(jsonfiles)

def data_management():
    try:
        initiated_data_retreaval
    except NameError:
        print("nooooooo")
        data_retreaval()
    else:
        print("yeeeeees")

    frame = []
    for files in jsonfiles:
        df = pd.read_json(files)
        frame.append(df)
    global df_total
    df_total = pd.concat(frame)
    print(df_total.head())
    print(df_total.info())

if __name__ == "__main__":
    data_retreaval()
    data_management()