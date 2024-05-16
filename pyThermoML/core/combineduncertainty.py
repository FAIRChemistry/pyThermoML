import sdRDM

from typing import Dict, Optional, Union
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .asymcombstduncert import AsymCombStdUncert
from .asymcombexpanduncert import AsymCombExpandUncert
from .ecombuncertevalmethod import eCombUncertEvalMethod


@forge_signature
class CombinedUncertainty(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_comb_uncert_eval_method: Union[eCombUncertEvalMethod, str, None] = element(
        default=None,
        tag="eCombUncertEvalMethod",
        json_schema_extra=dict(xml="eCombUncertEvalMethod"),
    )
    n_comb_uncert_assess_num: Optional[int] = element(
        default=None,
        tag="nCombUncertAssessNum",
        json_schema_extra=dict(xml="nCombUncertAssessNum"),
    )
    asym_comb_expand_uncert: Optional[AsymCombExpandUncert] = element(
        default_factory=AsymCombExpandUncert,
        tag="AsymCombExpandUncert",
        json_schema_extra=dict(xml="AsymCombExpandUncert"),
    )
    asym_comb_std_uncert: Optional[AsymCombStdUncert] = element(
        default_factory=AsymCombStdUncert,
        tag="AsymCombStdUncert",
        json_schema_extra=dict(xml="AsymCombStdUncert"),
    )
    n_comb_coverage_factor: Optional[float] = element(
        default=None,
        tag="nCombCoverageFactor",
        json_schema_extra=dict(xml="nCombCoverageFactor"),
    )
    n_comb_expand_uncert_value: Optional[float] = element(
        default=None,
        tag="nCombExpandUncertValue",
        json_schema_extra=dict(xml="nCombExpandUncertValue"),
    )
    n_comb_std_uncert_value: Optional[float] = element(
        default=None,
        tag="nCombStdUncertValue",
        json_schema_extra=dict(xml="nCombStdUncertValue"),
    )
    n_comb_uncert_lev_of_confid: Optional[float] = element(
        default=None,
        tag="nCombUncertLevOfConfid",
        json_schema_extra=dict(xml="nCombUncertLevOfConfid"),
    )
    s_comb_uncert_eval_method: Optional[str] = element(
        default=None,
        tag="sCombUncertEvalMethod",
        json_schema_extra=dict(xml="sCombUncertEvalMethod"),
    )
    s_comb_uncert_evaluator: Optional[str] = element(
        default=None,
        tag="sCombUncertEvaluator",
        json_schema_extra=dict(xml="sCombUncertEvaluator"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="decc3d7428f0517c8bc0428fd9785112138a62f6"
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
