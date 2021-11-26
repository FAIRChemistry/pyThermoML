[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matzegltg/pyThermoML.git/HEAD)

# PyThermoML

**Authors:** Matthias Gueltig, Jan Range
**License:** BSD 2 Clause - see the [License] for details.

This project provides the first means to interact with the ThermoML format. The library is written in python, and is avalable in PyPi, so all you sholud need to do is run:

```
pip install PyThermoML
```

## Examples

Let's consider the following .json file as result of your measuremnt:

```
{
    "title": "Title of referred paper",
    "DOI": "DOI of referred paper",    
    "authors": {
        "author0": "author1",
        "author1": "author2"
    },
    "compounds": {
        "c1": {
            "standardInchI": "inhi1",
            "standardInchIKey": "inchikey1",
            "commonName": "water",
            "ID": "c1"
        },
        "c2": {
            "smiles": "smiles2",
            "commonName": "ethanol",
            "ID": "c2"
        }
    },
    "pureOrMixtureData": {
        "pom1": {
            "ID": "pom1",
            "comps": [
                "c1",
                "c2"
            ],
            "properties": {
                "pvisc1": {
                    "propName": "Viscosity",
                    "ID": "pvisc1",
                    "propGroup": "TransportProp",
                    "unit": "Pa*s",
                    "method": "simulation"
                }
            },
            "variables": {
                "vtemp1": {
                    "varName": "Temperature",
                    "ID": "vtemp1",
                    "unit": "K",
                    "varType": "eTemperature"
                },
                "vmoleFrac1": {
                    "varName": "Mole fraction",
                    "ID": "vmoleFrac1",
                    "unit": "",
                    "compoundID": "c1",
                    "varType": "eComponentComposition"
                },
                "vmoleFrac2": {
                    "varName": "Mole fraction",
                    "ID": "vmoleFrac2",
                    "unit": "",
                    "compoundID": "c2",
                    "varType": "eComponentComposition"
                }
            },
            "measurements": {
                "meas1": {
                    "ID": "meas1",
                    "properties": {
                        "pvisc1": [
                            {
                                "measurementID": "meas1",
                                "value": 10.0,
                                "uncertainty": 0.1,
                                "ID": "pvisc1"
                            }
                        ]
                    },
                    "variables": {
                        "vtemp1": [
                            {
                                "measurementID": "meas1",
                                "value": 300.0,
                                "uncertainty": 10.0,
                                "ID": "vtemp1"
                            }
                        ],
                        "vmoleFrac1": [
                            {
                                "measurementID": "meas1",
                                "value": 0.2,
                                "uncertainty": 0.01,
                                "ID": "vmoleFrac1"
                            }
                        ],
                        "vmoleFrac2": [
                            {
                                "measurementID": "meas1",
                                "value": 0.8,
                                "uncertainty": 0.02,
                                "ID": "vMoleFrac2"
                            }
                        ]
                    }
                }
            }
        }
    }
}
```
Attention: The project is continuously being worked on.
## Test
```
'''
File: exampleWriteThermo.py
Project: examples
Author: Matthias Gueltig, Jan Range
License: BSD-2 clause
-----
Last Modified: Thursday November 25th 2021
Modified By: Matthias Gueltig (<matthias2906@t-online.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

from flask.helpers import send_file
from pythermo.thermoml.core import PureOrMixtureData, DataReport, Compound, DataPoint

from pythermo.thermoml.vars.componentcomposition import ComponentCompositionBase
from pythermo.thermoml.vars.temperature import TemperatureBase
from pythermo.thermoml.vars.pressure import PressureBase
from pythermo.thermoml.props.transportproperties import TransportProperty
from pythermo.thermoml.props.volumetricproperties import VolumetricProperty

from pythermo.thermoml.tools.writeTools import ThermoMLWriter
from pythermo.thermoml.tools.readTools import ThermoMLReader
import json
from pathlib import Path

from pydantic.json import pydantic_encoder
from lxml import etree
# TODO: reading input data from excel spreadsheet

# title, DOI, authors
authors = {
    "author 1": "Koichi Takamura",
    "author 2": "Herbert Fischer",
    "author 3": "Norman R. Morrow"
}

dataReport = DataReport(title="Physical properties of aqueous glycerol solutions",
                        DOI="10.1016/j.petrol.2012.09.003", authors=authors)


# declaration of compound used in measurements
# TODO: Compound ID is fix? 1,2,3,... in ThermoML integers necesarry
comp1 = Compound(ID="c1", standardInchI="InChI=1S/H2O/h1H2",
                 standardInchIKey="XLYOFNOQVPJJNP-UHFFFAOYSA-N", smiles="O", commonName="water")
comp2 = Compound(ID="c2", standardInchI="InChI=1S/C3H8O3/c4-1-3(6)2-5/h3-6H,1-2H2",
                 standardInchIKey="PEDCQBHIVMGVHV-UHFFFAOYSA-N", smiles="C(C(CO)O)O", commonName="glycerol")


comp1_ID = dataReport.addCompound(comp1)
comp2_ID = dataReport.addCompound(comp2)

comps = [comp1_ID, comp2_ID]
# components which are used in respective experiment
experiment = PureOrMixtureData(ID="pom1", comps=comps)

# property definitions
dens = VolumetricProperty.massDensity(ID='p1', method='simulation')
sdiffCoeff1 = TransportProperty.selfDiffusionCoefficient(
    ID="p2", method='simulation', compoundID=comp1_ID)
sdiffCoeff2 = TransportProperty.selfDiffusionCoefficient(
    ID="p3", method='simulation', compoundID=comp2_ID)

# Variable definitions
temp = TemperatureBase.temperature(ID="v1")

frac1 = ComponentCompositionBase.moleFraction('v2', comp1_ID)
frac2 = ComponentCompositionBase.moleFraction('v3', comp2_ID)

densID = experiment.addProperty(dens)
dffCoeff1ID = experiment.addProperty(sdiffCoeff1)
dffCoeff2ID = experiment.addProperty(sdiffCoeff2)
tempID = experiment.addVariable(temp)
frac1ID = experiment.addVariable(frac1)
frac2ID = experiment.addVariable(frac2)

# not used in ThermoML
measurementID = "meas1"

viscDataPoint = DataPoint(
    measurementID=measurementID,
    value=10.0,
    propID=densID,
)

sdiff1DataPoint1 = DataPoint(
    measurementID=measurementID,
    value=10334,
    propID=dffCoeff1ID
)

sdiff2DataPoint1 = DataPoint(
    measurementID=measurementID,
    value=123123,
    propID=dffCoeff2ID
)

tempDataPoint = DataPoint(
    measurementID=measurementID,
    value=300.0,
    varID=tempID,
)

frac1DataPoint = DataPoint(
    measurementID=measurementID,
    value=0.2,
    varID=frac1ID,
)

frac2DataPoint = DataPoint(
    measurementID=measurementID,
    value=0.8,
    varID=frac2ID,
)

measurementID = "meas2"
sdiff1DataPoint2 = DataPoint(
    measurementID=measurementID,
    value=10334,
    propID=dffCoeff1ID
)

sdiff2DataPoint2 = DataPoint(
    measurementID=measurementID,
    value=123123,
    propID=dffCoeff2ID
)
viscDataPoint2 = DataPoint(
    measurementID=measurementID,
    value=1000.0,
    propID=densID,
    uncertainty=0.1
)

tempDataPoint2 = DataPoint(
    measurementID=measurementID,
    value=1000.0,
    varID=tempID,
    uncertainty=10.0
)

frac1DataPoint2 = DataPoint(
    measurementID=measurementID,
    value=1000.0,
    varID=frac1ID,
    uncertainty=0.01
)

frac2DataPoint2 = DataPoint(
    measurementID=measurementID,
    value=1000,
    varID=frac2ID,
    uncertainty=0.02
)

datapoints = [viscDataPoint, sdiff1DataPoint1, sdiff2DataPoint1,
              tempDataPoint, frac1DataPoint, frac2DataPoint]

datapoints2 = [viscDataPoint2, sdiff1DataPoint2, sdiff2DataPoint2, tempDataPoint2,
               frac1DataPoint2, frac2DataPoint2]
# add Measurement to experiment
experiment.addMeasurement(dataPoints=datapoints)
experiment.addMeasurement(dataPoints=datapoints2)

#print(experiment.getMoleFractionIDs())
# add experiment to dataReport
dataReport.addPureOrMixtureData(experiment)


#print(y.getPureOrMixtureData('pom1').measurements)

writer = ThermoMLWriter(dataRep=dataReport, filename="testThermo.xml")
writer.writeThermo()
"""
#file = etree.parse("testThermo.xml")
#print(etree.tostring(file, pretty_print=True, encoding=str))
"""

reader = ThermoMLReader(path="testThermo.xml")
dataRepr = reader.readFromFile()

#print(dataRepr.json(exclude_none=True, indent=4))
#print(dataRepr.authors)
#print(dataReport.getPureOrMixtureData("1").json(exclude_none=True, indent=4))

```
