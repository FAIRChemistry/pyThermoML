import json
import pandas as pd
import numpy as np

# Get the line mapping
lineMap = json.load(open("tableMapping.json"))

# Read file
file = open("Alkane/05.txt", encoding="ISO-8859-1").readlines()[183::]

# Track individual data
data = list()

for line in file[:-1]:
    dataDict = dict()
    for key, (leftIndex, rightIndex) in lineMap.items():

        if key == "state":
            values = line[leftIndex:rightIndex]
            state, prop, ref = list(filter(
                None,
                values.split(' ')
            ))

            dataDict["state"] = state
            dataDict["prop"] = prop
            dataDict["reference"] = ref.replace("[", "").replace("]", "")

        else:

            value = line[leftIndex:rightIndex].replace(' ', '')

            if value:
                dataDict[key] = float(value)
            else:
                dataDict[key] = np.nan

    data.append(dataDict)

pd.DataFrame(data).to_csv("test_05.csv", sep=",", index=False)
