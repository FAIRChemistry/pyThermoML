import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class Book(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    s_chapter: Optional[str] = element(
        description="Chapter number",
        default=None,
        tag="sChapter",
        json_schema_extra=dict(xml="sChapter"),
    )

    s_edition: Optional[str] = element(
        description="Edition number of the book",
        default=None,
        tag="sEdition",
        json_schema_extra=dict(xml="sEdition"),
    )

    s_editor: List[str] = element(
        description="Editor of the book",
        default_factory=ListPlus,
        tag="sEditor",
        json_schema_extra=dict(multiple=True, xml="sEditor"),
    )

    s_isbn: Optional[str] = element(
        description="The International Standard Book Number",
        default=None,
        tag="sISBN",
        json_schema_extra=dict(xml="sISBN"),
    )

    s_publisher: Optional[str] = element(
        description="Publisher name and city",
        default=None,
        tag="sPublisher",
        json_schema_extra=dict(xml="sPublisher"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="4014e57ac2f3b9b09cdefb1c3e2f2cfca298f660"
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
