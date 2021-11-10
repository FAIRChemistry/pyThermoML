import pandas as pd
import os
import numpy as np
from pythermo.thermoml.core import datareport
from pythermo.thermoml.tools.readTools import readThermo
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import plotly.express as px


R = 8.31446261815324/1000

def __transformViscosity__(eta):
    return np.log(eta*1000)


def __tranformTemperature__(temperature):
    return 1 / (R*temperature)

def createDataFrame():
  

    fileList = os.listdir(os.getcwd() + "/DataGudrunGygli/cml2ThermoML/")

    data = list()
    DOIs = []
    for files in fileList:
        subFilelist = os.listdir(os.getcwd() + "/DataGudrunGygli/cml2ThermoML/" + files)
       
        for filename in subFilelist:

            if ".xml" in filename:
                # Load ThermoML
                dataReport = readThermo(os.getcwd() + "/DataGudrunGygli/cml2ThermoML/" + files + "/" + filename)
                
                # extract general information
                doi = dataReport.DOI
                print(type(doi))
                print(DOIs)
                if doi not in DOIs:
                    DOIs.append(doi)
                title = dataReport.title
                authors = dataReport.authors
                authors = [author for author in authors.values()]
                
                # extract fraction information
                pom = dataReport.getPureOrMixtureData("1")
                comps = list()
                
                for comp in dataReport.getCompDict().values():
                    comps.append(comp.commonName)

                measDict = pom.getMeasurementsList()
                
                for index, meas in enumerate(measDict):
                    
                    moleFractions = []
                    for i in range(7):
                        moleFractions.append("NaN")
                    if 'water' in comps:

                        if 'methanol' in comps:
                            #print(f'{comps} methanol + water')
                            __createDFRow__(dataReport, data, doi, title, authors, pom, meas, moleFractions, "water", 0, "methanol", 5)
                            
                        elif 'choline chloride' in comps:
                            if 'urea' in comps:
                                #print(f'{comps} urea + water + ChCl')
                                __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "water", 0, "choline chloride", 2, "urea", 3)
                            elif 'glycerol' in comps:
                                #print(f'{comps} glycerol + water + ChCl')
                                __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "water", 0, "choline chloride", 2, "glycerol", 1)
                            else:
                                __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "water", 0, "choline chloride", 2)
                                #print(f'{comps} water + choline chloride')
                        elif 'ethylene glycol' in comps:
                            if 'N,N-Diethylethanolammonium chloride' in comps:
                                __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "water", 0, "ethylene glycol", 4, "N,N-Diethylethanolammonium chloride", 6)
                                #print(f'{comps} ethylene glycol + wasser + N,N-Diethylethanolammonium chloride')
                            else:
                                __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "water", 0, "ethylene glycol", 4)
                                #print(f'{comps} ethylene glycol + wasser')
                        elif 'glycerol' in comps:
                            if 'N,N-Diethylethanolammonium chloride' in comps:
                                __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "water", 0, "glycerol", 1, "N,N-Diethylethanolammonium chloride", 6)
                                #print(f'{comps} water + glycerol + N,N-Diethylethanolammonium chloride')
                        elif 'urea' in comps:
                            __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "water", 0, "urea", 3)
                            #print(f'{comps} water + urea')
                        else:
                            __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "water", 0)
                            #print(f'{comps} water')                    
                        

    df = pd.DataFrame(data, columns=['DOI', 'title', 'authors',  
    'mole fraction water', 'mole fraction glycerol', 'mole fraction choline chloride', 'mole fraction urea', 'mole fraction ethylene glycol', 'mole fraction methanol', "mole fractionN,N-Diethylethanolammonium chloride", 'temperature', 'viscosity', 'delta viscosity',
    '1/RT (mol/kj)', 'ln(eta) (cP)', 'delta ln(eta) (cP)'])

    return df, DOIs

def __getMoleFraction__(dataReport, pureOrMixtureData, moleculeName, meas):
    """returns moleFraction of moleculeName in meas"""
    for ID, compound in dataReport.getCompDict().items():
        if compound.commonName == moleculeName:
            # used because in variable declaration ID of component composition of respective molecule is not compound ID (shift +1) because temperature
            moleFracKey = pureOrMixtureData.getMoleFractionIDs()[ID]

    return meas.getVariable(moleFracKey)[0].value

def __getTemperature__(pureOrMixtureData, meas):
    """returns Temperature of meas"""
    for key, variable in pureOrMixtureData.getPOMVariableList().items():
        if variable.varName == "Temperature":
            tempKey = key
    
    return meas.getVariable(tempKey)[0].value

def __getViscosity__(pureOrMixtureData, meas):
    """returns viscosity of meas"""
    for key, property in pureOrMixtureData.getPOMPropertyList().items():
        if property.propName == "Viscosity":
            propKey = key

    return meas.getProperty(propKey)[0].value, meas.getProperty(propKey)[0].uncertainty

def __createDFRow__(dataReport, data, doi, title, authors, pom, meas, moleFractions, molec1, molec1ID, molec2=None,  molec2ID=None, molec3=None,  molec3ID=None):
    if molec3 is None:
        if molec2 is None:
            mf1 = __getMoleFraction__(dataReport, pom, molec1, meas)
            temp = __getTemperature__(pom, meas)
            tempRT = __tranformTemperature__(temp)
            visc, deltaVisc = __getViscosity__(pom, meas)
            viscln = __transformViscosity__(visc)
            deltaViscln = __transformViscosity__(viscln)
            moleFractions[molec1ID] = str(mf1)
            data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, tempRT, viscln, deltaViscln))
        else:
            mf1 = __getMoleFraction__(dataReport, pom, molec1, meas)
            mf2 = __getMoleFraction__(dataReport, pom, molec2, meas)
            temp = __getTemperature__(pom, meas)
            tempRT = __tranformTemperature__(temp)
            visc, deltaVisc = __getViscosity__(pom, meas)
            viscln = __transformViscosity__(visc)
            deltaViscln = __transformViscosity__(viscln)
            moleFractions[molec1ID] = str(mf1)
            moleFractions[molec2ID] = str(mf2)
            data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, tempRT, viscln, deltaViscln))
    else:
        mf1 = __getMoleFraction__(dataReport, pom, molec1, meas)
        mf2 = __getMoleFraction__(dataReport, pom, molec2, meas)
        mf3 = __getMoleFraction__(dataReport, pom, molec3, meas)
        temp = __getTemperature__(pom, meas)
        tempRT = __tranformTemperature__(temp)
        visc, deltaVisc = __getViscosity__(pom, meas)
        viscln = __transformViscosity__(visc)
        deltaViscln = __transformViscosity__(viscln)
        moleFractions[molec1ID] = str(mf1)
        moleFractions[molec2ID] = str(mf2)
        moleFractions[molec3ID] = str(mf3)

        data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, tempRT, viscln, deltaViscln))

if __name__ == "__main__":
    df, dois = createDataFrame()
    print(df)

    for doi in dois:
        dataDOI = df[df.DOI == doi]
        fig = px.scatter(dataDOI, x='1/RT (mol/kj)', y='ln(eta) (cP)', trendline="ols", color="mole fraction water", title=f"ln(eta) over 1/RT {doi}")
        fig.update(layout=dict(title=dict(x=0.5)))
        fitResults= px.get_trendline_results(fig).px_fit_results.iloc[0]
        fig.show()
        