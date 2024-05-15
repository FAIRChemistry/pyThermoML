import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class EqParameter(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_eq_par_digits: Optional[int] = element(
        default=None, tag="nEqParDigits", json_schema_extra=dict(xml="nEqParDigits")
    )
    n_eq_par_value: Optional[float] = element(
        default=None, tag="nEqParValue", json_schema_extra=dict(xml="nEqParValue")
    )
    s_eq_par_symbol: Optional[str] = element(
        default=None, tag="sEqParSymbol", json_schema_extra=dict(xml="sEqParSymbol")
    )
    n_eq_par_index: List[int] = element(
        default_factory=ListPlus,
        tag="nEqParIndex",
        json_schema_extra=dict(multiple=True, xml="nEqParIndex"),
    )
    n_eq_par_number: Optional[int] = element(
        default=None, tag="nEqParNumber", json_schema_extra=dict(xml="nEqParNumber")
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="4d2d23abb157f43b563c9d44de5b83e37a50b96b"
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
