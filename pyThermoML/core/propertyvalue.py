import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .curvedev import CurveDev
from .combineduncertainty import CombinedUncertainty
from .asymcombstduncert import AsymCombStdUncert
from .asymcombexpanduncert import AsymCombExpandUncert
from .proprepeatability import PropRepeatability
from .asymexpanduncert import AsymExpandUncert
from .propuncertainty import PropUncertainty
from .ecombuncertevalmethod import eCombUncertEvalMethod
from .asymstduncert import AsymStdUncert
from .proplimit import PropLimit


@forge_signature
class PropertyValue(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    n_prop_digits: Optional[int] = element(
        default=None, tag="nPropDigits", json_schema_extra=dict(xml="nPropDigits")
    )
    n_prop_number: Optional[int] = element(
        default=None, tag="nPropNumber", json_schema_extra=dict(xml="nPropNumber")
    )
    n_prop_value: Optional[float] = element(
        default=None, tag="nPropValue", json_schema_extra=dict(xml="nPropValue")
    )
    prop_limit: Optional[PropLimit] = element(
        default_factory=PropLimit,
        tag="PropLimit",
        json_schema_extra=dict(xml="PropLimit"),
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
    n_prop_device_spec_value: Optional[float] = element(
        default=None,
        tag="nPropDeviceSpecValue",
        json_schema_extra=dict(xml="nPropDeviceSpecValue"),
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
