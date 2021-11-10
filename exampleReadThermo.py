from pandas.core.frame import DataFrame
from pythermo.thermoml.tools.readTools import readThermo
import json
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from collections import OrderedDict

def doArrhenius(df) -> DataFrame:
    """performs Arrhenius analyzation of given dataFrame

    Params:
        df: pandas dataframe of respective data report object

    Returns:
        Dataframe with ln(eta0) and Eeta of Arrhenius
    """

    moleFractions = df[['water', 'glycerol', 'choline chloride', 'urea', 'ethylene glycol', 'methanol', "N,N-Diethylethanolammonium chloride"]].values
    moleFractions = OrderedDict((tuple(x),x) for x in moleFractions).values()

    newData = []

    for molarRatio in moleFractions:
        
        filterDF = df[(df['water'] == molarRatio[0]) & (df['glycerol'] == molarRatio[1]) & (df['choline chloride'] == molarRatio[2]) & (df['urea'] == molarRatio[3]) & (df['ethylene glycol'] == molarRatio[4]) & (df['methanol'] == molarRatio[5]) & (df['N,N-Diethylethanolammonium chloride'] == molarRatio[6])]
        x = filterDF[['1/RT (mol/kj)']]
        y = filterDF[['ln(eta) (cP)']]

        # TODO: add components to new dataframe
        #components = list()
        #comp = df.columns[df.water.notna().any()].tolist()
        #print(comp)
        regressor = LinearRegression()
        regressor.fit(x,y)
        y_pred = regressor.predict(x)
        
        plt.scatter(x, y, alpha=0.5, label=molarRatio)
        plt.plot(x, y_pred, label=molarRatio)
        newData.append((df['DOI'].values[0], df['title'].values[0], df['authors'].values[0], molarRatio[0], molarRatio, regressor.intercept_[0], regressor.coef_[0][0], regressor.score(x,y)))

    newDataFrame = pd.DataFrame(newData, columns=['DOI', 'title', 'authors', 'xw', 'mole Fractions', 'ln(eta0) (cP)', 'Eeta', 'R^2'])
    newDataFrame = newDataFrame.sort_values(by=['xw'], ascending=True)
    plt.title(df['title'].values[0])
    plt.xlabel('1/RT (mol/kj)')
    plt.ylabel('ln(eta) (cP)')
    plt.legend()
    plt.grid()
    plt.show()
    
    return newDataFrame

def plotEeta(df):
    x = df.xw
    y = df.Eeta
    print(x)
    print(y)
    plt.scatter(x,y, alpha=0.5)
    plt.title(df['DOI'].values[0])
    plt.xlabel('xw')
    plt.ylabel('eEta')
    plt.legend()
    plt.grid()
    plt.show()

def plotEta0(df):
    x = df.xw
    y = df['ln(eta0) (cP)']
    print(x)
    print(y)
    plt.scatter(x,y, alpha=0.5)
    plt.title(df['DOI'].values[0])
    plt.xlabel('xw')
    plt.ylabel('ln(eta0)')
    plt.legend()
    plt.grid()
    plt.show()
if __name__ == "__main__":


    dataRep = readThermo("DataGudrunGygli/cml2ThermoML/ChCl_glycerol/ChCl_glycerol_DOI2.xml")

    df = dataRep.createDataFrame()
    x = doArrhenius(df)
    print(x)
    plotEeta(x)
    plotEta0(x)
