import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .eqvariable import EqVariable
from .eqproperty import EqProperty
from .eqconstant import EqConstant
from .eqconstraint import EqConstraint
from .eqparameter import EqParameter
from .eeqname import eEqName
from .covariance import Covariance


@forge_signature
class Equation(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_eq_name: Union[eEqName, str, None] = element(
        default=None, tag="eEqName", json_schema_extra=dict(xml="eEqName")
    )
    s_eq_name: Optional[str] = element(
        default=None, tag="sEqName", json_schema_extra=dict(xml="sEqName")
    )
    url_math_source: Optional[str] = element(
        default=None, tag="urlMathSource", json_schema_extra=dict(xml="urlMathSource")
    )
    covariance: List[Covariance] = element(
        default_factory=ListPlus,
        tag="Covariance",
        json_schema_extra=dict(multiple=True, xml="Covariance"),
    )
    eq_constant: List[EqConstant] = element(
        default_factory=ListPlus,
        tag="EqConstant",
        json_schema_extra=dict(multiple=True, xml="EqConstant"),
    )
    eq_constraint: List[EqConstraint] = element(
        default_factory=ListPlus,
        tag="EqConstraint",
        json_schema_extra=dict(multiple=True, xml="EqConstraint"),
    )
    eq_parameter: List[EqParameter] = element(
        default_factory=ListPlus,
        tag="EqParameter",
        json_schema_extra=dict(multiple=True, xml="EqParameter"),
    )
    eq_property: List[EqProperty] = element(
        default_factory=ListPlus,
        tag="EqProperty",
        json_schema_extra=dict(multiple=True, xml="EqProperty"),
    )
    eq_variable: List[EqVariable] = element(
        default_factory=ListPlus,
        tag="EqVariable",
        json_schema_extra=dict(multiple=True, xml="EqVariable"),
    )
    n_covariance_lev_of_confid: Optional[float] = element(
        default=None,
        tag="nCovarianceLevOfConfid",
        json_schema_extra=dict(xml="nCovarianceLevOfConfid"),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="7847845987ccfa50e8c08ada56669b59d1b97819"
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

    def add_to_covariance(
        self,
        n_covariance_value: Optional[float] = None,
        n_eq_par_number1: Optional[int] = None,
        n_eq_par_number2: Optional[int] = None,
        **kwargs
    ) -> Covariance:
        """
        This method adds an object of type 'Covariance' to attribute covariance

        Args:

            n_covariance_value (): . Defaults to None
            n_eq_par_number1 (): . Defaults to None
            n_eq_par_number2 (): . Defaults to None
        """
        params = {
            "n_covariance_value": n_covariance_value,
            "n_eq_par_number1": n_eq_par_number1,
            "n_eq_par_number2": n_eq_par_number2,
        }
        if id is not None:
            params["id"] = id
        self.covariance.append(Covariance(**params))
        return self.covariance[-1]

    def add_to_eq_constant(
        self,
        n_eq_constant_digits: Optional[int] = None,
        n_eq_constant_value: Optional[float] = None,
        s_eq_constant_symbol: Optional[str] = None,
        n_eq_constant_index: List[int] = ListPlus(),
        **kwargs
    ) -> EqConstant:
        """
        This method adds an object of type 'EqConstant' to attribute eq_constant

        Args:

            n_eq_constant_digits (): . Defaults to None
            n_eq_constant_value (): . Defaults to None
            s_eq_constant_symbol (): . Defaults to None
            n_eq_constant_index (): . Defaults to ListPlus()
        """
        params = {
            "n_eq_constant_digits": n_eq_constant_digits,
            "n_eq_constant_value": n_eq_constant_value,
            "s_eq_constant_symbol": s_eq_constant_symbol,
            "n_eq_constant_index": n_eq_constant_index,
        }
        if id is not None:
            params["id"] = id
        self.eq_constant.append(EqConstant(**params))
        return self.eq_constant[-1]

    def add_to_eq_constraint(
        self,
        n_constraint_number: Optional[int] = None,
        n_pure_or_mixture_data_number: Optional[int] = None,
        n_reaction_data_number: Optional[int] = None,
        s_eq_symbol: Optional[str] = None,
        n_eq_constraint_index: List[int] = ListPlus(),
        n_eq_constraint_range_max: Optional[float] = None,
        n_eq_constraint_range_min: Optional[float] = None,
        s_other_constraint_unit: Optional[str] = None,
        **kwargs
    ) -> EqConstraint:
        """
        This method adds an object of type 'EqConstraint' to attribute eq_constraint

        Args:

            n_constraint_number (): . Defaults to None
            n_pure_or_mixture_data_number (): . Defaults to None
            n_reaction_data_number (): . Defaults to None
            s_eq_symbol (): . Defaults to None
            n_eq_constraint_index (): . Defaults to ListPlus()
            n_eq_constraint_range_max (): . Defaults to None
            n_eq_constraint_range_min (): . Defaults to None
            s_other_constraint_unit (): . Defaults to None
        """
        params = {
            "n_constraint_number": n_constraint_number,
            "n_pure_or_mixture_data_number": n_pure_or_mixture_data_number,
            "n_reaction_data_number": n_reaction_data_number,
            "s_eq_symbol": s_eq_symbol,
            "n_eq_constraint_index": n_eq_constraint_index,
            "n_eq_constraint_range_max": n_eq_constraint_range_max,
            "n_eq_constraint_range_min": n_eq_constraint_range_min,
            "s_other_constraint_unit": s_other_constraint_unit,
        }
        if id is not None:
            params["id"] = id
        self.eq_constraint.append(EqConstraint(**params))
        return self.eq_constraint[-1]

    def add_to_eq_parameter(
        self,
        n_eq_par_digits: Optional[int] = None,
        n_eq_par_value: Optional[float] = None,
        s_eq_par_symbol: Optional[str] = None,
        n_eq_par_index: List[int] = ListPlus(),
        n_eq_par_number: Optional[int] = None,
        **kwargs
    ) -> EqParameter:
        """
        This method adds an object of type 'EqParameter' to attribute eq_parameter

        Args:

            n_eq_par_digits (): . Defaults to None
            n_eq_par_value (): . Defaults to None
            s_eq_par_symbol (): . Defaults to None
            n_eq_par_index (): . Defaults to ListPlus()
            n_eq_par_number (): . Defaults to None
        """
        params = {
            "n_eq_par_digits": n_eq_par_digits,
            "n_eq_par_value": n_eq_par_value,
            "s_eq_par_symbol": s_eq_par_symbol,
            "n_eq_par_index": n_eq_par_index,
            "n_eq_par_number": n_eq_par_number,
        }
        if id is not None:
            params["id"] = id
        self.eq_parameter.append(EqParameter(**params))
        return self.eq_parameter[-1]

    def add_to_eq_property(
        self,
        n_prop_number: Optional[int] = None,
        n_pure_or_mixture_data_number: Optional[int] = None,
        n_reaction_data_number: Optional[int] = None,
        s_eq_symbol: Optional[str] = None,
        n_eq_prop_index: List[int] = ListPlus(),
        n_eq_prop_range_max: Optional[float] = None,
        n_eq_prop_range_min: Optional[float] = None,
        s_other_prop_unit: Optional[str] = None,
        **kwargs
    ) -> EqProperty:
        """
        This method adds an object of type 'EqProperty' to attribute eq_property

        Args:

            n_prop_number (): . Defaults to None
            n_pure_or_mixture_data_number (): . Defaults to None
            n_reaction_data_number (): . Defaults to None
            s_eq_symbol (): . Defaults to None
            n_eq_prop_index (): . Defaults to ListPlus()
            n_eq_prop_range_max (): . Defaults to None
            n_eq_prop_range_min (): . Defaults to None
            s_other_prop_unit (): . Defaults to None
        """
        params = {
            "n_prop_number": n_prop_number,
            "n_pure_or_mixture_data_number": n_pure_or_mixture_data_number,
            "n_reaction_data_number": n_reaction_data_number,
            "s_eq_symbol": s_eq_symbol,
            "n_eq_prop_index": n_eq_prop_index,
            "n_eq_prop_range_max": n_eq_prop_range_max,
            "n_eq_prop_range_min": n_eq_prop_range_min,
            "s_other_prop_unit": s_other_prop_unit,
        }
        if id is not None:
            params["id"] = id
        self.eq_property.append(EqProperty(**params))
        return self.eq_property[-1]

    def add_to_eq_variable(
        self,
        n_pure_or_mixture_data_number: Optional[int] = None,
        n_reaction_data_number: Optional[int] = None,
        n_var_number: Optional[int] = None,
        s_eq_symbol: Optional[str] = None,
        n_eq_var_index: List[int] = ListPlus(),
        n_eq_var_range_max: Optional[float] = None,
        n_eq_var_range_min: Optional[float] = None,
        s_other_var_unit: Optional[str] = None,
        **kwargs
    ) -> EqVariable:
        """
        This method adds an object of type 'EqVariable' to attribute eq_variable

        Args:

            n_pure_or_mixture_data_number (): . Defaults to None
            n_reaction_data_number (): . Defaults to None
            n_var_number (): . Defaults to None
            s_eq_symbol (): . Defaults to None
            n_eq_var_index (): . Defaults to ListPlus()
            n_eq_var_range_max (): . Defaults to None
            n_eq_var_range_min (): . Defaults to None
            s_other_var_unit (): . Defaults to None
        """
        params = {
            "n_pure_or_mixture_data_number": n_pure_or_mixture_data_number,
            "n_reaction_data_number": n_reaction_data_number,
            "n_var_number": n_var_number,
            "s_eq_symbol": s_eq_symbol,
            "n_eq_var_index": n_eq_var_index,
            "n_eq_var_range_max": n_eq_var_range_max,
            "n_eq_var_range_min": n_eq_var_range_min,
            "s_other_var_unit": s_other_var_unit,
        }
        if id is not None:
            params["id"] = id
        self.eq_variable.append(EqVariable(**params))
        return self.eq_variable[-1]
