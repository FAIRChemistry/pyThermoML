from pythermo.thermoml.tools.readTools import readThermo
import json
import os
import numpy as np
from sklearn.linear_model import LinearRegression
import math as mth
import matplotlib.pyplot as plt


path = "DataGudrunGygli/cml2ThermoML/water"
R = 8.31446261815324/1000

def doArrhenius(path):
    # cluster all Data in one big dict, with key: filename, value: dataRep
    files = os.listdir(path)
    dataRepDict = dict()
    for elem in files:
        dataRepDict[elem] = json.loads(readThermo(path + "/" + elem).toJSON())
    
    tempdict = dict()
    viscdict = dict()

    for key in dataRepDict.keys():
        temps = []
        viscs = []
        for value in dataRepDict[key]["pureOrMixtureData"]["1"]["measurements"].values():
            #pure substance -> mole fraction at mixtures?
            
            temps.append(1/(value["variables"]["1"][0]["value"]*R))
            
            #convert to cP
            viscs.append(mth.log(value["properties"]["1"][0]["value"]*1000, mth.e))

        if len(temps) == len(viscs):
            print("sucessfully created " + str(len(temps)) + " datapoints")
        else:
            print("WARNING! Not same dimensions")
    
        tempdict[key] = temps
        viscdict[key] = viscs
        

    return tempdict, viscdict
    

def visualizeDatapoints(tempdict, viscdict):

    for key in tempdict.keys():
        
        x = np.array(tempdict[key])
        x = x.reshape(-1,1)
        y = np.array(viscdict[key])

        model = LinearRegression()
        model.fit(x,y)

        #print("infinit temperature:", model.intercept_)
        #print("slope: ", model.coef_)
        print("R2: ", round(model.score(x,y), 2))
        


        t = (min(x), max(x))
        #plt.text(0.4, -0.8, "R2 of " + str(key) + ": " + str(round(model.score(x,y), 2)) + "\n \n", horizontalalignment='center', verticalalignment='center')
        
        plt.scatter(x,y, alpha=0.5)
        plt.plot(t, model.predict(t), label=key)
    
    
    plt.grid()
    plt.title("arrhenius pure water")
    plt.xlabel("1/RT in [mol/KJ]")
    plt.ylabel("ln(eta) in [cP]")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    temps, viscs = doArrhenius(path)
    visualizeDatapoints(temps, viscs)
