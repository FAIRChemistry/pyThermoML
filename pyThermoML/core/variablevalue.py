import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .varrepeatability import VarRepeatability
from .varuncertainty import VarUncertainty


@forge_signature
class VariableValue(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_var_digits: Optional[int] = element(
        default=None, tag="nVarDigits", json_schema_extra=dict(xml="nVarDigits")
    )
    n_var_number: Optional[int] = element(
        default=None, tag="nVarNumber", json_schema_extra=dict(xml="nVarNumber")
    )
    n_var_value: Optional[float] = element(
        default=None, tag="nVarValue", json_schema_extra=dict(xml="nVarValue")
    )
    n_var_device_spec_value: Optional[float] = element(
        default=None,
        tag="nVarDeviceSpecValue",
        json_schema_extra=dict(xml="nVarDeviceSpecValue"),
    )
    var_repeatability: Optional[VarRepeatability] = element(
        default_factory=VarRepeatability,
        tag="VarRepeatability",
        json_schema_extra=dict(xml="VarRepeatability"),
    )
    var_uncertainty: List[VarUncertainty] = element(
        default_factory=ListPlus,
        tag="VarUncertainty",
        json_schema_extra=dict(multiple=True, xml="VarUncertainty"),
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

    def add_to_var_uncertainty(
        self,
        n_uncert_assess_num: Optional[int] = None,
        n_coverage_factor: Optional[float] = None,
        n_expand_uncert_value: Optional[float] = None,
        n_std_uncert_value: Optional[float] = None,
        n_uncert_lev_of_confid: Optional[float] = None,
        s_uncert_eval_method: Optional[str] = None,
        s_uncert_evaluator: Optional[str] = None,
        **kwargs
    ) -> VarUncertainty:
        """
        This method adds an object of type 'VarUncertainty' to attribute var_uncertainty

        Args:

            n_uncert_assess_num (): . Defaults to None
            n_coverage_factor (): . Defaults to None
            n_expand_uncert_value (): . Defaults to None
            n_std_uncert_value (): . Defaults to None
            n_uncert_lev_of_confid (): . Defaults to None
            s_uncert_eval_method (): . Defaults to None
            s_uncert_evaluator (): . Defaults to None
        """
        params = {
            "n_uncert_assess_num": n_uncert_assess_num,
            "n_coverage_factor": n_coverage_factor,
            "n_expand_uncert_value": n_expand_uncert_value,
            "n_std_uncert_value": n_std_uncert_value,
            "n_uncert_lev_of_confid": n_uncert_lev_of_confid,
            "s_uncert_eval_method": s_uncert_eval_method,
            "s_uncert_evaluator": s_uncert_evaluator,
        }
        if id is not None:
            params["id"] = id
        self.var_uncertainty.append(VarUncertainty(**params))
        return self.var_uncertainty[-1]
