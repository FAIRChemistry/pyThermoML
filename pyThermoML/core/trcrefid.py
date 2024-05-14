import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class TRCRefID(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_authorn: Optional[int] = element(
        description="Integer identifier to distinguish conflicts",
        default=None,
        tag="nAuthorn",
        json_schema_extra=dict(xml="nAuthorn"),
    )

    s_author1: Optional[str] = element(
        description="First 3 characters of Author 1 last name",
        default=None,
        tag="sAuthor1",
        json_schema_extra=dict(xml="sAuthor1"),
    )

    s_author2: Optional[str] = element(
        description="First 3 characters of Author 2 last name",
        default=None,
        tag="sAuthor2",
        json_schema_extra=dict(xml="sAuthor2"),
    )

    yr_yr_pub: Optional[int] = element(
        description="Integer year of publication",
        default=None,
        tag="yrYrPub",
        json_schema_extra=dict(xml="yrYrPub"),
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
