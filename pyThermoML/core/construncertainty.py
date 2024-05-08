import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class ConstrUncertainty(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_coverage_factor: Optional[float] = element(
        default=None,
        tag="nCoverageFactor",
        json_schema_extra=dict(xml="nCoverageFactor"),
    )
    n_expand_uncert_value: Optional[float] = element(
        default=None,
        tag="nExpandUncertValue",
        json_schema_extra=dict(xml="nExpandUncertValue"),
    )
    n_std_uncert_value: Optional[float] = element(
        default=None,
        tag="nStdUncertValue",
        json_schema_extra=dict(xml="nStdUncertValue"),
    )
    n_uncert_lev_of_confid: Optional[float] = element(
        default=None,
        tag="nUncertLevOfConfid",
        json_schema_extra=dict(xml="nUncertLevOfConfid"),
    )
    s_uncert_eval_method: Optional[str] = element(
        default=None,
        tag="sUncertEvalMethod",
        json_schema_extra=dict(xml="sUncertEvalMethod"),
    )
    s_uncert_evaluator: Optional[str] = element(
        default=None,
        tag="sUncertEvaluator",
        json_schema_extra=dict(xml="sUncertEvaluator"),
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
