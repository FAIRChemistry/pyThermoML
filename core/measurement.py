'''
File: measurement.py
Project: core
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:35:56 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''

import json


class Measurement(object):

    def __init__(
        self,
        values,
        pureOrMixtureData
    ):

        self.properties = dict()
        self.variables = dict()

        # Iterate through values and check existence
        for ID, value in values.items():

            if ID in pureOrMixtureData.properties.keys():
                self.properties[ID] = value

            elif ID in pureOrMixtureData.variables.keys():
                self.variables[ID] = value

            else:
                raise NameError(
                    f"Property/Variable {ID} not defined in PureOrMixtureData object. Please define!"
                )

    def __str__(self):
        return json.dumps(
            self.__dict__,
            indent=4
        )
