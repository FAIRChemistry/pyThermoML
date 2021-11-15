import pandas as pd
from pandas.core.frame import DataFrame
import os
import numpy as np
from pythermo.thermoml.core import datareport
from pythermo.thermoml.tools.readTools import readThermo
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def createDataFrame(dataReport) -> DataFrame:
    """creates pandas data Frame of current datareport object
    
    This method is used to simplificate analyzation.
    WARNING
        Only use method if your variables are temperature or max. 3 mole fractions.
        Datafrane only describes viscosity and mass density as property

    """
    
    # citation stuff
    try:
        doi = dataReport.DOI
    except AttributeError:
        doi = None
    try:
        title = dataReport.title
    except AttributeError:
        title = None
    try:
        authors = dataReport.authors
        authors = [author for author in authors.values()]
    except AttributeError:
        authors = None

    # extract more information
    # TODO: more than one pure or mixture data
    pom = dataReport.getPureOrMixtureData(dataReport.getPureOrMixtureDataIDs()[0])
    
    comps = list()

    # datalist used to describe one row of dataframe
    data = list()

    for comp in dataReport.getCompDict().values():
        comps.append(comp.smiles)
        
    measDict = pom.getMeasurementsList()

    for meas in measDict:
        moleFractions = []
        for i in range(7):
            moleFractions.append("NaN")
        if 'O' in comps:
            
            if 'CO' in comps:
                #print(f'{comps} methanol + water')
                __createDFRow__(dataReport, data, doi, title, authors, pom, meas, moleFractions, "O", 0, "CO", 5)
                
            elif 'C[N+](C)(C)CCO.[Cl-]' in comps:
                if 'C(=O)(N)N' in comps:
                    #print(f'{comps} urea + water + ChCl')
                    __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "O", 0, "C[N+](C)(C)CCO.[Cl-]", 2, "C(=O)(N)N", 3)
                elif 'C(C(CO)O)O' in comps:
                    #print(f'{comps} glycerol + water + ChCl')
                    
                    __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "O", 0, "C[N+](C)(C)CCO.[Cl-]", 2, "C(C(CO)O)O", 1)
                else:
                    __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "O", 0, "C[N+](C)(C)CCO.[Cl-]", 2)
                    #print(f'{comps} water + choline chloride')
            elif 'C(CO)O' in comps:
                if 'CC(C)(C)NCCO.Cl' in comps:
                    __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "O", 0, "ethylene glycol", 4, "CC(C)(C)NCCO.Cl", 6)
                    #print(f'{comps} ethylene glycol + wasser + N,N-Diethylethanolammonium chloride')
                else:
                    __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "O", 0, "ethylene glycol", 4)
                    #print(f'{comps} ethylene glycol + wasser')
            elif 'C(C(CO)O)O' in comps:
                
                if 'CC(C)(C)NCCO.Cl' in comps:
                    __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "O", 0, "C(C(CO)O)O", 1, "CC(C)(C)NCCO.Cl", 6)
                    #print(f'{comps} water + glycerol + N,N-Diethylethanolammonium chloride')
                else:
                    __createDFRow__(dataReport, data, doi, title, authors, pom, meas, moleFractions, "O", 0, "C(C(CO)O)O", 1)
            elif 'C(=O)(N)N' in comps:
                __createDFRow__(dataReport, data, doi , title, authors, pom, meas, moleFractions, "O", 0, "C(=O)(N)N", 3)
                #print(f'{comps} water + urea')
            else:
                __createDFRow__(dataReport, data, doi, title, authors, pom, meas, moleFractions, "O", 0)
                #print(f'{comps} water')                    
    

    df = pd.DataFrame(data, columns=['DOI', 'title', 'authors',  
    'water', 'glycerol', 'choline chloride', 'urea', 'ethylene glycol', 'methanol', "N,N-Diethylethanolammonium chloride", 
    'temperature', 'viscosity', 'delta viscosity', 'mass density', 'delta mass density', 
    '1/RT (mol/kj)', 'ln(eta) (cP)'])

    return df

