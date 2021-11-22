'''
File: property.py
Project: props
Author: Jan Range
License: BSD-2 clause
-----
Last Modified: Tuesday June 29th 2021 3:10:28 pm
Modified By: Jan Range (<jan.range@simtech.uni-stuttgart.de>)
-----
Copyright (c) 2021 Institute of Biochemistry and Technical Biochemistry Stuttgart
'''


from pydantic import BaseModel
from pydantic.fields import PrivateAttr
from typing import Optional


class PropertyBase(BaseModel):

    propName: str
    propGroup: str
    ID: str
    unit: str
    method: str
    compoundID: Optional[str] = None
    _type: str = PrivateAttr(default="prop")
