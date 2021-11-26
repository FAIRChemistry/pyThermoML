[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matzegltg/pyThermoML.git/HEAD)

# PyThermoML

**Authors:** Matthias Gueltig, Jan Range
**License:** BSD 2 Clause - see the [License](https://github.com/matzegltg/pyThermoML/blob/master/LICENSE) for details.

This project provides the first means to interact with the ThermoML format. The library is written in python, and is avalable on PyPi, so all you sholud need to do is run:

```
pip install PyThermoML
```

This library depends on the following libraries:

* typing
* dataclasses
* pathlib
* pydantic
* lxml

## General Information
This API provides the following properties:
* volumetric properties:
    * mass density (kg/m3)
* heat capacity properties:
    * molar heat capacity at constant pressure (J/K/mol)
    * molar heat capacity at constant volume (J/K/mol)
* transport properties:
    * viscosity (Pa*s)
    * kinematic viscosity (m2/s)
    * microviscosity (Pa*s)
    * self dffusion coefficient (m2/s)
* bioproperties:
    * peakTemperature (K)
* other:
    * surface tension (N/m) 
    * speed of sound (m/s)

This API provides the following variables:
* component composition:
    * mole fraction ()
* temperatures:
    * temperature(K)
    * upper temperature(K)
    * lower temperature(K)
* pressure:
    * pressure (kPa)
    

The units are fixed and cannot be changed - otherwise you will receive error messages. For more information visit ThermoML schema definition.

## Examples

Let's consider an easy example for explanation how pyThermoML works: In this case you have measured a mass density of pure water of 1000 kg/m^3 at 273.15K. If you are interessted in storing your data in a structured way you could use basic functionalities of pyThermoML. All you need to do is write your experimental data into a basic .json file as you can see below or [here](https://github.com/matzegltg/pyThermoML/blob/master/templates/githubExample.json).

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
Some other mandatory parameters for instance IDs units units are also specified. With the propGroup/varType keyword the respective property/variable groups referring to [ThermoML - schema](http://media.iupac.org/namespaces/ThermoML/ThermoML.xsd) have to be defined. The rest is done by the API.

You can read in the .json file with the following code excerpt:

```python
from pythermo.thermoml.tools.readTools import ThermoMLReader

# create ThermoMLReader object to create a new DataReport object.
reader = ThermoMLReader(path="githubExample.json")
dataReport = reader.readFromJSON()
```

With the generated dataReport object you could for instance acces your experimental value for mass density as follows:
```python 
dataReport.getPureOrMixtureData("pom1").getMeasurement("meas1").getProperty("pdens").value
```
This excerpt will return 1000.

Finally experimental/simulated data can be stored in a structured way by creating ThermoML .xml files:

```python
from pythermo.thermoml.tools.writeTools import ThermoMLWriter

# suppose .json file is stored named 'githubExample.json'
# create ThermoMLWriter object to convert .json file to ThermoML file.
writer = ThermoMLWriter(dataRep="githubExample.json", filename="githubExample.xml")
writer.writeThermo()
```

The generated 'githubExample.xml' is available [here](https://github.com/matzegltg/pyThermoML/blob/master/templates/githubExample.xml). 
For more information please visit [templates](https://github.com/matzegltg/pyThermoML/tree/master/templates).

##Attention:
The project is continuously being worked on. Interacting between .json, .xml, and DataReport object works.
