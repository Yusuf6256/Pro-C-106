import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    size_of_tv=[]
    average_time_spent = []
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            average_time_spent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
        
    return {"x":size_of_tv, "y":average_time_spent}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print("correlation between size of tv and average time spent in a week",correlation[0,1])

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Size of TV", y="\tAverage time spent watching TV in a week (hours)")
        fig.show()

def setup():
    data_path= "ho.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotfigure(data_path)

setup()



