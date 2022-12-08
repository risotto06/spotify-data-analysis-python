import os
from glob import glob
import zipfile
from pandas import json_normalize
import pandas as pd
import json

# Standard plotly imports
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go
from plotly.offline import iplot, init_notebook_mode
import cufflinks
cufflinks.go_offline(connected=True)
init_notebook_mode(connected=True)


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
    global initiated_data_management
    initiated_data_management = "00123100"

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

def msSong():
    global df_total

    try:
        initiated_data_management
    except NameError:
        data_management()

    df_total = df_total.drop("endTime", axis=1)
    df_total = df_total.groupby(['trackName', 'artistName'], as_index=False)['msPlayed'].sum()
    df_total.sort_values(by=['msPlayed'], inplace=True, ascending=False)
    print(df_total.head())
    print(df_total.info())

def msArtist():
    pass

def msTotal():
    pass

def ploter():
    global df_total
    df_total["msPlayed"].iplot(kind='hist', xTitle='ms', yTitle='count', title='songms')

if __name__ == "__main__":
    data_retreaval()
    data_management()
    ploter()