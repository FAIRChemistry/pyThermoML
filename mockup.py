'''
File: mockup.py
Project: pyThermoML
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:22:37 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

# Initialize dataReport parent class
dataRep = DataReport(
    "Hallo",
    "DOI",
    "Name"
)

# Define compounds
comp1 = Compound()
comp2 = Compound()

comp1_ID = dataRep.addCompound(comp1)
comp2_ID = dataRep.addCompound(comp2)

# Initialize PureMixtureData
experiment1 = PureMixtureData()

# Define properties
prop1 = peakTemperature('ID')
prop2 = viscocity('ID2')

# Define Variables
var1 = temperature('ID3')

prop1_ID = experiment1.addProperty()
prop2_ID = experiment1.addProperty()
var1_ID = experiment1.addVariable()

# Measurement
meas = Measurement(
    prop1_ID=10.0,
    prop2_ID=20.0,
    var1_ID=20.0
)

