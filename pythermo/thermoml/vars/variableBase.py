'''
File: variableBase.py
Project: vars
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:12:14 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''
from pydantic import BaseModel
from pydantic.fields import PrivateAttr
from typing import Optional

import json


class VariableBase(BaseModel):

    varType: str
    varName: str
    ID: str
    unit: str
    compoundID: Optional[str] = None
    _type: str = PrivateAttr(default="Variable")
