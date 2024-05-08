import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .book import Book
from .thesis import Thesis
from .trcrefid import TRCRefID
from .journal import Journal
from .etype import eType
from .esourcetype import eSourceType
from .elanguage import eLanguage


@forge_signature
class PredictionMethodRef(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    book: Optional[Book] = element(
        default_factory=Book, tag="book", json_schema_extra=dict(xml="book")
    )
    journal: Optional[Journal] = element(
        default_factory=Journal, tag="journal", json_schema_extra=dict(xml="journal")
    )
    thesis: Optional[Thesis] = element(
        default_factory=Thesis, tag="thesis", json_schema_extra=dict(xml="thesis")
    )

    date_cit: Optional[str] = element(
        description="Date of the citation",
        default=None,
        tag="dateCit",
        json_schema_extra=dict(xml="dateCit"),
    )

    e_language: Union[eLanguage, str, None] = element(
        description="Language of publication",
        default=None,
        tag="eLanguage",
        json_schema_extra=dict(xml="eLanguage"),
    )

    e_source_type: Union[eSourceType, str, None] = element(
        description="The source status type for a citation",
        default=None,
        tag="eSourceType",
        json_schema_extra=dict(xml="eSourceType"),
    )

    e_type: Union[eType, str, None] = element(
        description="The type of publication",
        default=None,
        tag="eType",
        json_schema_extra=dict(xml="eType"),
    )

    s_abstract: Optional[str] = element(
        description="An abstract of the publication",
        default=None,
        tag="sAbstract",
        json_schema_extra=dict(xml="sAbstract"),
    )

    s_author: List[str] = element(
        description="Author of publication",
        default_factory=ListPlus,
        tag="sAuthor",
        json_schema_extra=dict(multiple=True, xml="sAuthor"),
    )

    s_cas_cit: Optional[str] = element(
        description="The Chemical Abstracts Service citation",
        default=None,
        tag="sCASCit",
        json_schema_extra=dict(xml="sCASCit"),
    )

    s_document_origin: Optional[str] = element(
        description="Company, institution, or conference name",
        default=None,
        tag="sDocumentOrigin",
        json_schema_extra=dict(xml="sDocumentOrigin"),
    )

    s_doi: Optional[str] = element(
        description="DOI",
        default=None,
        tag="sDOI",
        json_schema_extra=dict(xml="sDOI"),
    )

    s_id_num: Optional[str] = element(
        description="Identification number, e.g., a patent number or a document number",
        default=None,
        tag="sIDNum",
        json_schema_extra=dict(xml="sIDNum"),
    )
    s_keyword: List[str] = element(
        default_factory=ListPlus,
        tag="sKeyword",
        json_schema_extra=dict(multiple=True, xml="sKeyword"),
    )

    s_location: Optional[str] = element(
        description="Reference to a location",
        default=None,
        tag="sLocation",
        json_schema_extra=dict(xml="sLocation"),
    )

    s_page: Optional[str] = element(
        description="Page range where the publication can be found",
        default=None,
        tag="sPage",
        json_schema_extra=dict(xml="sPage"),
    )

    s_pub_name: Optional[str] = element(
        description="Name of the publication.",
        default=None,
        tag="sPubName",
        json_schema_extra=dict(xml="sPubName"),
    )

    s_title: Optional[str] = element(
        description="Title of the publication",
        default=None,
        tag="sTitle",
        json_schema_extra=dict(xml="sTitle"),
    )

    s_vol: Optional[str] = element(
        description="Volume number",
        default=None,
        tag="sVol",
        json_schema_extra=dict(xml="sVol"),
    )
    trc_ref_id: Optional[TRCRefID] = element(
        default_factory=TRCRefID, tag="TRCRefID", json_schema_extra=dict(xml="TRCRefID")
    )

    url_cit: Optional[str] = element(
        description="URL to the publication",
        default=None,
        tag="urlCit",
        json_schema_extra=dict(xml="urlCit"),
    )

    yr_pub_yr: Optional[str] = element(
        description="Publication year",
        default=None,
        tag="yrPubYr",
        json_schema_extra=dict(xml="yrPubYr"),
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
