import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .singleprop import SingleProp
from .equationofstate import EquationOfState
from .multiprop import MultiProp


@forge_signature
class CriticalEvaluation(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    equation_of_state: Optional[EquationOfState] = element(
        default_factory=EquationOfState,
        tag="EquationOfState",
        json_schema_extra=dict(xml="EquationOfState"),
    )
    multi_prop: Optional[MultiProp] = element(
        default_factory=MultiProp,
        tag="MultiProp",
        json_schema_extra=dict(xml="MultiProp"),
    )
    single_prop: Optional[SingleProp] = element(
        default_factory=SingleProp,
        tag="SingleProp",
        json_schema_extra=dict(xml="SingleProp"),
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
