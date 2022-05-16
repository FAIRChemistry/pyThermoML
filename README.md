# PyThermoML

**Authors:** Matthias Gueltig, Jan Range

This project provides the first means to interact with the ThermoML format. The library is written in python. Please type the following commands to make pyThermoML run

```
git https://github.com/FAIRChemistry/pyThermoML.git
cd pyThermoML
python setup.py develop
```

This library depends on the following libraries:

* pydantic
* lxml

# Structure

PyThermoML can be divided into four packages: Core, props, vars and tools:

**Core**:
The core package contains the base classes of pyThermoML, which inherit from pydantic’s [1] BaseModel. They are data classes containing operations to interact with integrated data. 
An object of the **DataReport** class forms the basis for the integration of a data set. Each DataReport object contains two dictionaries: The values of the first dictionary are objects of the **Compound** class. The keys are the corresponding Compound IDs. The values of the second dictionary are objects of the **PureOrMixtureData** class. The keys are the corresponding **PureOrMixtureData** IDs.
Objects of the **Compound** class must have an ID, and can contain the following attributes: standardInchI, standardInchIKey, smilesCode and commonName. 
Objects of the **PureOrMixtureData** class have an ID, a list with the IDs of the used compounds and three dictionaries where objects of the PropertyBase, VariableBase and Measurement class are associated by IDs.
Objects of the **Measurement** class have an ID and consist of two dictionaries that are used to associate objects of the DataPoint class by IDs. One dictionary for variables and one dictionary for properties.
Objects of the **DataPoint** class have the ID of the **Measurement** object they refer to, and the value of the corresponding variable or property. The varID/propID defines whether the **DataPoint** object describes a property or a variable. A **DataPoint** object contains just one value, so either the propID or varID is None. If no property/variable can be associated, a TypeError is thrown. The attribute data_point_type is automatically set to the value "property" or "variable" when creating a **DataPoint** object. In addition, the attribute numberOfDigits can be specified. In case of multiple measurements, the attribute uncertainty can be specified. The uncertainty is the standard deviation around the corresponding measured value.

**Props and Vars**:
Properties and variables are defined in the props/vars package. All implemented properties/variables inherit from the **VariableBase** or **PropertyBase**. 
Objects of type **PropertyBase** (and their child classes) have a propName, propGroup, ID, unit, method, and, if the examined property is component specific a compoundID. In the base class, ID and method are validated. method has either the value "simulation", "experiment", or "other". Otherwise, a TypeError is thrown.
The attributes that have not yet been specified are defined in the child classes. For example, the propGroup "VolumetricProp" is defined for volumetric properties. All properties are instantiated via classmethods. For example, the operation massDensity() allocates the porpName with the value “Mass density” and the unit with "kg/m3". Thus for each property, the units are prescribed by pyThermoML. The compoundID in this case is "None", since the density of a liquid mixture is not component specific.
Except for the attribute method, which is not an attribute of the VariableBase analogue considerations apply to child classes of the VariableBase. The decisive factor is: New properties/variables, that are not included in the API can be implemented via this inheritance concept with little implementation effort. Writer and Reader must be adapted if necessary. PyThermoML maps the following properties:
* volumetric properties: mass density [kg/m^3 ]   
* heat capacity properties: molar heat capacity at constant pressure [J/(K*mol)], molar heat capacity at constant volume [J/(K*mol)]
* transport properties: viscosity [Pa*s], kinematic viscosity [m^2/s], self-diffusion coefficient [m^2/s]
* bioproperties: peakTemperature [K]
* other: surface tension [N/m], speed of sound [m/s]

These variables are mapped by pyThermoML:
* component composition: mole fraction []
* temperatures: temperature [K], upper temperature [K], lower temperature [K]
* pressure: pressure [kPa]

**Tools**: 
In the tools package pyThermoML provides functionalities to transform a DataReport - object in different file formats. The package is divided into the classes **ThermoMLReader**, **ThermoMLWriter** and **ThermoMLDaRUSHandler**.
Objects of type **ThermoMLReader** contain the namespace of ThermoML and the path to the ThermoML file (.xml) or JSON file (.json) that must be read in. The path is validated by file name extension. In addition, each **ThermoMLReader** object contains two dictionaries. They contain as keys the names of the properties/variables stored in ThermoML, and as values the corresponding classmethods of child classes of the PropertyBase/VariableBase. If new properties/variables are added to the API, this dictionary must be updated. This is the reason why almost no change needs to be made in the readFromThermoMLFile() method, which is responsible for the actual reading process. Tags of the ThermoML file are read in via the lxml.etree module [2].
When reading JSON files via the readFromJSON() method, only the parse_file() operation of pydantic is called.
Objects of type **ThermoMLWriter** contain a dataRep, which is the dictionary representation of a DataReport after validation. Individual entries of the ThermoML file can be created via lxml.etree.[2] With etree.QName a wrapper for the ThermoML namespace is created. The function writeThermo() writes the dataRep to a filename which is also an attribute of the **ThermoMLWriter** class.
The class **ThermoMLDaRUSHandler** provides functionalitie for DaRUS interaction. The uploadToDaRUS method exctracts metadata of a locally generated ThermoML file and uploads the file and two metadata blocks to a specified DaRUS dataverse. With downloadFromDaRUS ThermoML files on DaRUS can be downloaded.

# Example for API Usage
Considering a basic example: A mass density of pure water of 1000 kg/m^3 at 273.15K has been measured. The experimental data can be written into a basic .json file as below.
```json
{
    "title": "name of your paper",
    "authors": {
        "author1": "your name"
    },
    "compounds": {
        "c1": {
            "commonName": "water",
            "ID": "c1"
        }
    },
    "pureOrMixtureData": {
        "pom1": {
            "ID": "pom1",
            "comps": [
                "c1"
            ],
            "properties": {
                "pdens": {
                    "propName": "Mass density",
                    "ID": "pdens",
                    "propGroup": "VolumetricProp",
                    "method": "experiment",
                    "unit": "kg/m3"
                }
            },
            "variables": {
                "vtemp": {
                    "varName": "Temperature",
                    "ID": "vtemp",
                    "unit": "K",
                    "varType": "eTemperature"
                }
            },
            "measurements": {
                "meas1": {
                    "ID": "meas1",
                    "properties": {
                        "pdens": {
                            "measurementID": "meas1",
                            "propID": "pdens",
                            "value": 1000
                        }
                    },
                    "variables": {
                        "vtemp": {
                            "measurementID": "meas1",
                            "varID": "vtemp",
                            "value": 293.15
                        }
                    }
                }
            }
        }
    }
}
```
Some other mandatory parameters for instance IDs, units are specified. With the propGroup/varType keyword the corresponding property/variable groups referring to ThermoML – schema must be defined.

The .json representation can be used as input for pyThermoML. An automated workflow with other examples can be found [here](https://github.com/FAIRChemistry/pyThermoML/tree/master/pyThermoML_example_workflow).

