# @File          :   readTools.py
# @Last modified :   2022/04/09 19:28:49
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from pythermo.thermoml.props.bioproperties import Bioproperty
from pythermo.thermoml.props.volumetricproperties import VolumetricProperty
from pythermo.thermoml.props.refractionSurfaceTensionSoundSpeedproperties import RefractionSurfaceTensionSoundSpeedproperty
from pythermo.thermoml.props.heatcapacityproperties import HeatCapacityProperty
from pythermo.thermoml.props.transportproperties import TransportProperty

from pythermo.thermoml.vars.temperature import TemperatureBase
from pythermo.thermoml.vars.pressure import PressureBase
from pythermo.thermoml.vars.componentcomposition import ComponentCompositionBase

from pythermo.thermoml.core import Compound, DataPoint, DataReport, PureOrMixtureData, ThermoMLQuantityNotFoundError
from lxml import etree
from pydantic import BaseModel
from typing import Dict
from pathlib import Path
import warnings

class ThermoMLReader(BaseModel):
    """
    Class providing reader functionalities to read a ThermoML file.

    Args:
        folder_thermoML_files(str): path to folder that contains thermoML files
    """

    folder_thermoML_files: str
    
    # NAMESPACE (str): Namespace of ThermoML 
    __NAMESPACE__: str = './/{http://www.iupac.org/namespaces/ThermoML}'

    # propMapping (dict): Dict with property names and units (str) as keys and initalizer function as values.     
    __propMapping__: Dict = {
        'Viscosity, Pa*s': TransportProperty.viscosity,
        'Kinematic Viscosity, m2/s': TransportProperty.kinematicViscosity,
        'Self diffusion coefficient, m2/s': TransportProperty.selfDiffusionCoefficient,
        'Mass density, kg/m3': VolumetricProperty.massDensity,
        'Surface tension liquid-gas, N/m': RefractionSurfaceTensionSoundSpeedproperty.surfaceTension,
        'Speed of sound, m/s': RefractionSurfaceTensionSoundSpeedproperty.speedOfSound,
        'Molar heat capacity at constant pressure, J/K/mol': HeatCapacityProperty.molarHCconstPressure,
        'Molar heat capacity at constant volume, J/K/mol': HeatCapacityProperty.molarHCconstVolume,
        'Peak temperature, K': Bioproperty.peakTemperature,
    }

    # varMapping (dict): Dict with variable names and units (str) as keys and initalizer function as values.
    __varMapping__: Dict = {
        'Temperature, K': TemperatureBase.temperature,
        'Lower temperature, K': TemperatureBase.lowerTemperature,
        'Upper temperature, K': TemperatureBase.upperTemperature,
        'Mole fraction': ComponentCompositionBase.moleFraction,
        'Pressure, kPa': PressureBase.pressure
    }


    def readFromJSON(self, filename:str) -> DataReport:
        """Reads given .json formatted file to DataReport object.
        Args:
            filename (str): name of the json file that 
        Returns:
            DataReport: Based on given .json file DataReport object
        """
        return DataReport.parse_file(Path(f"{self.folder_thermoML_files}{filename}"))

    def readFromThermoMLFile(self, filename:str, NIST:bool=False) -> DataReport:
        """Reads given ThermoML file to DataReport object.
        Args:
            filename (str): name of the thermoML file that should be read in.
        Returns:
            DataReport: Based on given ThermoML file
        """

        path = etree.parse(f"{self.folder_thermoML_files}{filename}").getroot()
        title = self.__getOneEntry__(path, tag="sTitle")
        doi = self.__getOneEntry__(path, tag="sDOI")
        authors = self.__getAuthors__(path)

        datareport = DataReport(title=title, DOI=doi, authors=authors)

        comps = self.__getCompounds__(path)

        if comps is not None:
            for comp in comps.values():
                datareport.addCompound(comp)

            pOMData = self.__getPOMData__(path, comps)

            # experiment[0] Object
            # experiment[1] ElementTree
            for experiment in pOMData.values():
                props = self.__getProperties__(experiment[1])
                vars = self.__getVariables__(experiment[1])
                
                for id, value in props.items():
                    if NIST:
                        method = "experiment"
                    else:
                        method = value[1]
                    experiment[0].addProperty(
                        value[0](ID=id, method=method, compoundID=value[2]))

                for id, value in vars.items():
                    experiment[0].addVariable(value[0](ID=id, compoundID=value[1]))

                datareport.addPureOrMixtureData(
                    self.__getMeasurements__(experiment[0], experiment[1]))

        return datareport

    def __getOneEntry__(self, root: etree._Element, tag:str) -> str:
        """returns value of specified tag in ThermoML file

        Args:
            tag (str): name of the tag
            root (etree._Element): root of element

        Returns:
            str: value of specified tag in ThermoML file
            None: if tag cannot be found in file
        """
        if root.findall(self.__NAMESPACE__ + tag):
            return root.findall(self.__NAMESPACE__ + tag)[0].text
        else:
            return None

    def __getAuthors__(self, path) -> dict[str, str]:
        """returns authors dictionary from sAuthors tag in ThermoML file

        Args:
            root (etree._Element): etree._Element representation of ThermoML file

        Returns:
            dict[str, str]: dict of authors
        """
        if path.findall(self.__NAMESPACE__ + 'sAuthor'):
            authorList = path.findall(self.__NAMESPACE__ + 'sAuthor')
            authors = dict()

            for index, author in enumerate(authorList):
                authors[str(index)] = author.text

            return authors

    def __getCompounds__(self, path) -> dict[str, Compound]:
        """returns dictionary of compounds used in ThermoML file.
        Args:

        Raises:
            ThermoMLNoCompoundError: ThermoML file does not contain compounds

        Returns:
            dict[str, Compound]: compounds used in ThermoML file. Key is compID
        """
        comps = dict()
        if path.findall(self.__NAMESPACE__ + 'Compound'):

            for compound in path.findall(self.__NAMESPACE__ + 'Compound'):
                ID = self.__getOneEntry__(compound, 'nOrgNum')
                comps[ID] = Compound(
                    ID=ID,
                    standardInchI=self.__getOneEntry__(
                        compound, 'sStandardInChI'),
                    standardInchIKey=self.__getOneEntry__(
                        compound, 'sStandardInChIKey'),
                    smiles=self.__getOneEntry__(compound, 'sSmiles'),
                    commonName=self.__getOneEntry__(compound, 'sCommonName')
                )

            return comps

    def __getPOMData__(self, path, comps: dict[str, Compound]) -> dict[str, list[PureOrMixtureData, etree.Element]]:
        """returns dict of pureOrMixtureData in dataReport

        Args:
            comps (dict): compound dictionary

        Returns:
            dict: dict with keys: nPureOrMixtureDataNumber and values: [PureOrMixtureData, pureOrMixtureData]
            First argument is Object of PureOrMixtureData, second argument returns ET Element. 
            -> only get following properties/variables of pureOrMixtureData, not whole path
        """

        pOMData = dict()
        comps = list(comps.keys())
        if path.findall(self.__NAMESPACE__ + 'PureOrMixtureData'):

            for pureOrMixtureData in path.findall(self.__NAMESPACE__ + 'PureOrMixtureData'):
                compiler = self.__getOneEntry__(pureOrMixtureData, 'sCompiler')
                pomID = self.__getOneEntry__(pureOrMixtureData, 'nPureOrMixtureDataNumber')
                # All declared compounds should be used in pure or mixture Data
                pOMData[pomID] = (PureOrMixtureData(
                    ID=pomID,
                    comps=comps,
                    compiler=compiler), pureOrMixtureData)
        return pOMData

    def __getProperties__(self, pureOrMixtureData:etree._Element) -> dict:
        """get properties from ThermoML file

        Args:
            pureOrMixtureData (etree._Element): pureOrMixtureData object that contains properties
            
        
        Note:
            compID is gonna be ignored if property is not component specific

        Returns:
            dict: dict of properties used in pureOrMixtureData. Keys: nPropNumber, Values: [Func, compID]
        """
        properties = dict()
        for property in pureOrMixtureData.findall(self.__NAMESPACE__ + 'Property'):
            if self.__getOneEntry__(property, 'nOrgNum'):
                compID = self.__getOneEntry__(property, 'nOrgNum')
            else:
                compID = None
            
            
            propID = self.__getOneEntry__(property, 'nPropNumber')
            method = self.__getOneEntry__(property, 'eMethodName')
            properties[propID] = (self.__getPropMapping__(self.__getOneEntry__(property, 'ePropName')),
                                                                         method, compID)
        return properties

    def __getPropMapping__(self, ePropName:str):
        """returns function that matches to ePropName

        Args:
            ePropName (str): name of property

        Returns:
            method: method that matches to ePropName
        """
        try:
            func = self.__propMapping__[ePropName]
            return func
        except KeyError:
            raise ThermoMLQuantityNotFoundError(ePropName)
        

    def __getVariables__(self, pureOrMixtureData:etree._Element) -> dict:
        """get variables from ThermoML file

        Args:
            pureOrMixtureData (etree._Element): pureOrMixtureData object that contains variables
        
        Note:
            compID is gonna be ignored if variable is not component specific

        Returns:
            dict: dict of variables used in pureOrMixtureData. Keys: nVarNumber, Values: [Func, compID]
        """
        variables = dict()
        for variable in pureOrMixtureData.findall(self.__NAMESPACE__ + 'Variable'):
            variableType = variable.findall(self.__NAMESPACE__ + 'VariableType')
            varName = variableType[0].getchildren()[0].text
            
            if self.__getOneEntry__(variable, 'nOrgNum'):
                compID = self.__getOneEntry__(variable, 'nOrgNum')
            else:
                compID = None
            
            varID = f"{self.__getOneEntry__(variable, 'nVarNumber')}"
            
            variables[varID] = (
                self.__getVarMapping__(varName), compID)
        return variables

    def __getVarMapping__(self, varName: str):
        """returns function that matches to varName

        Args:
            varName (str): name of variable

        Returns:
            method: s that matches to varName
        """
        try:
            func = self.__varMapping__[varName]
            return func
        except KeyError:
            raise ThermoMLQuantityNotFoundError(varName)
        

    def __getMeasurements__(self, experiment:PureOrMixtureData, pureOrMixtureData:etree._Element) -> PureOrMixtureData:
        """fill pureOrMixtureData object with measurement data from ThermoML file.

        Args:
            experiment (PureOrMixtureData): currently instanciated PureOrMixtureData object, that have to be filled in with data
            pureOrMixtureData (etree._Element): ThermoML file pureOrMixtureData entries

        Returns:
            PureOrMixtureData: filled pureOrMixtureData object
        """

        for measID, numValues in enumerate(pureOrMixtureData.findall(self.__NAMESPACE__ + 'NumValues')):
            if 'ID' in numValues.attrib:
                measID = numValues.attrib['ID']

            else:
                measID = f"{measID}"

            datapoints = []
            for variableValue in numValues.findall(self.__NAMESPACE__ + 'VariableValue'):
                try:
                    uncert = float(self.__getOneEntry__(
                        variableValue, 'nStdUncertValue'))
                except ValueError:
                    uncert = None
                except TypeError:
                    uncert = None

                try:
                    numbOfDig = int(self.__getOneEntry__(
                        variableValue, 'nVarDigits'))
                except ValueError:
                    numbOfDig = None
                except TypeError:
                    numbOfDig = None
                
                
                varID = self.__getOneEntry__(variableValue, 'nVarNumber')
                datapoints.append(DataPoint(measurementID=measID, value=float(self.__getOneEntry__(variableValue, 'nVarValue')),
                                  varID=varID, uncertainty=uncert, numberOfDigits=numbOfDig))

            for propertyValue in numValues.findall(self.__NAMESPACE__ + 'PropertyValue'):
                try:
                    uncert = float(self.__getOneEntry__(
                        propertyValue, 'nStdUncertValue'))
                except ValueError:
                    uncert = None
                except TypeError:
                    uncert = None

                try:
                    numbOfDig = int(self.__getOneEntry__(
                        propertyValue, 'nPropDigits'))
                except ValueError:
                    numbOfDig = None
                except TypeError:
                    numbOfDig = None
                
                propID = self.__getOneEntry__(propertyValue, "nPropNumber")
                datapoints.append(DataPoint(measurementID=measID, value=float(self.__getOneEntry__(propertyValue, 'nPropValue')),
                                  propID=propID, uncertainty=uncert, numberOfDigits=numbOfDig))
            
            measID = ""
            experiment.addMeasurement(dataPoints=datapoints)

        return experiment
