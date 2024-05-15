import sdRDM

from typing import Dict, Optional, Union
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .erepeatmethod import eRepeatMethod


@forge_signature
class VarRepeatability(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_repeat_method: Union[eRepeatMethod, str, None] = element(
        default=None, tag="eRepeatMethod", json_schema_extra=dict(xml="eRepeatMethod")
    )
    n_repetitions: Optional[int] = element(
        default=None, tag="nRepetitions", json_schema_extra=dict(xml="nRepetitions")
    )
    n_var_repeat_value: Optional[float] = element(
        default=None,
        tag="nVarRepeatValue",
        json_schema_extra=dict(xml="nVarRepeatValue"),
    )
    s_repeat_evaluator: Optional[str] = element(
        default=None,
        tag="sRepeatEvaluator",
        json_schema_extra=dict(xml="sRepeatEvaluator"),
    )
    s_repeat_method: Optional[str] = element(
        default=None, tag="sRepeatMethod", json_schema_extra=dict(xml="sRepeatMethod")
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
