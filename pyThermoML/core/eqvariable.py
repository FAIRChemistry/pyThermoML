import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict


@forge_signature
class EqVariable(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_pure_or_mixture_data_number: Optional[int] = element(
        default=None,
        tag="nPureOrMixtureDataNumber",
        json_schema_extra=dict(xml="nPureOrMixtureDataNumber"),
    )
    n_reaction_data_number: Optional[int] = element(
        default=None,
        tag="nReactionDataNumber",
        json_schema_extra=dict(xml="nReactionDataNumber"),
    )
    n_var_number: Optional[int] = element(
        default=None, tag="nVarNumber", json_schema_extra=dict(xml="nVarNumber")
    )
    s_eq_symbol: Optional[str] = element(
        default=None, tag="sEqSymbol", json_schema_extra=dict(xml="sEqSymbol")
    )
    n_eq_var_index: List[int] = element(
        default_factory=ListPlus,
        tag="nEqVarIndex",
        json_schema_extra=dict(multiple=True, xml="nEqVarIndex"),
    )
    n_eq_var_range_max: Optional[float] = element(
        default=None, tag="nEqVarRangeMax", json_schema_extra=dict(xml="nEqVarRangeMax")
    )
    n_eq_var_range_min: Optional[float] = element(
        default=None, tag="nEqVarRangeMin", json_schema_extra=dict(xml="nEqVarRangeMin")
    )
    s_other_var_unit: Optional[str] = element(
        default=None, tag="sOtherVarUnit", json_schema_extra=dict(xml="sOtherVarUnit")
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
