# PyThermoML

**Authors:** Matthias Gueltig, Jan Range

This project provides the first means to interact with the ThermoML format. The library is written in python. Please type the following commands to make pyThermoML run

```
git clone https://github.com/ThermoPyML/pyThermoML.git
cd pyThermoML
python setup.py install
```

This library depends on the following libraries:

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

## Attention:
The project is continuously being worked on. 
