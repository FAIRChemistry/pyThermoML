import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .regnum import RegNum
from .propertygroup import PropertyGroup


@forge_signature
class PropertyMethodID(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_comp_index: Optional[int] = element(
        default=None, tag="nCompIndex", json_schema_extra=dict(xml="nCompIndex")
    )
    property_group: Optional[PropertyGroup] = element(
        default_factory=PropertyGroup,
        tag="PropertyGroup",
        json_schema_extra=dict(xml="PropertyGroup"),
    )
    reg_num: Optional[RegNum] = element(
        default_factory=RegNum, tag="RegNum", json_schema_extra=dict(xml="RegNum")
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
