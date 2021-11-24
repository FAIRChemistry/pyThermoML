from pythermo.thermoml.props.bioproperties import Bioproperty
from pythermo.thermoml.props.volumetricproperties import VolumetricProperty
from pythermo.thermoml.props.refractionSurfaceTensionSoundSpeedproperties import RefractionSurfaceTensionSoundSpeedproperty
from pythermo.thermoml.props.heatcapacityproperties import HeatCapacityProperty
from pythermo.thermoml.props.transportproperties import TransportProperty

from pythermo.thermoml.vars.temperature import TemperatureBase
from pythermo.thermoml.vars.pressure import PressureBase
from pythermo.thermoml.vars.componentcomposition import ComponentCompositionBase

from pythermo.thermoml.core import Compound, DataPoint, DataReport, PureOrMixtureData, ThermoMLSchemaError, ThermoMLMissingIDError, ThermoMLNoCompoundError
from lxml import etree
from pydantic import BaseModel, validator
from typing import Dict, Optional


class ThermoMLReader(BaseModel):
    path: str
    NAMESPACE: str = './/{http://www.iupac.org/namespaces/ThermoML}'
    propMapping: Dict = {
            'Viscosity, Pa*s': TransportProperty.viscosity,
            'Kinematic Viscosity, m2/s': TransportProperty.kinematicViscosity,
            'Self diffusion coefficient, m2/s': TransportProperty.selfDiffusionCoefficient,
            'Mass density, kg/m3': VolumetricProperty.massDensity,
            'Surface tension liquid-gas, N/m': RefractionSurfaceTensionSoundSpeedproperty.surfaceTension,
            'Speed of sound, m/s': RefractionSurfaceTensionSoundSpeedproperty.speedOfSound,
            'Molar heat capacity at constant pressure, J/K/mol': HeatCapacityProperty.molarHCconstPressure,
            'Molar heat capacity at constant volume, J/K/mol': HeatCapacityProperty.MolarHCconstVolume,
            'Peak temperature, K': Bioproperty.peakTemperature,

            # not in ThermoML
            'Microviscosity, Pa*s': TransportProperty.microViscosity
        }
    
    varMapping: Dict = {
            'Temperature, K': TemperatureBase.temperature,
            'Lower temperature, K': TemperatureBase.lowerTemperature,
            'Upper temperature, K': TemperatureBase.upperTemperature,
            'Mole fraction': ComponentCompositionBase.moleFraction,
            'Pressure, kPa': PressureBase.pressure
    }

    @validator('path')
    @classmethod
    def convertPath(cls, values):
        try:
            tree = etree.parse(values)

            return tree.getroot()
        except FileNotFoundError:
            print(f"Could not find ThermoML file")

    def readFromFile(self) -> DataReport:
        '''
        Reads ThermoML document to an object layer ThermoML

        Args:
            String path: Path to ThermoML file
        '''

        title = self.__getOneEntry__(self.path, tag="sTitle")
        doi = self.__getOneEntry__(self.path, tag= "sDOI")
        authors = self.__getAuthors__()
        
        datareport = DataReport(title=title, doi=doi, authors=authors)
        
        comps = self.__getCompounds__()
        
        for comp in comps.values():
            datareport.addCompound(comp)
        
        pOMData = self.__getPOMData__(comps)
        
        # experiment[0] Object
        # experiment[1] ElementTree
        for experiment in pOMData.values():
            props = self.__getProperties__(experiment[1])
            vars = self.__getVariables__(experiment[1])
            print(props)
            for id, value in props.items():
                
                experiment[0].addProperty(value[0](ID = id, method= value[1], compoundID=value[2]))
            
            for id, value in vars.items():
                print(value)
                experiment[0].addVariable(value[0](ID=id, compoundID=value[1]))
            
            datareport.addPureOrMixtureData(self.__getMeasurements__(experiment[0], experiment[1]))

        return datareport

    def __getOneEntry__(self, root, tag) -> str:
        """returns value of specified tag in ThermoML file

        Args:
            tag (str): name of the tag

        Raises:
            ThermoMLSchemaError: when tag con not be found in schema or multiple tags with same name are in file

        Returns:
            str: value of specified tag in ThermoML file
        """
        if root.findall(self.NAMESPACE + tag):
            if len(root.findall(self.NAMESPACE + tag)) == 1:
                return root.findall(self.NAMESPACE + tag)[0].text
            else:
                raise ThermoMLSchemaError(tag)


    def __getAuthors__(self) -> dict[str, str]:
        """returns authors dictionary from sAuthors tag in ThermoML file

        Args:
            root (etree._Element): etree._Element representation of ThermoML file

        Returns:
            dict[str, str]: dict of authors
        """
        if self.path.findall(self.NAMESPACE + 'sAuthor'):
            authorList = self.path.findall(self.NAMESPACE + 'sAuthor')
            authors = dict()

            for index, author in enumerate(authorList):
                authors[str(index)] = author.text

            return authors

    def __getCompounds__(self) -> dict:
        comps = dict()
        if self.path.findall(self.NAMESPACE + 'Compound'):
            
            for compound in self.path.findall(self.NAMESPACE + 'Compound'):
                comps[self.__getOneEntry__(compound, 'nOrgNum')] = Compound(
                    ID = self.__getOneEntry__(compound, 'nOrgNum'),
                    standardInchI = self.__getOneEntry__(compound, 'sStandardInchi'),
                    standardInchIKey = self.__getOneEntry__(compound, 'sStandardInchiKey'),
                    smiles = self.__getOneEntry__(compound, 'sSmiles'),
                    commonName = self.__getOneEntry__(compound, 'commonName')
                )
            
            return comps
        else:
            raise ThermoMLNoCompoundError()

    def __getPOMData__(self, comps) -> dict:
        '''
        Return dictionary of pureOrMixtureData in dataReport
        
        Key: nPureOrMixtureDataNumber
        Value: [PureOrMixtureData, pureOrMixtureData]
        First argument is Object of PureOrMixtureData, second argument returns ET Element. 
        -> only get following properties/variables of pureOrMixtureData, not whole path
        '''
        
        pOMData = dict()
        comps = list(comps.keys())
        if self.path.findall(self.NAMESPACE + 'PureOrMixtureData'):
            
            for pureOrMixtureData in self.path.findall(self.NAMESPACE + 'PureOrMixtureData'):
                # All declared compounds should be used in pure or mixture Data
                pOMData[self.__getOneEntry__(pureOrMixtureData, 'nPureOrMixtureDataNumber')] = (PureOrMixtureData(
                    ID = self.__getOneEntry__(pureOrMixtureData, 'nPureOrMixtureDataNumber'), 
                    comps = comps), pureOrMixtureData)

        print(pOMData)
        return pOMData

    def __getProperties__(self, pureOrMixtureData) -> dict:
        '''
        Return dictionary of properties used in pureOrMixtureData
        
        Key: nPropNumber
        Value: [Func, eMethodName]
        '''
        properties = dict()
        for property in pureOrMixtureData.findall(self.NAMESPACE + 'Property'):
            try:
                compID = self.__getOneEntry__(property, 'nOrgNum')
            except IndexError:
                raise ThermoMLMissingIDError('nOrgNum')
    
            properties[self.__getOneEntry__(property, 'nPropNumber')] = (self.__getPropMapping__(self.__getOneEntry__(property, 'ePropName')),
            self.__getOneEntry__(property, 'eMethodName'), compID)
        return properties


    def __getPropMapping__(self, ePropName):
        '''
        Returns function that matches to ePropName
        '''
        try:
            func = self.propMapping[ePropName]
        except KeyError:
            print('Property not found')
        return func

    def __getVariables__(self, pureOrMixtureData) -> dict:
        '''
        Returns dict of variables used in pureOrMixtureData
        
        Key: nVarNumber
        Value: [Func, compID]
        compID is gonna be ignored if variable is not component specific
        '''

        variables = dict()
        for variable in pureOrMixtureData.findall(self.NAMESPACE + 'Variable'):
            variableType = variable.findall(self.NAMESPACE + 'VariableType')
            varName = variableType[0].getchildren()[0].text
            try:
                compID = self.__getOneEntry__(variable, 'nOrgNum')
            except IndexError:
                compID = ""
            
            variables[self.__getOneEntry__(variable, 'nVarNumber')] = (self.__getVarMapping__(varName), compID)
        return variables

    def __getVarMapping__(self, varName):
        '''
        Return function that matches to variable
        '''
        try:
            func = self.varMapping[varName]
        except KeyError:
            print('Variable not found')
        return func

    def __getMeasurements__(self, experiment, pureOrMixtureData):

        measID = 0
        for numValues in pureOrMixtureData.findall(self.NAMESPACE + 'NumValues'):        
            if 'ID' in numValues.attrib:
                measID = numValues.attrib['ID']
            else:
                # default measurmentIDs
                measID = int(measID)
                measID+= 1
                measID = str(measID)

            datapoints = []
            for variableValue in numValues.findall(self.NAMESPACE + 'VariableValue'):
                try:
                    uncert = float(self.__getOneEntry__(variableValue, 'nExpandUncertValue'))
                except ValueError:
                    uncert = None
                except TypeError:
                    uncert = None
                
                try:
                    numbOfDig = int(self.__getOneEntry__(variableValue, 'nVarDigits'))
                except ValueError:
                    numbOfDig = None
                except TypeError:
                    numbOfDig = None
                datapoints.append(DataPoint(measurementID=measID, value=float(self.__getOneEntry__(variableValue, 'nVarValue')), varID = self.__getOneEntry__(variableValue, 'nVarNumber'), uncertainty=uncert, numberOfDigits=numbOfDig))

            for propertyValue in numValues.findall(self.NAMESPACE + 'PropertyValue'):
                try:
                    uncert = float(self.__getOneEntry__(propertyValue, 'nCombExpandUncertValue'))
                except ValueError:
                    uncert = None
                except TypeError:
                    uncert = None
                
                try:
                    numbOfDig = int(self.__getOneEntry__(propertyValue, 'nPropDigits'))
                except ValueError:
                    numbOfDig = None
                except TypeError:
                    numbOfDig = None  
                datapoints.append(DataPoint(measurementID=measID, value=float(self.__getOneEntry__(propertyValue, 'nPropValue')), propID =self.__getOneEntry__(propertyValue, 'nPropNumber'), uncertainty= uncert, numberOfDigits=numbOfDig))
            experiment.addMeasurement(dataPoints=datapoints)

        return experiment