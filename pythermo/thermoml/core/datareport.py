import pandas as pd
import numpy as np

from typing import Optional
from pydantic import BaseModel

from pythermo.thermoml.core.exceptions import ThermoMLTypeError
from pythermo.thermoml.core.pureOrMixtureData import PureOrMixtureData
from pythermo.thermoml.core.compound import Compound


class DataReport(BaseModel):

    title: Optional[str]
    DOI: Optional[str]
    authors: dict[str, str] = {}
    compounds: dict[str, Compound] = {}
    pureOrMixtureData: dict[str, PureOrMixtureData] = {}

    def addCompound(self, comp: Compound) -> str:
        """adds compund to DataReport returns ID"""
        if comp._type != "comp":
            raise ThermoMLTypeError(
                given_type=comp._type, expected_type="Compound"
            )
            # Add compound to dictionary in DataReport
        self.compounds[comp.ID] = comp

        return comp.ID

    def addPureOrMixtureData(self, pureOrMixtureData):
        self.pureOrMixtureData[pureOrMixtureData.ID] = pureOrMixtureData

        return pureOrMixtureData.ID

    def addAuthor(self, name: str, ID: str):
        self.authors[ID] = name

    def getAuthor(self, ID):
        try:
            return self.authors[ID]
        except KeyError:
            raise KeyError(
                f"Author with ID {ID} does not exist"
            )

    def getCompound(self, ID):
        try:
            return self.compounds[ID]
        except KeyError:
            raise KeyError(
                f"Compound with ID {ID} does not exist."
            )

    def getPureOrMixtureData(self, ID: str) -> PureOrMixtureData:
        if ID is not None:
            try:
                return self.pureOrMixtureData[ID]
            except KeyError:

                raise KeyError(
                    f"PureOrMixtureData with ID {ID} does not exist."
                )

        # DANGEROUS!
        else:
            try:
                print("used pure or mixture data key = ID")
                return self.pureOrMixtureData["ID"]

            except KeyError:
                raise KeyError("Please enter key of pure or mixture Data")

    def getAuthorList(self):
        return self._getElementList(self.authors)

    def getCompoundList(self):
        return self._getElementList(self.compounds)

    def getPureOrMixtureDataList(self):
        return self._getElementList(self.pureOrMixtureData)

    def _getElementList(self, dictionary: dict) -> list[str]:
        return list(dictionary.keys())

    def getPureOrMixtureDataIDs(self) -> list:
        """returns list with keys used in DataReport"""
        return list(self.pureOrMixtureData.keys())

    def createDataFrame(self) -> pd.DataFrame:
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

        for comp in self.compounds.values():
            comps.append(comp.commonName)

        measDict = pom.getMeasurementsList()
        for meas in measDict:
            moleFractions = []
            for i in range(7):
                moleFractions.append("NaN")
            if 'water' in comps:

                if 'methanol' in comps:
                    self.__createDFRow__(
                        data, doi, title, authors, pom, meas, moleFractions, "water", 0, "methanol", 5)

                elif 'choline chloride' in comps:
                    if 'urea' in comps:
                        #print(f'{comps} urea + water + ChCl')
                        self.__createDFRow__(data, doi, title, authors, pom, meas,
                                             moleFractions, "water", 0, "choline chloride", 2, "urea", 3)
                    elif 'glycerol' in comps:
                        #print(f'{comps} glycerol + water + ChCl')
                        self.__createDFRow__(data, doi, title, authors, pom, meas,
                                             moleFractions, "water", 0, "choline chloride", 2, "glycerol", 1)
                    else:
                        self.__createDFRow__(
                            data, doi, title, authors, pom, meas, moleFractions, "water", 0, "choline chloride", 2)
                        #print(f'{comps} water + choline chloride')
                elif 'ethylene glycol' in comps:
                    if 'N,N-Diethylethanolammonium chloride' in comps:
                        self.__createDFRow__(data, doi, title, authors, pom, meas, moleFractions,
                                             "water", 0, "ethylene glycol", 4, "N,N-Diethylethanolammonium chloride", 6)
                        #print(f'{comps} ethylene glycol + wasser + N,N-Diethylethanolammonium chloride')
                    else:
                        self.__createDFRow__(
                            data, doi, title, authors, pom, meas, moleFractions, "water", 0, "ethylene glycol", 4)
                        #print(f'{comps} ethylene glycol + wasser')
                elif 'glycerol' in comps:
                    if 'N,N-Diethylethanolammonium chloride' in comps:
                        self.__createDFRow__(data, doi, title, authors, pom, meas, moleFractions,
                                             "water", 0, "glycerol", 1, "N,N-Diethylethanolammonium chloride", 6)
                        #print(f'{comps} water + glycerol + N,N-Diethylethanolammonium chloride')
                elif 'urea' in comps:
                    self.__createDFRow__(
                        data, doi, title, authors, pom, meas, moleFractions, "water", 0, "urea", 3)
                    #print(f'{comps} water + urea')
                else:
                    self.__createDFRow__(
                        data, doi, title, authors, pom, meas, moleFractions, "water", 0)
                    #print(f'{comps} water')

        df = pd.DataFrame(data, columns=['DOI', 'title', 'authors',
                                         'water', 'glycerol', 'choline chloride', 'urea', 'ethylene glycol', 'methanol', "N,N-Diethylethanolammonium chloride", 'temperature', 'viscosity', 'delta viscosity',
                                         '1/RT (mol/kj)', 'ln(eta) (cP)'])

        return df

    # private methods used for data frame creation
    def __getMoleFraction__(self, pureOrMixtureData, moleculeName, meas):
        """returns moleFraction of moleculeName in meas"""
        for ID, compound in self.compounds.items():
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

    def __createDFRow__(
            self, data, doi, title, authors, pom, meas, moleFractions, molec1, molec1ID, molec2=None, molec2ID=None, molec3=None, molec3ID=None):
        if molec3 is None:
            if molec2 is None:
                mf1 = self.__getMoleFraction__(pom, molec1, meas)
                temp = self.__getTemperature__(pom, meas)
                tempRT = self.__tranformTemperature__(temp)
                visc, deltaVisc = self.__getViscosity__(pom, meas)
                viscln = self.__transformViscosity__(visc)
                moleFractions[molec1ID] = str(mf1)
                data.append((doi, title, authors, *moleFractions,
                            temp, visc, deltaVisc, tempRT, viscln,))
            else:
                mf1 = self.__getMoleFraction__(pom, molec1, meas)
                mf2 = self.__getMoleFraction__(pom, molec2, meas)
                temp = self.__getTemperature__(pom, meas)
                tempRT = self.__tranformTemperature__(temp)
                visc, deltaVisc = self.__getViscosity__(pom, meas)
                viscln = self.__transformViscosity__(visc)
                moleFractions[molec1ID] = str(mf1)
                moleFractions[molec2ID] = str(mf2)
                data.append((doi, title, authors, *moleFractions,
                            temp, visc, deltaVisc, tempRT, viscln))
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

            data.append((doi, title, authors, *moleFractions,
                        temp, visc, deltaVisc, tempRT, viscln))

    def __transformViscosity__(self, eta):
        return np.log(eta * 1000)

    def __tranformTemperature__(self, temperature):
        R = 8.31446261815324 / 1000
        return 1 / (R * temperature)
