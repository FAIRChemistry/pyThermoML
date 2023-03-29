# @File          :   combineduncertainty.py
# @Last modified :   2022/04/09 19:28:22
# @Author        :   Matthias Gueltig, Jan Range
# @Version       :   1.0
# @License       :   BSD-2-Clause License
# @Copyright (C) :   2022 Institute of Biochemistry and Technical Biochemistry Stuttgart

from typing import Optional
from pydantic import BaseModel


class CombinedUncertainty(BaseModel):
    """class representing experimental/simulated pure or mixture data

    Args:
        number (int): Numerical ID of this cuncertainty
        value (int): Uncertainty value

    """

    ID: int
    value: float
    evaluator: Optional[str] = None
    evaluation_method: Optional[str] = None
    level_of_confidence: Optional[int] = None
