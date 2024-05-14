import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class Journal(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    s_coden: Optional[str] = element(
        description="The CODEN identification of the journal",
        default=None,
        tag="sCODEN",
        json_schema_extra=dict(xml="sCODEN"),
    )

    s_issn: Optional[str] = element(
        description="The International Standard Subscription Number",
        default=None,
        tag="sISSN",
        json_schema_extra=dict(xml="sISSN"),
    )

    s_issue: Optional[str] = element(
        description="Issue number, usually indicates month",
        default=None,
        tag="sIssue",
        json_schema_extra=dict(xml="sIssue"),
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
