# @File          :   pureOrMixtureData.py
# @Last modified :   2022/04/09 18:57:31
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from enum import Enum
from typing import Optional
from pydantic import BaseModel, validator


class ConstraintType(Enum):

    ePressure = "Pressure, kPa"


class Constraint(BaseModel):
    """class representing constraints

    Args:
        number (int): Integer identifier for the given constraint
        const
    """

    number: int
    constraint_id: ConstraintType
    phase_id: str
    value: float
    digits: Optional[int] = None

    @validator("digits")
    def get_digits(cls, value, values):
        """Returns number of digits of a given value"""

        if not values.get("value"):
            return None

        return len(str(value).replace(".", ""))
