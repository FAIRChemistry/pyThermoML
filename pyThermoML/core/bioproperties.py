import sdRDM

from typing import Dict, Optional, Union
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .epropname import ePropName
from .criticalevaluation import CriticalEvaluation
from .prediction import Prediction
from .emethodname import eMethodName


@forge_signature
class BioProperties(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    critical_evaluation: Optional[CriticalEvaluation] = element(
        default_factory=CriticalEvaluation,
        tag="CriticalEvaluation",
        json_schema_extra=dict(xml="CriticalEvaluation"),
    )
    e_method_name: Union[eMethodName, str, None] = element(
        default=None, tag="eMethodName", json_schema_extra=dict(xml="eMethodName")
    )
    e_prop_name: Union[ePropName, str, None] = element(
        default=None, tag="ePropName", json_schema_extra=dict(xml="ePropName")
    )
    prediction: Optional[Prediction] = element(
        default_factory=Prediction,
        tag="Prediction",
        json_schema_extra=dict(xml="Prediction"),
    )
    s_method_name: Optional[str] = element(
        default=None, tag="sMethodName", json_schema_extra=dict(xml="sMethodName")
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
