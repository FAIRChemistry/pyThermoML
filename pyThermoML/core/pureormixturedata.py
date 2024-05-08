import sdRDM

import pandas as pd
from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .refphaseid import RefPhaseID
from .propphaseid import PropPhaseID
from .variable import Variable
from .component import Component
from .covariance import Covariance
from .eqparameter import EqParameter
from .eeqname import eEqName
from .constrrepeatability import ConstrRepeatability
from .eqconstant import EqConstant
from .solvent import Solvent
from .propertyvalue import PropertyValue
from .varrepeatability import VarRepeatability
from .vardevicespec import VarDeviceSpec
from .eqvariable import EqVariable
from .regnum import RegNum
from .erefstatetype import eRefStateType
from .catalyst import Catalyst
from .constraint import Constraint
from .curvedev import CurveDev
from .estandardstate import eStandardState
from .auxiliarysubstance import AuxiliarySubstance
from .efunction import eFunction
from .numvalues import NumValues
from .constrdevicespec import ConstrDeviceSpec
from .variableid import VariableID
from .propuncertainty import PropUncertainty
from .propertymethodid import PropertyMethodID
from .equation import Equation
from .property import Property
from .varphaseid import VarPhaseID
from .varuncertainty import VarUncertainty
from .constraintid import ConstraintID
from .phaseid import PhaseID
from .propdevicespec import PropDeviceSpec
from .eqproperty import EqProperty
from .ecrystallatticetype import eCrystalLatticeType
from .eqconstraint import EqConstraint
from .variablevalue import VariableValue
from .construncertainty import ConstrUncertainty
from .epresentation import ePresentation
from .ephase import ePhase
from .constraintphaseid import ConstraintPhaseID
from .proprepeatability import PropRepeatability
from .combineduncertainty import CombinedUncertainty
from .eexppurpose import eExpPurpose


