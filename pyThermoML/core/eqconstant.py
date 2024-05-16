import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class EqConstant(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_eq_constant_digits: Optional[int] = element(
        default=None,
        tag="nEqConstantDigits",
        json_schema_extra=dict(xml="nEqConstantDigits"),
    )
    n_eq_constant_value: Optional[float] = element(
        default=None,
        tag="nEqConstantValue",
        json_schema_extra=dict(xml="nEqConstantValue"),
    )
    s_eq_constant_symbol: Optional[str] = element(
        default=None,
        tag="sEqConstantSymbol",
        json_schema_extra=dict(xml="sEqConstantSymbol"),
    )
    n_eq_constant_index: List[int] = element(
        default_factory=ListPlus,
        tag="nEqConstantIndex",
        json_schema_extra=dict(multiple=True, xml="nEqConstantIndex"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="decc3d7428f0517c8bc0428fd9785112138a62f6"
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
