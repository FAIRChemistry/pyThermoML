import sdRDM

from typing import Dict, Optional, Union
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .edevicespecmethod import eDeviceSpecMethod


@forge_signature
class ConstrDeviceSpec(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_device_spec_method: Union[eDeviceSpecMethod, str, None] = element(
        default=None,
        tag="eDeviceSpecMethod",
        json_schema_extra=dict(xml="eDeviceSpecMethod"),
    )
    n_device_spec_lev_of_confid: Optional[float] = element(
        default=None,
        tag="nDeviceSpecLevOfConfid",
        json_schema_extra=dict(xml="nDeviceSpecLevOfConfid"),
    )
    n_device_spec_value: Optional[float] = element(
        default=None,
        tag="nDeviceSpecValue",
        json_schema_extra=dict(xml="nDeviceSpecValue"),
    )
    s_device_spec_evaluator: Optional[str] = element(
        default=None,
        tag="sDeviceSpecEvaluator",
        json_schema_extra=dict(xml="sDeviceSpecEvaluator"),
    )
    s_device_spec_method: Optional[str] = element(
        default=None,
        tag="sDeviceSpecMethod",
        json_schema_extra=dict(xml="sDeviceSpecMethod"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/SimTech-Research-Data-Management/ThermoML-Specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="374af92aef0e91313c5c390226161b9876735345"
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
