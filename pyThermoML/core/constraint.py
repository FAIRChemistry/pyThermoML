import sdRDM

from typing import Dict, List, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .constrdevicespec import ConstrDeviceSpec
from .constraintid import ConstraintID
from .solvent import Solvent
from .constrrepeatability import ConstrRepeatability
from .constraintphaseid import ConstraintPhaseID
from .construncertainty import ConstrUncertainty


@forge_signature
class Constraint(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    constraint_id: Optional[ConstraintID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=ConstraintID,
        tag="ConstraintID",
        json_schema_extra=dict(xml="ConstraintID"),
    )
    n_constr_digits: Optional[int] = element(
        default=None, tag="nConstrDigits", json_schema_extra=dict(xml="nConstrDigits")
    )
    n_constraint_value: Optional[float] = element(
        default=None,
        tag="nConstraintValue",
        json_schema_extra=dict(xml="nConstraintValue"),
    )
    constr_device_spec: Optional[ConstrDeviceSpec] = element(
        default_factory=ConstrDeviceSpec,
        tag="ConstrDeviceSpec",
        json_schema_extra=dict(xml="ConstrDeviceSpec"),
    )
    constr_repeatability: Optional[ConstrRepeatability] = element(
        default_factory=ConstrRepeatability,
        tag="ConstrRepeatability",
        json_schema_extra=dict(xml="ConstrRepeatability"),
    )
    constr_uncertainty: List[ConstrUncertainty] = element(
        default_factory=ListPlus,
        tag="ConstrUncertainty",
        json_schema_extra=dict(multiple=True, xml="ConstrUncertainty"),
    )

    constraint_phase_id: Optional[ConstraintPhaseID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=ConstraintPhaseID,
        tag="ConstraintPhaseID",
        json_schema_extra=dict(xml="ConstraintPhaseID"),
    )
    n_constraint_number: Optional[int] = element(
        default=None,
        tag="nConstraintNumber",
        json_schema_extra=dict(xml="nConstraintNumber"),
    )
    solvent: Optional[Solvent] = element(
        default_factory=Solvent, tag="Solvent", json_schema_extra=dict(xml="Solvent")
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

    def add_to_constr_uncertainty(
        self,
        n_coverage_factor: Optional[float] = None,
        n_expand_uncert_value: Optional[float] = None,
        n_std_uncert_value: Optional[float] = None,
        n_uncert_lev_of_confid: Optional[float] = None,
        s_uncert_eval_method: Optional[str] = None,
        s_uncert_evaluator: Optional[str] = None,
        **kwargs
    ) -> ConstrUncertainty:
        """
        This method adds an object of type 'ConstrUncertainty' to attribute constr_uncertainty

        Args:

            n_coverage_factor (): . Defaults to None
            n_expand_uncert_value (): . Defaults to None
            n_std_uncert_value (): . Defaults to None
            n_uncert_lev_of_confid (): . Defaults to None
            s_uncert_eval_method (): . Defaults to None
            s_uncert_evaluator (): . Defaults to None
        """
        params = {
            "n_coverage_factor": n_coverage_factor,
            "n_expand_uncert_value": n_expand_uncert_value,
            "n_std_uncert_value": n_std_uncert_value,
            "n_uncert_lev_of_confid": n_uncert_lev_of_confid,
            "s_uncert_eval_method": s_uncert_eval_method,
            "s_uncert_evaluator": s_uncert_evaluator,
        }
        if id is not None:
            params["id"] = id
        self.constr_uncertainty.append(ConstrUncertainty(**params))
        return self.constr_uncertainty[-1]
