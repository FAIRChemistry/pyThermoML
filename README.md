[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/matzegltg/pyThermoML.git/HEAD)

# PyThermoML

**Authors:** Matthias Gueltig, Jan Range
**License:** BSD 2 Clause - see the [License] for details.

This project provides the first means to interact with the ThermoML format. The library is written in python, and is avalable in PyPi, so all you sholud need to do is run:

```
git install PyThermoML
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