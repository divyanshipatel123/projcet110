import pandas as pd
import csv 
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go 
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
population_SD = statistics.stdev(data)

def randomSetOfMeans(counter):
    dataset = []
    for i in range(0 , counter):
        randIndex = random.randint(0 , len(data) - 1)
        val = data[randIndex]
        dataset.append(val)
    mean = statistics.mean(dataset)
    return mean
meanList = []
def setup():
    
    for i in range(0,100):
        setOfmeans = randomSetOfMeans(30)
        meanList.append(setOfmeans)

    mean_Sample_dist = statistics.mean(meanList)
    sd_Sample_dist = statistics.stdev(meanList)
    print(population_mean , " is the mean of the population")
    print(mean_Sample_dist , " is the mean of the sampling distribution")
    print(sd_Sample_dist, " is the standard deviation of the sampling distribution")
    showPlot()

def showPlot():
    fig = ff.create_distplot([meanList] , ["reading time of the articles"] , show_hist= False)
    fig.show()

setup()