import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    marks_in_percentage=[]
    days_present = []
    with open(data_path) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for row in csv_reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))
        
    return {"x":marks_in_percentage, "y":days_present}

def findCorrelation(dataSource):
    correlation=np.corrcoef(dataSource['x'],dataSource['y'])
    print("correlation between marks and days present in a scholastic year",correlation[0,1])

def plotfigure(data_path):
    with open(data_path) as csv_file:
        df=csv.DictReader(csv_file)
        fig=px.scatter(df,x="Marks In Percentage", y="Days Present")
        fig.show()

def setup():
    data_path= "fi.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotfigure(data_path)

setup()



