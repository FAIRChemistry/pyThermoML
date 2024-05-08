import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .varphaseid import VarPhaseID
from .solvent import Solvent
from .varrepeatability import VarRepeatability
from .variableid import VariableID
from .vardevicespec import VarDeviceSpec
from .varuncertainty import VarUncertainty


@forge_signature
class Variable(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_var_number: Optional[int] = element(
        default=None, tag="nVarNumber", json_schema_extra=dict(xml="nVarNumber")
    )

    variable_id: Optional[VariableID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=VariableID,
        tag="VariableID",
        json_schema_extra=dict(xml="VariableID"),
    )
    solvent: Optional[Solvent] = element(
        default_factory=Solvent, tag="Solvent", json_schema_extra=dict(xml="Solvent")
    )
    var_device_spec: Optional[VarDeviceSpec] = element(
        default_factory=VarDeviceSpec,
        tag="VarDeviceSpec",
        json_schema_extra=dict(xml="VarDeviceSpec"),
    )

    var_phase_id: Optional[VarPhaseID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=VarPhaseID,
        tag="VarPhaseID",
        json_schema_extra=dict(xml="VarPhaseID"),
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
