from pythermo.thermoml.core import PureOrMixtureData, Measurement, DataReport, Compound, DataPoint, datapoint, measurement

from pythermo.thermoml.vars.componentcomposition import MoleFraction
from pythermo.thermoml.vars.temperature import LowerTemperature, Temperature
from pythermo.thermoml.vars.pressure import Pressure
from pythermo.thermoml.props.transportproperties import Viscosity, Diffusioncoefficient
from pythermo.thermoml.props.volumetricproperties import MassDensity


import json
import csv

file = "data/test_05.csv"

def makeDataRep():
    
    
    with open(file, 'r') as csvfile:
        datareader = csv.reader(csvfile, delimiter=',')

        dataReps = []
        counter = 0
        for rows in datareader:
            
            if counter > 0 :
                print(rows[0])
                dataReport = DataReport(title=rows[14])
                comp = Compound("134", standardInchi=None, standardInchiKey=None, smiles=None, commonName="pentane")
                compID = dataReport.addCompound(comp)
                experiment = PureOrMixtureData("ID", compID)

                #variables
                temp = Temperature('temp')        
                prs = Pressure('prs')

                #properties
                visc = Viscosity('visc', method=None)
                dens = MassDensity('dens', method=None)
                dc = Diffusioncoefficient('dc', method=None)

                tempID = experiment.addVariable(temp)
                prsID = experiment.addVariable(prs)

                viscID = experiment.addProperty(visc)
                densID = experiment.addProperty(dens)
                dcID = experiment.addProperty(dc)

                measurementID = rows[14]
                print(rows[0])
                tempDataPoint = DataPoint(measurementID=measurementID, value=rows[0],varID=tempID)
                prsDataPoint = DataPoint(measurementID=measurementID, value=rows[1],varID=prsID)
                viscDataPoint = DataPoint(measurementID=measurementID, value=rows[2],propID=viscID)
                densDataPoint = DataPoint(measurementID=measurementID, value=rows[3],propID=densID)
                dcDataPoint = DataPoint(measurementID=measurementID, value=rows[7],propID=dcID)

                datapoints = [tempDataPoint, prsDataPoint, viscDataPoint, densDataPoint, dcDataPoint]

                experiment.addMeasurement(dataPoints=datapoints)
                dataReport.addPureOrMixtureData(experiment)
                dataReps.append(dataReport)
                counter+=1
            else:
                counter += 1
makeDataRep()
        