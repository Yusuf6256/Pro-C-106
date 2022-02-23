import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    coffee_in_ml=[]
    sleep_in_hours = []
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            coffee_in_ml.append(float(row["Coffee in ml"]))
            sleep_in_hours.append(float(row["sleep in hours"]))
        
    return {"x":coffee_in_ml, "y":sleep_in_hours}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print("correlation between coffee and sleep in hours in a week",correlation[0,1])

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Coffee in ml", y="sleep in hours")
        fig.show()

def setup():
    data_path= "lI.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotfigure(data_path)