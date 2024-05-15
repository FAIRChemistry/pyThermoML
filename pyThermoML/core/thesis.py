import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class Thesis(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    s_deg: Optional[str] = element(
        description="Academic degree designation, e.g., MS or PhD",
        default=None,
        tag="sDeg",
        json_schema_extra=dict(xml="sDeg"),
    )

    s_deg_inst: Optional[str] = element(
        description="Academic degree granting institution",
        default=None,
        tag="sDegInst",
        json_schema_extra=dict(xml="sDegInst"),
    )

    s_umi_pub_num: Optional[str] = element(
        description="University Microfilms International Publication Number",
        default=None,
        tag="sUMIPubNum",
        json_schema_extra=dict(xml="sUMIPubNum"),
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
