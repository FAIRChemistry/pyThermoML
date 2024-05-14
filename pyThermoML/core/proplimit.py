import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class PropLimit(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_prop_limit_digits: Optional[int] = element(
        default=None,
        tag="nPropLimitDigits",
        json_schema_extra=dict(xml="nPropLimitDigits"),
    )
    n_prop_lower_limit_value: Optional[float] = element(
        default=None,
        tag="nPropLowerLimitValue",
        json_schema_extra=dict(xml="nPropLowerLimitValue"),
    )
    n_prop_upper_limit_value: Optional[float] = element(
        default=None,
        tag="nPropUpperLimitValue",
        json_schema_extra=dict(xml="nPropUpperLimitValue"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="7847845987ccfa50e8c08ada56669b59d1b97819"
    )
    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                (isinstance(i, _Element) for i in value)
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)
        return self
