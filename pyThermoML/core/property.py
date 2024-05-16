import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .ecombuncertevalmethod import eCombUncertEvalMethod
from .ephase import ePhase
from .propertymethodid import PropertyMethodID
from .solvent import Solvent
from .epresentation import ePresentation
from .catalyst import Catalyst
from .proprepeatability import PropRepeatability
from .propuncertainty import PropUncertainty
from .propphaseid import PropPhaseID
from .combineduncertainty import CombinedUncertainty
from .refphaseid import RefPhaseID
from .asymcombexpanduncert import AsymCombExpandUncert
from .asymcombstduncert import AsymCombStdUncert
from .propdevicespec import PropDeviceSpec
from .curvedev import CurveDev
from .ecrystallatticetype import eCrystalLatticeType
from .asymexpanduncert import AsymExpandUncert
from .estandardstate import eStandardState
from .ebiostate import eBioState
from .epropphase import ePropPhase
from .asymstduncert import AsymStdUncert
from .regnum import RegNum
from .erefstatetype import eRefStateType


@forge_signature
class Property(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_presentation: Union[ePresentation, str, None] = element(
        default=None, tag="ePresentation", json_schema_extra=dict(xml="ePresentation")
    )
    n_pressure_digits: Optional[int] = element(
        default=None,
        tag="nPressureDigits",
        json_schema_extra=dict(xml="nPressureDigits"),
    )
    n_pressure_pa: Optional[float] = element(
        default=None, tag="nPressure-kPa", json_schema_extra=dict(xml="nPressure-kPa")
    )
    n_prop_number: Optional[int] = element(
        default=None, tag="nPropNumber", json_schema_extra=dict(xml="nPropNumber")
    )
    n_ref_pressure: Optional[float] = element(
        default=None, tag="nRefPressure", json_schema_extra=dict(xml="nRefPressure")
    )
    n_ref_pressure_digits: Optional[int] = element(
        default=None,
        tag="nRefPressureDigits",
        json_schema_extra=dict(xml="nRefPressureDigits"),
    )
    n_ref_temp: Optional[float] = element(
        default=None, tag="nRefTemp", json_schema_extra=dict(xml="nRefTemp")
    )
    n_ref_temp_digits: Optional[int] = element(
        default=None, tag="nRefTempDigits", json_schema_extra=dict(xml="nRefTempDigits")
    )
    n_temperature_digits: Optional[int] = element(
        default=None,
        tag="nTemperatureDigits",
        json_schema_extra=dict(xml="nTemperatureDigits"),
    )
    n_temperature_k: Optional[float] = element(
        default=None, tag="nTemperature-K", json_schema_extra=dict(xml="nTemperature-K")
    )

    property_method_id: Optional[PropertyMethodID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=PropertyMethodID,
        tag="Property-MethodID",
        json_schema_extra=dict(xml="Property-MethodID"),
    )
    catalyst: List[Catalyst] = element(
        default_factory=ListPlus,
        tag="Catalyst",
        json_schema_extra=dict(multiple=True, xml="Catalyst"),
    )
    combined_uncertainty: List[CombinedUncertainty] = element(
        default_factory=ListPlus,
        tag="CombinedUncertainty",
        json_schema_extra=dict(multiple=True, xml="CombinedUncertainty"),
    )
    curve_dev: List[CurveDev] = element(
        default_factory=ListPlus,
        tag="CurveDev",
        json_schema_extra=dict(multiple=True, xml="CurveDev"),
    )
    e_ref_state_type: Union[eRefStateType, str, None] = element(
        default=None, tag="eRefStateType", json_schema_extra=dict(xml="eRefStateType")
    )
    e_standard_state: Union[eStandardState, str, None] = element(
        default=None, tag="eStandardState", json_schema_extra=dict(xml="eStandardState")
    )
    prop_device_spec: Optional[PropDeviceSpec] = element(
        default_factory=PropDeviceSpec,
        tag="PropDeviceSpec",
        json_schema_extra=dict(xml="PropDeviceSpec"),
    )

    prop_phase_id: List[PropPhaseID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=ListPlus,
        tag="PropPhaseID",
        json_schema_extra=dict(multiple=True, xml="PropPhaseID"),
    )
    prop_repeatability: Optional[PropRepeatability] = element(
        default_factory=PropRepeatability,
        tag="PropRepeatability",
        json_schema_extra=dict(xml="PropRepeatability"),
    )
    prop_uncertainty: List[PropUncertainty] = element(
        default_factory=ListPlus,
        tag="PropUncertainty",
        json_schema_extra=dict(multiple=True, xml="PropUncertainty"),
    )

    ref_phase_id: Optional[RefPhaseID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=RefPhaseID,
        tag="RefPhaseID",
        json_schema_extra=dict(xml="RefPhaseID"),
    )
    solvent: Optional[Solvent] = element(
        default_factory=Solvent, tag="Solvent", json_schema_extra=dict(xml="Solvent")
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="09a845c92b96665129bf0265d21674b8b92bf834"
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

    def add_to_catalyst(
        self,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        e_phase: Union[ePhase, str, None] = None,
        **kwargs
    ) -> Catalyst:
        """
        This method adds an object of type 'Catalyst' to attribute catalyst

        Args:

            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            e_phase (): . Defaults to None
        """
        params = {"n_comp_index": n_comp_index, "reg_num": reg_num, "e_phase": e_phase}
        if id is not None:
            params["id"] = id
        self.catalyst.append(Catalyst(**params))
        return self.catalyst[-1]

    def add_to_combined_uncertainty(
        self,
        e_comb_uncert_eval_method: Union[eCombUncertEvalMethod, str, None] = None,
        n_comb_uncert_assess_num: Optional[int] = None,
        asym_comb_expand_uncert: Optional[AsymCombExpandUncert] = None,
        asym_comb_std_uncert: Optional[AsymCombStdUncert] = None,
        n_comb_coverage_factor: Optional[float] = None,
        n_comb_expand_uncert_value: Optional[float] = None,
        n_comb_std_uncert_value: Optional[float] = None,
        n_comb_uncert_lev_of_confid: Optional[float] = None,
        s_comb_uncert_eval_method: Optional[str] = None,
        s_comb_uncert_evaluator: Optional[str] = None,
        **kwargs
    ) -> CombinedUncertainty:
        """
        This method adds an object of type 'CombinedUncertainty' to attribute combined_uncertainty

        Args:

            e_comb_uncert_eval_method (): . Defaults to None
            n_comb_uncert_assess_num (): . Defaults to None
            asym_comb_expand_uncert (): . Defaults to None
            asym_comb_std_uncert (): . Defaults to None
            n_comb_coverage_factor (): . Defaults to None
            n_comb_expand_uncert_value (): . Defaults to None
            n_comb_std_uncert_value (): . Defaults to None
            n_comb_uncert_lev_of_confid (): . Defaults to None
            s_comb_uncert_eval_method (): . Defaults to None
            s_comb_uncert_evaluator (): . Defaults to None
        """
        params = {
            "e_comb_uncert_eval_method": e_comb_uncert_eval_method,
            "n_comb_uncert_assess_num": n_comb_uncert_assess_num,
            "asym_comb_expand_uncert": asym_comb_expand_uncert,
            "asym_comb_std_uncert": asym_comb_std_uncert,
            "n_comb_coverage_factor": n_comb_coverage_factor,
            "n_comb_expand_uncert_value": n_comb_expand_uncert_value,
            "n_comb_std_uncert_value": n_comb_std_uncert_value,
            "n_comb_uncert_lev_of_confid": n_comb_uncert_lev_of_confid,
            "s_comb_uncert_eval_method": s_comb_uncert_eval_method,
            "s_comb_uncert_evaluator": s_comb_uncert_evaluator,
        }
        if id is not None:
            params["id"] = id
        self.combined_uncertainty.append(CombinedUncertainty(**params))
        return self.combined_uncertainty[-1]

    def add_to_curve_dev(
        self,
        n_curve_dev_assess_num: Optional[int] = None,
        n_curve_dev_value: Optional[float] = None,
        s_curve_spec: Optional[str] = None,
        n_curve_rms_dev_value: Optional[float] = None,
        n_curve_rms_relative_dev_value: Optional[float] = None,
        s_curve_dev_evaluator: Optional[str] = None,
        **kwargs
    ) -> CurveDev:
        """
        This method adds an object of type 'CurveDev' to attribute curve_dev

        Args:

            n_curve_dev_assess_num (): . Defaults to None
            n_curve_dev_value (): . Defaults to None
            s_curve_spec (): . Defaults to None
            n_curve_rms_dev_value (): . Defaults to None
            n_curve_rms_relative_dev_value (): . Defaults to None
            s_curve_dev_evaluator (): . Defaults to None
        """
        params = {
            "n_curve_dev_assess_num": n_curve_dev_assess_num,
            "n_curve_dev_value": n_curve_dev_value,
            "s_curve_spec": s_curve_spec,
            "n_curve_rms_dev_value": n_curve_rms_dev_value,
            "n_curve_rms_relative_dev_value": n_curve_rms_relative_dev_value,
            "s_curve_dev_evaluator": s_curve_dev_evaluator,
        }
        if id is not None:
            params["id"] = id
        self.curve_dev.append(CurveDev(**params))
        return self.curve_dev[-1]

    def add_to_prop_phase_id(
        self,
        e_bio_state: Union[eBioState, str, None] = None,
        e_crystal_lattice_type: Union[eCrystalLatticeType, str, None] = None,
        e_prop_phase: Union[ePropPhase, str, None] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        s_bio_state: Optional[str] = None,
        s_phase_description: Optional[str] = None,
        **kwargs
    ) -> PropPhaseID:
        """
        This method adds an object of type 'PropPhaseID' to attribute prop_phase_id

        Args:

            e_bio_state (): . Defaults to None
            e_crystal_lattice_type (): . Defaults to None
            e_prop_phase (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            s_bio_state (): . Defaults to None
            s_phase_description (): . Defaults to None
        """
        params = {
            "e_bio_state": e_bio_state,
            "e_crystal_lattice_type": e_crystal_lattice_type,
            "e_prop_phase": e_prop_phase,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "s_bio_state": s_bio_state,
            "s_phase_description": s_phase_description,
        }
        if id is not None:
            params["id"] = id
        self.prop_phase_id.append(PropPhaseID(**params))
        return self.prop_phase_id[-1]

    def add_to_prop_uncertainty(
        self,
        n_uncert_assess_num: Optional[int] = None,
        asym_expand_uncert: Optional[AsymExpandUncert] = None,
        asym_std_uncert: Optional[AsymStdUncert] = None,
        n_coverage_factor: Optional[float] = None,
        n_expand_uncert_value: Optional[float] = None,
        n_std_uncert_value: Optional[float] = None,
        n_uncert_lev_of_confid: Optional[float] = None,
        s_uncert_eval_method: Optional[str] = None,
        s_uncert_evaluator: Optional[str] = None,
        **kwargs
    ) -> PropUncertainty:
        """
        This method adds an object of type 'PropUncertainty' to attribute prop_uncertainty

        Args:

            n_uncert_assess_num (): . Defaults to None
            asym_expand_uncert (): . Defaults to None
            asym_std_uncert (): . Defaults to None
            n_coverage_factor (): . Defaults to None
            n_expand_uncert_value (): . Defaults to None
            n_std_uncert_value (): . Defaults to None
            n_uncert_lev_of_confid (): . Defaults to None
            s_uncert_eval_method (): . Defaults to None
            s_uncert_evaluator (): . Defaults to None
        """
        params = {
            "n_uncert_assess_num": n_uncert_assess_num,
            "asym_expand_uncert": asym_expand_uncert,
            "asym_std_uncert": asym_std_uncert,
            "n_coverage_factor": n_coverage_factor,
            "n_expand_uncert_value": n_expand_uncert_value,
            "n_std_uncert_value": n_std_uncert_value,
            "n_uncert_lev_of_confid": n_uncert_lev_of_confid,
            "s_uncert_eval_method": s_uncert_eval_method,
            "s_uncert_evaluator": s_uncert_evaluator,
        }
        if id is not None:
            params["id"] = id
        self.prop_uncertainty.append(PropUncertainty(**params))
        return self.prop_uncertainty[-1]