### private methods used for data frame creation
def __getMoleFraction__(dataReport, pureOrMixtureData, moleculeName, meas):
    """returns moleFraction of moleculeName in meas"""
    for ID, compound in dataReport.getCompDict().items():
        if compound.smiles == moleculeName:
            # used because in variable declaration ID of component composition of respective molecule is not compound ID (shift +1) because temperature
            moleFracKey = pureOrMixtureData.getMoleFractionIDs()[ID]
    return meas.getVariable(moleFracKey)[0].value

def __getTemperature__(pureOrMixtureData, meas):
    """returns Temperature of meas"""
    for key, variable in pureOrMixtureData.getPOMVariableList().items():
        if variable.varName == "Temperature":
            tempKey = key
            return meas.getVariable(tempKey)[0].value
        else:
            return "NaN"

def __getViscosity__(pureOrMixtureData, meas):
    """returns viscosity of meas"""
    for key, property in pureOrMixtureData.getPOMPropertyList().items():
        if property.propName == "Viscosity":
            propKey = key
            try:
                return meas.getProperty(propKey)[0].value, meas.getProperty(propKey)[0].uncertainty
            except AttributeError:
                try:
                    return meas.getProperty(propKey)[0].value, "NaN"
                except AttributeError:
                    return "NaN", "NaN"
        else:
            return "NaN", "NaN"

def __getDensity__(pureOrMixtureData, meas):
    """returns density of meas"""
    for key, property in pureOrMixtureData.getPOMPropertyList().items():
        if property.propName == "Mass density":
            propKey = key
            try:
                return meas.getProperty(propKey)[0].value, meas.getProperty(propKey)[0].uncertainty
            except AttributeError:
                try:
                    return meas.getProperty(propKey)[0].value, "NaN"
                except AttributeError:
                    return "NaN", "NaN"
        else:
            return "NaN", "NaN"
    
def __createDFRow__(dataReport, data, doi, title, authors, pom, meas, moleFractions, molec1, molec1ID, molec2=None,  molec2ID=None, molec3=None,  molec3ID=None):
    
    if molec3 is None:
        if molec2 is None:
            mf1 = __getMoleFraction__(dataReport, pom, molec1, meas)
            temp = __getTemperature__(pom, meas)
            tempRT = __tranformTemperature__(temp)
            visc, deltaVisc = __getViscosity__(pom, meas)
            dens, deltaDens = __getDensity__(pom, meas)
            if visc != "NaN":
                viscln = __transformViscosity__(visc)
            else:
                viscln = "NaN"
            moleFractions[molec1ID] = str(mf1)
            data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, dens, deltaDens, tempRT, viscln))
        else:
            mf1 = __getMoleFraction__(dataReport, pom, molec1, meas)
            mf2 = __getMoleFraction__(dataReport, pom, molec2, meas)
            temp = __getTemperature__(pom, meas)
            tempRT = __tranformTemperature__(temp)
            visc, deltaVisc = __getViscosity__(pom, meas)
            dens, deltaDens = __getDensity__(pom, meas)
            if visc != "NaN":
                viscln = __transformViscosity__(visc)
            else:
                viscln = "NaN"
            moleFractions[molec1ID] = str(mf1)
            moleFractions[molec2ID] = str(mf2)
            data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, dens, deltaDens, tempRT, viscln))
    else:
        mf1 = __getMoleFraction__(dataReport, pom, molec1, meas)
        mf2 = __getMoleFraction__(dataReport, pom, molec2, meas)
        mf3 = __getMoleFraction__(dataReport, pom, molec3, meas)
        temp = __getTemperature__(pom, meas)
        tempRT = __tranformTemperature__(temp)
        visc, deltaVisc = __getViscosity__(pom, meas)
        dens, deltaDens = __getDensity__(pom, meas)
        if visc != "NaN":
            viscln = __transformViscosity__(visc)
        else:
            viscln = "NaN"
        moleFractions[molec1ID] = str(mf1)
        moleFractions[molec2ID] = str(mf2)
        moleFractions[molec3ID] = str(mf3)

        data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, dens, deltaDens, tempRT, viscln))


def __transformViscosity__(eta):
    return np.log(eta*1000)


def __tranformTemperature__(temperature):
    R = 8.31446261815324/1000
    return 1 / (R*temperature)