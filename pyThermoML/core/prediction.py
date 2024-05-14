import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .elanguage import eLanguage
from .trcrefid import TRCRefID
from .esourcetype import eSourceType
from .book import Book
from .predictionmethodref import PredictionMethodRef
from .epredictiontype import ePredictionType
from .etype import eType
from .thesis import Thesis
from .journal import Journal


@forge_signature
class Prediction(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_prediction_type: Union[ePredictionType, str, None] = element(
        default=None,
        tag="ePredictionType",
        json_schema_extra=dict(xml="ePredictionType"),
    )
    prediction_method_ref: List[PredictionMethodRef] = element(
        default_factory=ListPlus,
        tag="PredictionMethodRef",
        json_schema_extra=dict(multiple=True, xml="PredictionMethodRef"),
    )
    s_prediction_method_description: Optional[str] = element(
        default=None,
        tag="sPredictionMethodDescription",
        json_schema_extra=dict(xml="sPredictionMethodDescription"),
    )
    s_prediction_method_name: Optional[str] = element(
        default=None,
        tag="sPredictionMethodName",
        json_schema_extra=dict(xml="sPredictionMethodName"),
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

    def add_to_prediction_method_ref(
        self,
        book: Optional[Book] = None,
        journal: Optional[Journal] = None,
        thesis: Optional[Thesis] = None,
        date_cit: Optional[str] = None,
        e_language: Union[eLanguage, str, None] = None,
        e_source_type: Union[eSourceType, str, None] = None,
        e_type: Union[eType, str, None] = None,
        s_abstract: Optional[str] = None,
        s_author: List[str] = ListPlus(),
        s_cas_cit: Optional[str] = None,
        s_document_origin: Optional[str] = None,
        s_doi: Optional[str] = None,
        s_id_num: Optional[str] = None,
        s_keyword: List[str] = ListPlus(),
        s_location: Optional[str] = None,
        s_page: Optional[str] = None,
        s_pub_name: Optional[str] = None,
        s_title: Optional[str] = None,
        s_vol: Optional[str] = None,
        trc_ref_id: Optional[TRCRefID] = None,
        url_cit: Optional[str] = None,
        yr_pub_yr: Optional[str] = None,
        **kwargs
    ) -> PredictionMethodRef:
        """
        This method adds an object of type 'PredictionMethodRef' to attribute prediction_method_ref

        Args:

            book (): . Defaults to None
            journal (): . Defaults to None
            thesis (): . Defaults to None
            date_cit (): Date of the citation. Defaults to None
            e_language (): Language of publication. Defaults to None
            e_source_type (): The source status type for a citation. Defaults to None
            e_type (): The type of publication. Defaults to None
            s_abstract (): An abstract of the publication. Defaults to None
            s_author (): Author of publication. Defaults to ListPlus()
            s_cas_cit (): The Chemical Abstracts Service citation. Defaults to None
            s_document_origin (): Company, institution, or conference name. Defaults to None
            s_doi (): DOI. Defaults to None
            s_id_num (): Identification number, e.g., a patent number or a document number. Defaults to None
            s_keyword (): . Defaults to ListPlus()
            s_location (): Reference to a location. Defaults to None
            s_page (): Page range where the publication can be found. Defaults to None
            s_pub_name (): Name of the publication.. Defaults to None
            s_title (): Title of the publication. Defaults to None
            s_vol (): Volume number. Defaults to None
            trc_ref_id (): . Defaults to None
            url_cit (): URL to the publication. Defaults to None
            yr_pub_yr (): Publication year. Defaults to None
        """
        params = {
            "book": book,
            "journal": journal,
            "thesis": thesis,
            "date_cit": date_cit,
            "e_language": e_language,
            "e_source_type": e_source_type,
            "e_type": e_type,
            "s_abstract": s_abstract,
            "s_author": s_author,
            "s_cas_cit": s_cas_cit,
            "s_document_origin": s_document_origin,
            "s_doi": s_doi,
            "s_id_num": s_id_num,
            "s_keyword": s_keyword,
            "s_location": s_location,
            "s_page": s_page,
            "s_pub_name": s_pub_name,
            "s_title": s_title,
            "s_vol": s_vol,
            "trc_ref_id": trc_ref_id,
            "url_cit": url_cit,
            "yr_pub_yr": yr_pub_yr,
        }
        if id is not None:
            params["id"] = id
        self.prediction_method_ref.append(PredictionMethodRef(**params))
        return self.prediction_method_ref[-1]
