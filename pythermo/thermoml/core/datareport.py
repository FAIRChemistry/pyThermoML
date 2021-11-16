
from typing import Optional
from pandas.core.frame import DataFrame
from pythermo.thermoml.core.exceptions import ThermoMLTypeError
from pythermo.thermoml.core.functionalities import TypeChecker
from pythermo.thermoml.core import PureOrMixtureData
from pythermo.thermoml.core import Compound

import numpy as np
import pandas as pd
import json


class DataReport():
    
    title: Optional[str]
    DOI: Optional[str]
    authors: Optional[dict[str, str]] = {}
    compounds: dict[str, Compound] = {}
    pureOrMixtureData: dict[str, PureOrMixtureData] = {}
    
    def __init__(
        self,
        title=None,
        DOI=None,
        authors=None,
    ) -> None:
        '''
        Object describing a DataReport.

        Args:
            String title: Title of referred paper
            String DOI: DOI of referred
            List authors: Authors of referred paper
        '''
        
        
        if title is not None:
            self.title = TypeChecker(title, str)
        if DOI is not None:
            self.DOI = TypeChecker(DOI, str)

        self.authors = dict()
        self.compounds = dict()
        self.pureOrMixtureData = dict()

        if authors is not None:
            try:
                for key, value in authors.items():
                    self.authors[key] = value
            except AttributeError:
                raise AttributeError(
                    f"authors should be stored in a dict"
                )
    
    def __str__(self) -> str:
        return self.toJSON()

    def toJSON(self, d=False) -> str:
        '''retunrs json formatted string representation of DataReport class'''
        
        def transformAttributes(self):
            
            jsonDict = dict()
            for key, value in self.__dict__.items():
                
                if isinstance(value, dict):
                    jsonDict[key.replace('_', '')] = dict()

                    for ID, item in value.items():
                        try:
                            jsonDict[key.replace(
                                '_', '')][ID] = item.toJSON(d=True)
                        except AttributeError:
                            jsonDict[key.replace('_', '')][ID] = item

                else:
                    jsonDict[key.replace('_', '')] = value

            return jsonDict

        if d:
            return transformAttributes(self)

        else:
            return json.dumps(
                self,
                default=transformAttributes,
                indent=4
            )

    
    def addCompound(self, comp: Compound) -> str():
        """adds compund to DataReport returns ID"""
        if comp.dataType != "comp":
            raise ThermoMLTypeError (
                given_type=comp.dataType, expected_type="Compound"
            )
            # Add compound to dictionary in DataReport
        self.compounds[comp.ID] = comp

        return comp.ID

    def addPureOrMixtureData(self, pureOrMixtureData):
        self.pureOrMixtureData[pureOrMixtureData.ID] = pureOrMixtureData

        return pureOrMixtureData.ID

    def addAuthor(self, name, ID):
        self.authors[ID] = name

        return ID

    def getAuthor(self, ID):
        try:
            return self._authors[ID]
        except KeyError:
            raise KeyError(
                f"Author with ID {ID} does not exist"
            )
    
    def getAuthorList(self):
        return [
            authorInstance for authorInstance in self._authors.values()
        ]

    def getCompound(self, ID):
        try:
            return self._compounds[ID]
        except KeyError:
            raise KeyError(
                f"Compound with ID {ID} does not exist."
            )
        
    def getCompoundList(self):
        return [
            compoundInstance for compoundInstance in self._compounds.values()
        ]
    
    def getCompDict(self) -> dict:
        """returns dictionary with ID (key) of compound (value) used in dataReport"""
        compoundDict = dict()
        for value in self._compounds.values():
            compoundDict[value.ID] = value
        return compoundDict

    def getPureOrMixtureData(self, ID=None) -> PureOrMixtureData:
        if ID is not None:
            try:
                return self._pureOrMixtureData[ID]
            except KeyError:
                
                raise KeyError(
                    f"PureOrMixtureData with ID {ID} does not exist."
                )
        
        #DANGEROUS!
        else:
            try:
                print("used pure or mixture data key = ID")
                return self._pureOrMixtureData["ID"]
                
            except KeyError:
                raise KeyError(f"Please enter key of pure or mixture Data")

    def getPureOrMixtureDataList(self):
        return [
            pureOrMixtureDataInstance
            for pureOrMixtureDataInstance in self._pureOrMixtureData.values()

    ]

    def getPureOrMixtureDataIDs(self) -> list:
        """returns list with keys used in DataReport"""
        keys = list()
        for key in self._pureOrMixtureData.keys():
            keys.append(key)
        return keys
    

    @property
    def compounds(self):
        return self._compounds
    
    @compounds.setter
    def compounds(self, compounds):
        self._compounds = TypeChecker(compounds, dict)

    @property
    def authors(self):
        return self._authors
    
    @authors.setter
    def authors(self, authors):
        self._authors = TypeChecker(authors, dict)

    @property
    def pureOrMixtureData(self):
        return self._pureOrMixtureData

    @pureOrMixtureData.setter
    def pureOrMixtureData(self, pureOrMixtureData):
        self._pureOrMixtureData = TypeChecker(
            pureOrMixtureData, dict
        )

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = TypeChecker(title, str)

    @property
    def DOI(self):
        return self._DOI

    @DOI.setter
    def DOI(self, DOI):
        self._DOI = TypeChecker(DOI, str)


    def createDataFrame(self) -> DataFrame:
        """creates pandas data Frame of current datareport object"""

        # citation stuff
        doi = self.DOI
        title = self.title
        authors = self.authors
        authors = self.authors
        authors = [author for author in authors.values()]

        # extract more information
        # TODO: more than one pure or mixture data
        pom = self.getPureOrMixtureData(self.getPureOrMixtureDataIDs()[0])
        
        comps = list()

        # datalist used to describe one row of dataframe
        data = list()

        for comp in self.getCompDict().values():
            comps.append(comp.commonName)
            
        measDict = pom.getMeasurementsList()
        for meas in measDict:
            moleFractions = []
            for i in range(7):
                moleFractions.append("NaN")
            if 'water' in comps:

                if 'methanol' in comps:
                    #print(f'{comps} methanol + water')
                    self.__createDFRow__(data, doi, title, authors, pom, meas, moleFractions, "water", 0, "methanol", 5)
                    
                elif 'choline chloride' in comps:
                    if 'urea' in comps:
                        #print(f'{comps} urea + water + ChCl')
                        self.__createDFRow__(data, doi , title, authors, pom, meas, moleFractions, "water", 0, "choline chloride", 2, "urea", 3)
                    elif 'glycerol' in comps:
                        #print(f'{comps} glycerol + water + ChCl')
                        self.__createDFRow__(data, doi , title, authors, pom, meas, moleFractions, "water", 0, "choline chloride", 2, "glycerol", 1)
                    else:
                        self.__createDFRow__(data, doi , title, authors, pom, meas, moleFractions, "water", 0, "choline chloride", 2)
                        #print(f'{comps} water + choline chloride')
                elif 'ethylene glycol' in comps:
                    if 'N,N-Diethylethanolammonium chloride' in comps:
                        self.__createDFRow__(data, doi , title, authors, pom, meas, moleFractions, "water", 0, "ethylene glycol", 4, "N,N-Diethylethanolammonium chloride", 6)
                        #print(f'{comps} ethylene glycol + wasser + N,N-Diethylethanolammonium chloride')
                    else:
                        self.__createDFRow__(data, doi , title, authors, pom, meas, moleFractions, "water", 0, "ethylene glycol", 4)
                        #print(f'{comps} ethylene glycol + wasser')
                elif 'glycerol' in comps:
                    if 'N,N-Diethylethanolammonium chloride' in comps:
                        self.__createDFRow__(data, doi , title, authors, pom, meas, moleFractions, "water", 0, "glycerol", 1, "N,N-Diethylethanolammonium chloride", 6)
                        #print(f'{comps} water + glycerol + N,N-Diethylethanolammonium chloride')
                elif 'urea' in comps:
                    self.__createDFRow__(data, doi , title, authors, pom, meas, moleFractions, "water", 0, "urea", 3)
                    #print(f'{comps} water + urea')
                else:
                    self.__createDFRow__(data, doi , title, authors, pom, meas, moleFractions, "water", 0)
                    #print(f'{comps} water')                    
                

        df = pd.DataFrame(data, columns=['DOI', 'title', 'authors',  
        'water', 'glycerol', 'choline chloride', 'urea', 'ethylene glycol', 'methanol', "N,N-Diethylethanolammonium chloride", 'temperature', 'viscosity', 'delta viscosity',
        '1/RT (mol/kj)', 'ln(eta) (cP)'])

        return df

    ### private methods used for data frame creation
    def __getMoleFraction__(self, pureOrMixtureData, moleculeName, meas):
        """returns moleFraction of moleculeName in meas"""
        for ID, compound in self.getCompDict().items():
            if compound.commonName == moleculeName:
                # used because in variable declaration ID of component composition of respective molecule is not compound ID (shift +1) because temperature
                moleFracKey = pureOrMixtureData.getMoleFractionIDs()[ID]
        return meas.getVariable(moleFracKey)[0].value

    def __getTemperature__(self, pureOrMixtureData, meas):
        """returns Temperature of meas"""
        for key, variable in pureOrMixtureData.getPOMVariableList().items():
            if variable.varName == "Temperature":
                tempKey = key
        
        return meas.getVariable(tempKey)[0].value

    def __getViscosity__(self, pureOrMixtureData, meas):
        """returns viscosity of meas"""
        for key, property in pureOrMixtureData.getPOMPropertyList().items():
            if property.propName == "Viscosity":
                propKey = key
        
        try:
            return meas.getProperty(propKey)[0].value, meas.getProperty(propKey)[0].uncertainty
        except AttributeError:
            return meas.getProperty(propKey)[0].value, "NG"

    def __createDFRow__(self, data, doi, title, authors, pom, meas, moleFractions, molec1, molec1ID, molec2=None,  molec2ID=None, molec3=None,  molec3ID=None):
        if molec3 is None:
            if molec2 is None:
                mf1 = self.__getMoleFraction__(pom, molec1, meas)
                temp = self.__getTemperature__(pom, meas)
                tempRT = self.__tranformTemperature__(temp)
                visc, deltaVisc = self.__getViscosity__(pom, meas)
                viscln = self.__transformViscosity__(visc)
                moleFractions[molec1ID] = str(mf1)
                data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, tempRT, viscln,))
            else:
                mf1 = self.__getMoleFraction__(pom, molec1, meas)
                mf2 = self.__getMoleFraction__(pom, molec2, meas)
                temp = self.__getTemperature__(pom, meas)
                tempRT = self.__tranformTemperature__(temp)
                visc, deltaVisc = self.__getViscosity__(pom, meas)
                viscln = self.__transformViscosity__(visc)
                moleFractions[molec1ID] = str(mf1)
                moleFractions[molec2ID] = str(mf2)
                data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, tempRT, viscln))
        else:
            mf1 = self.__getMoleFraction__(pom, molec1, meas)
            mf2 = self.__getMoleFraction__(pom, molec2, meas)
            mf3 = self.__getMoleFraction__(pom, molec3, meas)
            temp = self.__getTemperature__(pom, meas)
            tempRT = self.__tranformTemperature__(temp)
            visc, deltaVisc = self.__getViscosity__(pom, meas)
            viscln = self.__transformViscosity__(visc)
            moleFractions[molec1ID] = str(mf1)
            moleFractions[molec2ID] = str(mf2)
            moleFractions[molec3ID] = str(mf3)

            data.append((doi, title, authors, *moleFractions, temp, visc, deltaVisc, tempRT, viscln))
    
    def __transformViscosity__(self, eta):
        return np.log(eta*1000)


    def __tranformTemperature__(self, temperature):
        R = 8.31446261815324/1000
        return 1 / (R*temperature)
