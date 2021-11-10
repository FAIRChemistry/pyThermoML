from pythermo.thermoml.tools.readTools import readThermo
import json
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np

dataRep = readThermo("DataGudrunGygli/cml2ThermoML/ChCl_glycerol/ChCl_glycerol_DOI2.xml")

df = dataRep.createDataFrame()
print(df)
#print(pd.unique(df[['water', 'glycerol', 'choline chloride', 'urea', 'ethylene glycol', 'methanol', "N,N-Diethylethanolammonium chloride"]].values.ravel('K')))
#print(pd.concat([df['water'], df['glycerol'], df['choline chloride']]).unique())

print(df[['water', 'glycerol', 'choline chloride', 'urea', 'ethylene glycol', 'methanol', "N,N-Diethylethanolammonium chloride"]].values)
plt.close("all")
x = df["1/RT (mol/kj)"].values
y = df["ln(eta) (cP)"].values

x = x.reshape(-1,1)
regressor = LinearRegression()
regressor.fit(x,y)
y_pred = regressor.predict(x)

plt.scatter(x, y)
plt.plot(x, regressor.predict(x))
plt.title('arrhenius plot')
plt.xlabel('1/RT (mol/kj)')
plt.ylabel('ln(eta) (cP)')
plt.grid()
plt.show()