@forge_signature
class PureOrMixtureData(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    component: List[Component] = element(
        default_factory=ListPlus,
        tag="Component",
        json_schema_extra=dict(multiple=True, xml="Component"),
    )

    phase_id: List[PhaseID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=ListPlus,
        tag="PhaseID",
        json_schema_extra=dict(multiple=True, xml="PhaseID"),
    )
    property: List[Property] = element(
        default_factory=ListPlus,
        tag="Property",
        json_schema_extra=dict(multiple=True, xml="Property"),
    )
    auxiliary_substance: List[AuxiliarySubstance] = element(
        default_factory=ListPlus,
        tag="AuxiliarySubstance",
        json_schema_extra=dict(multiple=True, xml="AuxiliarySubstance"),
    )
    constraint: List[Constraint] = element(
        default_factory=ListPlus,
        tag="Constraint",
        json_schema_extra=dict(multiple=True, xml="Constraint"),
    )
    date_date_added: Optional[str] = element(
        default=None, tag="dateDateAdded", json_schema_extra=dict(xml="dateDateAdded")
    )

    e_exp_purpose: Union[eExpPurpose, str, None] = element(
        description="Purpose of measurement",
        default=None,
        tag="eExpPurpose",
        json_schema_extra=dict(xml="eExpPurpose"),
    )
    equation: List[Equation] = element(
        default_factory=ListPlus,
        tag="Equation",
        json_schema_extra=dict(multiple=True, xml="Equation"),
    )
    n_pure_or_mixture_data_number: Optional[int] = element(
        default=None,
        tag="nPureOrMixtureDataNumber",
        json_schema_extra=dict(xml="nPureOrMixtureDataNumber"),
    )
    num_values: List[NumValues] = element(
        default_factory=ListPlus,
        tag="NumValues",
        json_schema_extra=dict(multiple=True, xml="NumValues"),
    )
    s_compiler: Optional[str] = element(
        default=None, tag="sCompiler", json_schema_extra=dict(xml="sCompiler")
    )
    s_contributor: Optional[str] = element(
        default=None, tag="sContributor", json_schema_extra=dict(xml="sContributor")
    )
    variable: List[Variable] = element(
        default_factory=ListPlus,
        tag="Variable",
        json_schema_extra=dict(multiple=True, xml="Variable"),
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

    def add_to_component(
        self,
        n_amount: Optional[float] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        n_sample_nm: Optional[int] = None,
        **kwargs,
    ) -> Component:
        """
        This method adds an object of type 'Component' to attribute component

        Args:

            n_amount (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            n_sample_nm (): . Defaults to None
        """
        params = {
            "n_amount": n_amount,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "n_sample_nm": n_sample_nm,
        }
        if id is not None:
            params["id"] = id
        self.component.append(Component(**params))
        return self.component[-1]

    def add_to_phase_id(
        self,
        e_crystal_lattice_type: Union[eCrystalLatticeType, str, None] = None,
        e_phase: Union[ePhase, str, None] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        s_phase_description: Optional[str] = None,
        **kwargs,
    ) -> PhaseID:
        """
        This method adds an object of type 'PhaseID' to attribute phase_id

        Args:

            e_crystal_lattice_type (): . Defaults to None
            e_phase (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            s_phase_description (): . Defaults to None
        """
        params = {
            "e_crystal_lattice_type": e_crystal_lattice_type,
            "e_phase": e_phase,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "s_phase_description": s_phase_description,
        }
        if id is not None:
            params["id"] = id
        self.phase_id.append(PhaseID(**params))
        return self.phase_id[-1]

    def add_to_property(
        self,
        e_presentation: Union[ePresentation, str, None] = None,
        n_pressure_digits: Optional[int] = None,
        n_pressure_pa: Optional[float] = None,
        n_prop_number: Optional[int] = None,
        n_ref_pressure: Optional[float] = None,
        n_ref_pressure_digits: Optional[int] = None,
        n_ref_temp: Optional[float] = None,
        n_ref_temp_digits: Optional[int] = None,
        n_temperature_digits: Optional[int] = None,
        n_temperature_k: Optional[float] = None,
        property_method_id: Optional[PropertyMethodID] = None,
        catalyst: List[Catalyst] = ListPlus(),
        combined_uncertainty: List[CombinedUncertainty] = ListPlus(),
        curve_dev: List[CurveDev] = ListPlus(),
        e_ref_state_type: Union[eRefStateType, str, None] = None,
        e_standard_state: Union[eStandardState, str, None] = None,
        prop_device_spec: Optional[PropDeviceSpec] = None,
        prop_phase_id: List[PropPhaseID] = ListPlus(),
        prop_repeatability: Optional[PropRepeatability] = None,
        prop_uncertainty: List[PropUncertainty] = ListPlus(),
        ref_phase_id: Optional[RefPhaseID] = None,
        solvent: Optional[Solvent] = None,
        **kwargs,
    ) -> Property:
        """
        This method adds an object of type 'Property' to attribute property

        Args:

            e_presentation (): . Defaults to None
            n_pressure_digits (): . Defaults to None
            n_pressure_pa (): . Defaults to None
            n_prop_number (): . Defaults to None
            n_ref_pressure (): . Defaults to None
            n_ref_pressure_digits (): . Defaults to None
            n_ref_temp (): . Defaults to None
            n_ref_temp_digits (): . Defaults to None
            n_temperature_digits (): . Defaults to None
            n_temperature_k (): . Defaults to None
            property_method_id (): CASRN is necessary for mixtures only. Defaults to None
            catalyst (): . Defaults to ListPlus()
            combined_uncertainty (): . Defaults to ListPlus()
            curve_dev (): . Defaults to ListPlus()
            e_ref_state_type (): . Defaults to None
            e_standard_state (): . Defaults to None
            prop_device_spec (): . Defaults to None
            prop_phase_id (): CASRN is necessary for mixtures only. Defaults to ListPlus()
            prop_repeatability (): . Defaults to None
            prop_uncertainty (): . Defaults to ListPlus()
            ref_phase_id (): CASRN is necessary for mixtures only. Defaults to None
            solvent (): . Defaults to None
        """
        params = {
            "e_presentation": e_presentation,
            "n_pressure_digits": n_pressure_digits,
            "n_pressure_pa": n_pressure_pa,
            "n_prop_number": n_prop_number,
            "n_ref_pressure": n_ref_pressure,
            "n_ref_pressure_digits": n_ref_pressure_digits,
            "n_ref_temp": n_ref_temp,
            "n_ref_temp_digits": n_ref_temp_digits,
            "n_temperature_digits": n_temperature_digits,
            "n_temperature_k": n_temperature_k,
            "property_method_id": property_method_id,
            "catalyst": catalyst,
            "combined_uncertainty": combined_uncertainty,
            "curve_dev": curve_dev,
            "e_ref_state_type": e_ref_state_type,
            "e_standard_state": e_standard_state,
            "prop_device_spec": prop_device_spec,
            "prop_phase_id": prop_phase_id,
            "prop_repeatability": prop_repeatability,
            "prop_uncertainty": prop_uncertainty,
            "ref_phase_id": ref_phase_id,
            "solvent": solvent,
        }
        if id is not None:
            params["id"] = id
        self.property.append(Property(**params))
        return self.property[-1]

    def add_to_auxiliary_substance(
        self,
        e_function: Union[eFunction, str, None] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        s_function: Optional[str] = None,
        e_phase: Union[ePhase, str, None] = None,
        n_sample_nm: Optional[int] = None,
        **kwargs,
    ) -> AuxiliarySubstance:
        """
        This method adds an object of type 'AuxiliarySubstance' to attribute auxiliary_substance

        Args:

            e_function (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            s_function (): . Defaults to None
            e_phase (): . Defaults to None
            n_sample_nm (): . Defaults to None
        """
        params = {
            "e_function": e_function,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "s_function": s_function,
            "e_phase": e_phase,
            "n_sample_nm": n_sample_nm,
        }
        if id is not None:
            params["id"] = id
        self.auxiliary_substance.append(AuxiliarySubstance(**params))
        return self.auxiliary_substance[-1]

    def add_to_constraint(
        self,
        constraint_id: Optional[ConstraintID] = None,
        n_constr_digits: Optional[int] = None,
        n_constraint_value: Optional[float] = None,
        constr_device_spec: Optional[ConstrDeviceSpec] = None,
        constr_repeatability: Optional[ConstrRepeatability] = None,
        constr_uncertainty: List[ConstrUncertainty] = ListPlus(),
        constraint_phase_id: Optional[ConstraintPhaseID] = None,
        n_constraint_number: Optional[int] = None,
        solvent: Optional[Solvent] = None,
        **kwargs,
    ) -> Constraint:
        """
        This method adds an object of type 'Constraint' to attribute constraint

        Args:

            constraint_id (): CASRN is necessary for mixtures only. Defaults to None
            n_constr_digits (): . Defaults to None
            n_constraint_value (): . Defaults to None
            constr_device_spec (): . Defaults to None
            constr_repeatability (): . Defaults to None
            constr_uncertainty (): . Defaults to ListPlus()
            constraint_phase_id (): CASRN is necessary for mixtures only. Defaults to None
            n_constraint_number (): . Defaults to None
            solvent (): . Defaults to None
        """
        params = {
            "constraint_id": constraint_id,
            "n_constr_digits": n_constr_digits,
            "n_constraint_value": n_constraint_value,
            "constr_device_spec": constr_device_spec,
            "constr_repeatability": constr_repeatability,
            "constr_uncertainty": constr_uncertainty,
            "constraint_phase_id": constraint_phase_id,
            "n_constraint_number": n_constraint_number,
            "solvent": solvent,
        }
        if id is not None:
            params["id"] = id
        self.constraint.append(Constraint(**params))
        return self.constraint[-1]

    def add_to_equation(
        self,
        e_eq_name: Union[eEqName, str, None] = None,
        s_eq_name: Optional[str] = None,
        url_math_source: Optional[str] = None,
        covariance: List[Covariance] = ListPlus(),
        eq_constant: List[EqConstant] = ListPlus(),
        eq_constraint: List[EqConstraint] = ListPlus(),
        eq_parameter: List[EqParameter] = ListPlus(),
        eq_property: List[EqProperty] = ListPlus(),
        eq_variable: List[EqVariable] = ListPlus(),
        n_covariance_lev_of_confid: Optional[float] = None,
        **kwargs,
    ) -> Equation:
        """
        This method adds an object of type 'Equation' to attribute equation

        Args:

            e_eq_name (): . Defaults to None
            s_eq_name (): . Defaults to None
            url_math_source (): . Defaults to None
            covariance (): . Defaults to ListPlus()
            eq_constant (): . Defaults to ListPlus()
            eq_constraint (): . Defaults to ListPlus()
            eq_parameter (): . Defaults to ListPlus()
            eq_property (): . Defaults to ListPlus()
            eq_variable (): . Defaults to ListPlus()
            n_covariance_lev_of_confid (): . Defaults to None
        """
        params = {
            "e_eq_name": e_eq_name,
            "s_eq_name": s_eq_name,
            "url_math_source": url_math_source,
            "covariance": covariance,
            "eq_constant": eq_constant,
            "eq_constraint": eq_constraint,
            "eq_parameter": eq_parameter,
            "eq_property": eq_property,
            "eq_variable": eq_variable,
            "n_covariance_lev_of_confid": n_covariance_lev_of_confid,
        }
        if id is not None:
            params["id"] = id
        self.equation.append(Equation(**params))
        return self.equation[-1]

    def add_to_num_values(
        self,
        property_value: List[PropertyValue] = ListPlus(),
        variable_value: List[VariableValue] = ListPlus(),
        **kwargs,
    ) -> NumValues:
        """
        This method adds an object of type 'NumValues' to attribute num_values

        Args:

            property_value (): . Defaults to ListPlus()
            variable_value (): . Defaults to ListPlus()
        """
        params = {"property_value": property_value, "variable_value": variable_value}
        if id is not None:
            params["id"] = id
        self.num_values.append(NumValues(**params))
        return self.num_values[-1]

    def add_to_variable(
        self,
        n_var_number: Optional[int] = None,
        variable_id: Optional[VariableID] = None,
        solvent: Optional[Solvent] = None,
        var_device_spec: Optional[VarDeviceSpec] = None,
        var_phase_id: Optional[VarPhaseID] = None,
        var_repeatability: Optional[VarRepeatability] = None,
        var_uncertainty: List[VarUncertainty] = ListPlus(),
        **kwargs,
    ) -> Variable:
        """
        This method adds an object of type 'Variable' to attribute variable

        Args:

            n_var_number (): . Defaults to None
            variable_id (): CASRN is necessary for mixtures only. Defaults to None
            solvent (): . Defaults to None
            var_device_spec (): . Defaults to None
            var_phase_id (): CASRN is necessary for mixtures only. Defaults to None
            var_repeatability (): . Defaults to None
            var_uncertainty (): . Defaults to ListPlus()
        """
        params = {
            "n_var_number": n_var_number,
            "variable_id": variable_id,
            "solvent": solvent,
            "var_device_spec": var_device_spec,
            "var_phase_id": var_phase_id,
            "var_repeatability": var_repeatability,
            "var_uncertainty": var_uncertainty,
        }
        if id is not None:
            params["id"] = id
        self.variable.append(Variable(**params))
        return self.variable[-1]


def get_not_none(obj):
    non_none_attributes = {}
    for attr_name, attr_value in obj.__dict__.items():
        if attr_value is not None:
            non_none_attributes[attr_name] = attr_value
    return non_none_attributes


@forge_signature
class PureOrMixtureData(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    component: List[Component] = element(
        default_factory=ListPlus,
        tag="Component",
        json_schema_extra=dict(
            multiple=True,
            xml="Component",
        ),
    )

    phase_id: List[PhaseID] = element(
        description="CASRN is necessary for mixtures only",
        default_factory=ListPlus,
        tag="PhaseID",
        json_schema_extra=dict(
            multiple=True,
            xml="PhaseID",
        ),
    )

    property: List[Property] = element(
        default_factory=ListPlus,
        tag="Property",
        json_schema_extra=dict(
            multiple=True,
            xml="Property",
        ),
    )

    auxiliary_substance: List[AuxiliarySubstance] = element(
        default_factory=ListPlus,
        tag="AuxiliarySubstance",
        json_schema_extra=dict(
            multiple=True,
            xml="AuxiliarySubstance",
        ),
    )

    constraint: List[Constraint] = element(
        default_factory=ListPlus,
        tag="Constraint",
        json_schema_extra=dict(
            multiple=True,
            xml="Constraint",
        ),
    )

    date_date_added: Optional[str] = element(
        default=None,
        tag="dateDateAdded",
        json_schema_extra=dict(
            xml="dateDateAdded",
        ),
    )

    e_exp_purpose: Union[eExpPurpose, str, None] = element(
        description="Purpose of measurement",
        default=None,
        tag="eExpPurpose",
        json_schema_extra=dict(
            xml="eExpPurpose",
        ),
    )

    equation: List[Equation] = element(
        default_factory=ListPlus,
        tag="Equation",
        json_schema_extra=dict(
            multiple=True,
            xml="Equation",
        ),
    )

    n_pure_or_mixture_data_number: Optional[int] = element(
        default=None,
        tag="nPureOrMixtureDataNumber",
        json_schema_extra=dict(
            xml="nPureOrMixtureDataNumber",
        ),
    )

    num_values: List[NumValues] = element(
        default_factory=ListPlus,
        tag="NumValues",
        json_schema_extra=dict(
            multiple=True,
            xml="NumValues",
        ),
    )

    s_compiler: Optional[str] = element(
        default=None,
        tag="sCompiler",
        json_schema_extra=dict(
            xml="sCompiler",
        ),
    )

    s_contributor: Optional[str] = element(
        default=None,
        tag="sContributor",
        json_schema_extra=dict(
            xml="sContributor",
        ),
    )

    variable: List[Variable] = element(
        default_factory=ListPlus,
        tag="Variable",
        json_schema_extra=dict(
            multiple=True,
            xml="Variable",
        ),
    )

    _raw_xml_data: Dict = PrivateAttr(default_factory=dict)

    @model_validator(mode="after")
    def _parse_raw_xml_data(self):
        for attr, value in self:
            if isinstance(value, (ListPlus, list)) and all(
                isinstance(i, _Element) for i in value
            ):
                self._raw_xml_data[attr] = [elem2dict(i) for i in value]
            elif isinstance(value, _Element):
                self._raw_xml_data[attr] = elem2dict(value)

        return self

    def add_to_component(
        self,
        n_amount: Optional[float] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        n_sample_nm: Optional[int] = None,
        **kwargs,
    ) -> Component:
        """
        This method adds an object of type 'Component' to attribute component

        Args:

            n_amount (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            n_sample_nm (): . Defaults to None
        """

        params = {
            "n_amount": n_amount,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "n_sample_nm": n_sample_nm,
        }

        if id is not None:
            params["id"] = id

        self.component.append(Component(**params))

        return self.component[-1]

    def add_to_phase_id(
        self,
        e_crystal_lattice_type: Union[eCrystalLatticeType, str, None] = None,
        e_phase: Union[ePhase, str, None] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        s_phase_description: Optional[str] = None,
        **kwargs,
    ) -> PhaseID:
        """
        This method adds an object of type 'PhaseID' to attribute phase_id

        Args:

            e_crystal_lattice_type (): . Defaults to None
            e_phase (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            s_phase_description (): . Defaults to None
        """

        params = {
            "e_crystal_lattice_type": e_crystal_lattice_type,
            "e_phase": e_phase,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "s_phase_description": s_phase_description,
        }

        if id is not None:
            params["id"] = id

        self.phase_id.append(PhaseID(**params))

        return self.phase_id[-1]

    def add_to_property(
        self,
        e_presentation: Union[ePresentation, str, None] = None,
        n_pressure_digits: Optional[int] = None,
        n_pressure_pa: Optional[float] = None,
        n_prop_number: Optional[int] = None,
        n_ref_pressure: Optional[float] = None,
        n_ref_pressure_digits: Optional[int] = None,
        n_ref_temp: Optional[float] = None,
        n_ref_temp_digits: Optional[int] = None,
        n_temperature_digits: Optional[int] = None,
        n_temperature_k: Optional[float] = None,
        property_method_id: Optional[PropertyMethodID] = None,
        catalyst: List[Catalyst] = ListPlus(),
        combined_uncertainty: List[CombinedUncertainty] = ListPlus(),
        curve_dev: List[CurveDev] = ListPlus(),
        e_ref_state_type: Union[eRefStateType, str, None] = None,
        e_standard_state: Union[eStandardState, str, None] = None,
        prop_device_spec: Optional[PropDeviceSpec] = None,
        prop_phase_id: List[PropPhaseID] = ListPlus(),
        prop_repeatability: Optional[PropRepeatability] = None,
        prop_uncertainty: List[PropUncertainty] = ListPlus(),
        ref_phase_id: Optional[RefPhaseID] = None,
        solvent: Optional[Solvent] = None,
        **kwargs,
    ) -> Property:
        """
        This method adds an object of type 'Property' to attribute property

        Args:

            e_presentation (): . Defaults to None
            n_pressure_digits (): . Defaults to None
            n_pressure_pa (): . Defaults to None
            n_prop_number (): . Defaults to None
            n_ref_pressure (): . Defaults to None
            n_ref_pressure_digits (): . Defaults to None
            n_ref_temp (): . Defaults to None
            n_ref_temp_digits (): . Defaults to None
            n_temperature_digits (): . Defaults to None
            n_temperature_k (): . Defaults to None
            property_method_id (): CASRN is necessary for mixtures only. Defaults to None
            catalyst (): . Defaults to ListPlus()
            combined_uncertainty (): . Defaults to ListPlus()
            curve_dev (): . Defaults to ListPlus()
            e_ref_state_type (): . Defaults to None
            e_standard_state (): . Defaults to None
            prop_device_spec (): . Defaults to None
            prop_phase_id (): CASRN is necessary for mixtures only. Defaults to ListPlus()
            prop_repeatability (): . Defaults to None
            prop_uncertainty (): . Defaults to ListPlus()
            ref_phase_id (): CASRN is necessary for mixtures only. Defaults to None
            solvent (): . Defaults to None
        """

        params = {
            "e_presentation": e_presentation,
            "n_pressure_digits": n_pressure_digits,
            "n_pressure_pa": n_pressure_pa,
            "n_prop_number": n_prop_number,
            "n_ref_pressure": n_ref_pressure,
            "n_ref_pressure_digits": n_ref_pressure_digits,
            "n_ref_temp": n_ref_temp,
            "n_ref_temp_digits": n_ref_temp_digits,
            "n_temperature_digits": n_temperature_digits,
            "n_temperature_k": n_temperature_k,
            "property_method_id": property_method_id,
            "catalyst": catalyst,
            "combined_uncertainty": combined_uncertainty,
            "curve_dev": curve_dev,
            "e_ref_state_type": e_ref_state_type,
            "e_standard_state": e_standard_state,
            "prop_device_spec": prop_device_spec,
            "prop_phase_id": prop_phase_id,
            "prop_repeatability": prop_repeatability,
            "prop_uncertainty": prop_uncertainty,
            "ref_phase_id": ref_phase_id,
            "solvent": solvent,
        }

        if id is not None:
            params["id"] = id

        self.property.append(Property(**params))

        return self.property[-1]

    def add_to_auxiliary_substance(
        self,
        e_function: Union[eFunction, str, None] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        s_function: Optional[str] = None,
        e_phase: Union[ePhase, str, None] = None,
        n_sample_nm: Optional[int] = None,
        **kwargs,
    ) -> AuxiliarySubstance:
        """
        This method adds an object of type 'AuxiliarySubstance' to attribute auxiliary_substance

        Args:

            e_function (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            s_function (): . Defaults to None
            e_phase (): . Defaults to None
            n_sample_nm (): . Defaults to None
        """

        params = {
            "e_function": e_function,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "s_function": s_function,
            "e_phase": e_phase,
            "n_sample_nm": n_sample_nm,
        }

        if id is not None:
            params["id"] = id

        self.auxiliary_substance.append(AuxiliarySubstance(**params))

        return self.auxiliary_substance[-1]

    def add_to_constraint(
        self,
        constraint_id: Optional[ConstraintID] = None,
        n_constr_digits: Optional[int] = None,
        n_constraint_value: Optional[float] = None,
        constr_device_spec: Optional[ConstrDeviceSpec] = None,
        constr_repeatability: Optional[ConstrRepeatability] = None,
        constr_uncertainty: List[ConstrUncertainty] = ListPlus(),
        constraint_phase_id: Optional[ConstraintPhaseID] = None,
        n_constraint_number: Optional[int] = None,
        solvent: Optional[Solvent] = None,
        **kwargs,
    ) -> Constraint:
        """
        This method adds an object of type 'Constraint' to attribute constraint

        Args:

            constraint_id (): CASRN is necessary for mixtures only. Defaults to None
            n_constr_digits (): . Defaults to None
            n_constraint_value (): . Defaults to None
            constr_device_spec (): . Defaults to None
            constr_repeatability (): . Defaults to None
            constr_uncertainty (): . Defaults to ListPlus()
            constraint_phase_id (): CASRN is necessary for mixtures only. Defaults to None
            n_constraint_number (): . Defaults to None
            solvent (): . Defaults to None
        """

        params = {
            "constraint_id": constraint_id,
            "n_constr_digits": n_constr_digits,
            "n_constraint_value": n_constraint_value,
            "constr_device_spec": constr_device_spec,
            "constr_repeatability": constr_repeatability,
            "constr_uncertainty": constr_uncertainty,
            "constraint_phase_id": constraint_phase_id,
            "n_constraint_number": n_constraint_number,
            "solvent": solvent,
        }

        if id is not None:
            params["id"] = id

        self.constraint.append(Constraint(**params))

        return self.constraint[-1]

    def add_to_equation(
        self,
        e_eq_name: Union[eEqName, str, None] = None,
        s_eq_name: Optional[str] = None,
        url_math_source: Optional[str] = None,
        covariance: List[Covariance] = ListPlus(),
        eq_constant: List[EqConstant] = ListPlus(),
        eq_constraint: List[EqConstraint] = ListPlus(),
        eq_parameter: List[EqParameter] = ListPlus(),
        eq_property: List[EqProperty] = ListPlus(),
        eq_variable: List[EqVariable] = ListPlus(),
        n_covariance_lev_of_confid: Optional[float] = None,
        **kwargs,
    ) -> Equation:
        """
        This method adds an object of type 'Equation' to attribute equation

        Args:

            e_eq_name (): . Defaults to None
            s_eq_name (): . Defaults to None
            url_math_source (): . Defaults to None
            covariance (): . Defaults to ListPlus()
            eq_constant (): . Defaults to ListPlus()
            eq_constraint (): . Defaults to ListPlus()
            eq_parameter (): . Defaults to ListPlus()
            eq_property (): . Defaults to ListPlus()
            eq_variable (): . Defaults to ListPlus()
            n_covariance_lev_of_confid (): . Defaults to None
        """

        params = {
            "e_eq_name": e_eq_name,
            "s_eq_name": s_eq_name,
            "url_math_source": url_math_source,
            "covariance": covariance,
            "eq_constant": eq_constant,
            "eq_constraint": eq_constraint,
            "eq_parameter": eq_parameter,
            "eq_property": eq_property,
            "eq_variable": eq_variable,
            "n_covariance_lev_of_confid": n_covariance_lev_of_confid,
        }

        if id is not None:
            params["id"] = id

        self.equation.append(Equation(**params))

        return self.equation[-1]

    def add_to_num_values(
        self,
        property_value: List[PropertyValue] = ListPlus(),
        variable_value: List[VariableValue] = ListPlus(),
        **kwargs,
    ) -> NumValues:
        """
        This method adds an object of type 'NumValues' to attribute num_values

        Args:

            property_value (): . Defaults to ListPlus()
            variable_value (): . Defaults to ListPlus()
        """

        params = {
            "property_value": property_value,
            "variable_value": variable_value,
        }

        if id is not None:
            params["id"] = id

        self.num_values.append(NumValues(**params))

        return self.num_values[-1]

    def add_to_variable(
        self,
        n_var_number: Optional[int] = None,
        variable_id: Optional[VariableID] = None,
        solvent: Optional[Solvent] = None,
        var_device_spec: Optional[VarDeviceSpec] = None,
        var_phase_id: Optional[VarPhaseID] = None,
        var_repeatability: Optional[VarRepeatability] = None,
        var_uncertainty: List[VarUncertainty] = ListPlus(),
        **kwargs,
    ) -> Variable:
        """
        This method adds an object of type 'Variable' to attribute variable

        Args:

            n_var_number (): . Defaults to None
            variable_id (): CASRN is necessary for mixtures only. Defaults to None
            solvent (): . Defaults to None
            var_device_spec (): . Defaults to None
            var_phase_id (): CASRN is necessary for mixtures only. Defaults to None
            var_repeatability (): . Defaults to None
            var_uncertainty (): . Defaults to ListPlus()
        """

        params = {
            "n_var_number": n_var_number,
            "variable_id": variable_id,
            "solvent": solvent,
            "var_device_spec": var_device_spec,
            "var_phase_id": var_phase_id,
            "var_repeatability": var_repeatability,
            "var_uncertainty": var_uncertainty,
        }

        if id is not None:
            params["id"] = id

        self.variable.append(Variable(**params))

        return self.variable[-1]

    def get_composition(self, identifier: RegNum, id_dict: Dict[int, str]):
        """
        This function retrieves the composition value from a PureOrMixtureData object based on a specified RegNum identifier.

        Parameters:
            identifier (RegNum): The RegNum identifier for the desired composition.
            id_dict (Dict[int,str]): Dict matching n_org_number and the name of the compounds.

        Returns:
            float: The composition value.

        Raises:
            KeyError: If the PureOrMixtureData object does not contain a composition constraint for the specified species.

        """
        composition_flag = False
        composition = None
        constraint_ids = []
        for const in self.constraint:
            # Check if there is a composition constraint available
            if const.constraint_id.constraint_type.e_component_composition:
                composition_flag = True
                constraint_ids.append(const.constraint_id.reg_num.n_org_num)

                if const.constraint_id.reg_num == identifier:
                    composition = const.n_constraint_value
                    break

        # If pure entry without a constraint explicitly specifing it, composition is 1.0
        if not composition_flag and len(self.component) == 1:
            if self.component[0].reg_num == identifier:
                composition = 1.0

        if composition == None:
            if composition_flag:
                err_msg = (
                    "Pure or mixture data do not contain a composition constraint for"
                    f" the specified species: {id_dict[identifier.n_org_num]}."
                )
                err_msg += (
                    " Valid species are:"
                    f" '{', '.join( [ id_dict[c_id] for c_id in constraint_ids ] )}'."
                )
                raise KeyError(err_msg)
            else:
                raise KeyError("No composition constraint presented at all!")

        return composition

    def get_property(self):
        """
        This function takes a PureOrMixtureData object as input and extracts the property values and their corresponding uncertainties from the num_values attribute.
        It then returns a pandas DataFrame with two columns: "mean" and "95_confidence".

        Returns:
            pandas.DataFrame: A DataFrame containing the extracted property values and uncertainties.

        Example:
            self = PureOrMixtureData(...)
            df = get_property(self)
            print(df)

            Output:
                mean  95_confidence
            0   10.0           0.05
            1   20.0           0.10
            2   30.0           0.15
            ...
        """
        properties = []
        for num_value in self.num_values:
            properties.append([
                num_value.property_value[0].n_prop_value,
                num_value.property_value[0]
                .combined_uncertainty[0]
                .n_comb_expand_uncert_value,
            ])

        return pd.DataFrame(properties, columns=["mean", "95_confidence"])

    def property_name(self):
        property_dict = {
            "component_identifier": self.property[0].property_method_id.reg_num
        }
        for _, prop_group in self.property[0].property_method_id.property_group:
            if prop_group.e_prop_name:
                property_dict["type"] = prop_group.e_prop_name
                break
        return property_dict

    def property_exists(self, prop_name: str, prop_identifier: RegNum = RegNum()):
        """
        Check if a specific property exists in a PureOrMixtureData object.

        Parameters:
            prop_name (str): The name of the property to check for. This can also be a substring of the property.
            prop_identifier (RegNum, optional): Component identifier for the property. Defaults to RegNum().
        Returns:
            bool: True if the property exists, False otherwise.
        """

        property_dict = self.property_name()

        flag_property = (
            property_dict["component_identifier"] == prop_identifier
            and prop_name in property_dict["type"]
        )

        return flag_property

    def get_constraints(self):
        constraints = []
        for const in self.constraint:
            constraint = {
                "type": list(
                    get_not_none(const.constraint_id.constraint_type).values()
                )[0],
                "component_identifier": const.constraint_id.reg_num,
                "phase": const.constraint_phase_id.e_constraint_phase,
                "value": const.n_constraint_value,
            }
            constraints.append(constraint)

        return constraints

    def get_variable(self, var_name: str):
        """
        Get the values of a specified variable from a PureOrMixtureData object.

        Parameters:
            var_name (str): The name of the variable to retrieve.

        Returns:
            list: A list of values corresponding to the specified variable.

        Raises:
            KeyError: If the PureOrMixtureData object does not contain the specified variable.

        """
        variable = []
        no = 0
        for var in self.variable:
            if any(
                var_name in vname
                for vname in var.variable_id.variable_type.__dict__.values()
                if vname
            ):
                no = var.n_var_number
                break

        if not no:
            raise KeyError(
                f"Pure of mixture data do not contain specified variable: '{var_name}'."
            )

        for num_value in self.num_values:
            if num_value.variable_value[0].n_var_number == no:
                variable.append(num_value.variable_value[0].n_var_value)

        return variable

    def get_variables(self):
        variables = []
        for var in self.variable:
            variable = {
                "type": list(get_not_none(var.variable_id.variable_type).values())[0],
                "component_identifier": var.variable_id.reg_num,
                "phase": var.var_phase_id.e_var_phase,
            }
            variable["values"] = self.get_variable(variable["type"])
            variables.append(variable)

        return variables
