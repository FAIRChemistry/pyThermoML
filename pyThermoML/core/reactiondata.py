import sdRDM

from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .refphaseid import RefPhaseID
from .constraintphaseid import ConstraintPhaseID
from .participant import Participant
from .property import Property
from .propdevicespec import PropDeviceSpec
from .variableid import VariableID
from .eqconstraint import EqConstraint
from .regnum import RegNum
from .eeqname import eEqName
from .constraintid import ConstraintID
from .eqproperty import EqProperty
from .epresentation import ePresentation
from .efunction import eFunction
from .combineduncertainty import CombinedUncertainty
from .ereactionformalism import eReactionFormalism
from .estandardstate import eStandardState
from .ecompositionrepresentation import eCompositionRepresentation
from .proprepeatability import PropRepeatability
from .numvalues import NumValues
from .construncertainty import ConstrUncertainty
from .eqvariable import EqVariable
from .solvent import Solvent
from .eexppurpose import eExpPurpose
from .equation import Equation
from .constrrepeatability import ConstrRepeatability
from .constraint import Constraint
from .ecrystallatticetype import eCrystalLatticeType
from .propertyvalue import PropertyValue
from .propuncertainty import PropUncertainty
from .erefstatetype import eRefStateType
from .catalyst import Catalyst
from .variable import Variable
from .auxiliarysubstance import AuxiliarySubstance
from .varrepeatability import VarRepeatability
from .vardevicespec import VarDeviceSpec
from .constrdevicespec import ConstrDeviceSpec
from .eqparameter import EqParameter
from .varuncertainty import VarUncertainty
from .covariance import Covariance
from .propertymethodid import PropertyMethodID
from .curvedev import CurveDev
from .ephase import ePhase
from .propphaseid import PropPhaseID
from .ereactiontype import eReactionType
from .variablevalue import VariableValue
from .eqconstant import EqConstant
from .varphaseid import VarPhaseID


@forge_signature
class ReactionData(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_reaction_type: Union[eReactionType, str, None] = element(
        default=None, tag="eReactionType", json_schema_extra=dict(xml="eReactionType")
    )
    participant: List[Participant] = element(
        default_factory=ListPlus,
        tag="Participant",
        json_schema_extra=dict(multiple=True, xml="Participant"),
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
    e_reaction_formalism: Union[eReactionFormalism, str, None] = element(
        default=None,
        tag="eReactionFormalism",
        json_schema_extra=dict(xml="eReactionFormalism"),
    )
    equation: List[Equation] = element(
        default_factory=ListPlus,
        tag="Equation",
        json_schema_extra=dict(multiple=True, xml="Equation"),
    )
    n_electron_number: Optional[int] = element(
        default=None,
        tag="nElectronNumber",
        json_schema_extra=dict(xml="nElectronNumber"),
    )
    n_reaction_data_number: Optional[int] = element(
        default=None,
        tag="nReactionDataNumber",
        json_schema_extra=dict(xml="nReactionDataNumber"),
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
    solvent: List[Solvent] = element(
        default_factory=ListPlus,
        tag="Solvent",
        json_schema_extra=dict(multiple=True, xml="Solvent"),
    )
    variable: List[Variable] = element(
        default_factory=ListPlus,
        tag="Variable",
        json_schema_extra=dict(multiple=True, xml="Variable"),
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

    def add_to_participant(
        self,
        e_crystal_lattice_type: Union[eCrystalLatticeType, str, None] = None,
        e_phase: Union[ePhase, str, None] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        s_phase_description: Optional[str] = None,
        e_composition_representation: Union[
            eCompositionRepresentation, str, None
        ] = None,
        e_standard_state: Union[eStandardState, str, None] = None,
        n_numerical_composition: Optional[float] = None,
        n_sample_nm: Optional[int] = None,
        n_stoichiometric_coef: Optional[float] = None,
        **kwargs
    ) -> Participant:
        """
        This method adds an object of type 'Participant' to attribute participant

        Args:

            e_crystal_lattice_type (): . Defaults to None
            e_phase (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
            s_phase_description (): . Defaults to None
            e_composition_representation (): . Defaults to None
            e_standard_state (): . Defaults to None
            n_numerical_composition (): . Defaults to None
            n_sample_nm (): . Defaults to None
            n_stoichiometric_coef (): . Defaults to None
        """
        params = {
            "e_crystal_lattice_type": e_crystal_lattice_type,
            "e_phase": e_phase,
            "n_comp_index": n_comp_index,
            "reg_num": reg_num,
            "s_phase_description": s_phase_description,
            "e_composition_representation": e_composition_representation,
            "e_standard_state": e_standard_state,
            "n_numerical_composition": n_numerical_composition,
            "n_sample_nm": n_sample_nm,
            "n_stoichiometric_coef": n_stoichiometric_coef,
        }
        if id is not None:
            params["id"] = id
        self.participant.append(Participant(**params))
        return self.participant[-1]

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
        **kwargs
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
        **kwargs
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
        **kwargs
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
        **kwargs
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
        **kwargs
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

    def add_to_solvent(
        self,
        e_phase: Union[ePhase, str, None] = None,
        n_comp_index: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        **kwargs
    ) -> Solvent:
        """
        This method adds an object of type 'Solvent' to attribute solvent

        Args:

            e_phase (): . Defaults to None
            n_comp_index (): . Defaults to None
            reg_num (): . Defaults to None
        """
        params = {"e_phase": e_phase, "n_comp_index": n_comp_index, "reg_num": reg_num}
        if id is not None:
            params["id"] = id
        self.solvent.append(Solvent(**params))
        return self.solvent[-1]

    def add_to_variable(
        self,
        n_var_number: Optional[int] = None,
        variable_id: Optional[VariableID] = None,
        solvent: Optional[Solvent] = None,
        var_device_spec: Optional[VarDeviceSpec] = None,
        var_phase_id: Optional[VarPhaseID] = None,
        var_repeatability: Optional[VarRepeatability] = None,
        var_uncertainty: List[VarUncertainty] = ListPlus(),
        **kwargs
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
