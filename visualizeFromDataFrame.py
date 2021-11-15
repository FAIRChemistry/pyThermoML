from pandas.core.frame import DataFrame
from pythermo.thermoml.tools.readTools import readThermo
import json
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
from collections import OrderedDict
from createDataFrame import createDataFrame

def doArrhenius(df):
    """
    performs Arrhenius analyzation of given dataFrame

    Params:
        df: pandas dataframe of respective data report object

    Returns:
        Dataframe with ln(eta0) and Eeta of Arrhenius
        String that describes components used in simulation (sperated with _)
        
    """
    

    moleFractions = df[['water', 'glycerol', 'choline chloride', 'urea', 'ethylene glycol', 'methanol', "N,N-Diethylethanolammonium chloride"]].values
    moleFractions = OrderedDict((tuple(x),x) for x in moleFractions).values()

    newData = []

    fig = plt.figure()
    ax = plt.subplot(111)
    
    components = list()
    if df['water'].values[0] != "NaN":
        components.append('water')
    if df['glycerol'].values[0] != "NaN":
        components.append('glycerol')
    if df['choline chloride'].values[0] != "NaN":
        components.append('choline chloride')
    if df['urea'].values[0] != "NaN":
        components.append('urea')
    if df['methanol'].values[0] != "NaN":
        components.append('methanol')
    if df['ethylene glycol'].values[0] != "NaN":
        components.append('ethylene glycol')
    if df['N,N-Diethylethanolammonium chloride'].values[0] != "NaN":
        components.append('N,N-Diethylethanolammonium chloride')
            
    componentString = ""
    for comp in components:
        
        componentString += str(comp) + "_"
    
    
    componentString = componentString.rstrip(componentString[-1])
    
    for molarRatio in moleFractions:
        
        filterDF = df[(df['water'] == molarRatio[0]) & (df['glycerol'] == molarRatio[1]) & (df['choline chloride'] == molarRatio[2]) & (df['urea'] == molarRatio[3]) & (df['ethylene glycol'] == molarRatio[4]) & (df['methanol'] == molarRatio[5]) & (df['N,N-Diethylethanolammonium chloride'] == molarRatio[6])]
        x = filterDF[['1/RT (mol/kj)']]
        y = filterDF[['ln(eta) (cP)']]


        regressor = LinearRegression()
        regressor.fit(x,y)
        y_pred = regressor.predict(x)
        
        plt.scatter(x, y, alpha=0.5)
        plt.plot(x, y_pred, label=molarRatio)
        newData.append((df['DOI'].values[0], df['title'].values[0], df['authors'].values[0], molarRatio[0], molarRatio, regressor.intercept_[0], regressor.coef_[0][0], regressor.score(x,y)))

    newDataFrame = pd.DataFrame(newData, columns=['DOI', 'title', 'authors', 'xw', 'mole Fractions', 'ln(eta0) (cP)', 'Eeta', 'R^2'])
    newDataFrame = newDataFrame.sort_values(by=['xw'], ascending=True)
    box = ax.get_position()
    ax.set_position([box.x0, box.y0 + box.height * 0.1,
                 box.width, box.height * 0.9])
    ax.set_title(df['title'].values[0])
    ax.set_xlabel('1/RT (mol/kj)')
    ax.set_ylabel('ln(eta) (cP)')
    ax.legend(title="Mole fraction of components: \n water, glycerol, choline chloride, urea, ethylene glycol, methanol, N,N-Diethylethanolammonium chloride", loc='upper center', bbox_to_anchor=(0.5, -0.2), fancybox=True)
    ax.grid()
    
    fig.savefig("./plots/" + "arrhenius_plots_"+ componentString + ".jpg", bbox_inches="tight")
    
    return newDataFrame, componentString

def plotArrhenius(df, componentString):
    """
    creates plot of eEta over xw
    
    Params:
        df: pandas dataframe in which values vor eEta and xw are stored
        componentString: string of components
        
    """
    # TODO: plots next to each other
    fig, ax = plt.subplots(1, 2, figsize=(13,4), dpi=300)
    
    x = df.xw
    y = df.Eeta
    x = pd.to_numeric(x)
    y = pd.to_numeric(y)
    ax[0].scatter(x,y, alpha=0.5)
    ax[0].plot
    #ax[0].set_title(df['title'].values[0], pad=20)
    ax[0].set_xlabel('xw')
    ax[0].set_ylabel('eEta')
    ax[0].legend()
    ax[0].grid()

    
    x = df.xw
    y = df['ln(eta0) (cP)']
    x = pd.to_numeric(x)
    y = pd.to_numeric(y)
    ax[1].scatter(x,y, alpha=0.5)
    ax[1].set_xlabel('xw')
    ax[1].set_ylabel('ln(eta0)')
    ax[1].legend()
    ax[1].grid()
    
    fig.tight_layout()
    fig.savefig("./plots/" + "arrhenius_"+ componentString + ".jpg", bbox_inches="tight")
 
if __name__ == "__main__":


    dataRep = readThermo("DataGudrunGygli/cml2ThermoML/glycerol/glycerol_DOI1.xml")

    df = createDataFrame(dataRep)
    (x, comps) = doArrhenius(df)
    
    plotArrhenius(x, comps)
