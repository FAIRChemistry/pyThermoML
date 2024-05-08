```mermaid
classDiagram
    DataReport *-- Version
    DataReport *-- Citation
    DataReport *-- Compound
    DataReport *-- PureOrMixtureData
    DataReport *-- ReactionData
    Citation *-- eType
    Citation *-- eSourceType
    Citation *-- eLanguage
    Citation *-- TRCRefID
    Citation *-- Book
    Citation *-- Journal
    Citation *-- Thesis
    Compound *-- eSpeciationState
    Compound *-- RegNum
    Compound *-- SOrgID
    Compound *-- Polymer
    Compound *-- Ion
    Compound *-- Biomaterial
    Compound *-- MulticomponentSubstance
    Compound *-- Sample
    MulticomponentSubstance *-- Component
    Component *-- RegNum
    Sample *-- eSource
    Sample *-- eStatus
    Sample *-- Purity
    Sample *-- ComponentSample
    Purity *-- ePurifMethod
    Purity *-- eAnalMeth
    ComponentSample *-- RegNum
    PureOrMixtureData *-- eExpPurpose
    PureOrMixtureData *-- Component
    PureOrMixtureData *-- AuxiliarySubstance
    PureOrMixtureData *-- Property
    PureOrMixtureData *-- PhaseID
    PureOrMixtureData *-- Constraint
    PureOrMixtureData *-- Variable
    PureOrMixtureData *-- NumValues
    PureOrMixtureData *-- Equation
    AuxiliarySubstance *-- eFunction
    AuxiliarySubstance *-- ePhase
    AuxiliarySubstance *-- RegNum
    Property *-- ePresentation
    Property *-- eRefStateType
    Property *-- eStandardState
    Property *-- PropertyMethodID
    Property *-- PropPhaseID
    Property *-- RefPhaseID
    Property *-- Solvent
    Property *-- CombinedUncertainty
    Property *-- PropUncertainty
    Property *-- PropRepeatability
    Property *-- PropDeviceSpec
    Property *-- CurveDev
    Property *-- Catalyst
    PropertyMethodID *-- RegNum
    PropertyMethodID *-- PropertyGroup
    PropertyGroup *-- Criticals
    PropertyGroup *-- VaporPBoilingTAzeotropTandP
    PropertyGroup *-- PhaseTransition
    PropertyGroup *-- CompositionAtPhaseEquilibrium
    PropertyGroup *-- ActivityFugacityOsmoticProp
    PropertyGroup *-- VolumetricProp
    PropertyGroup *-- HeatCapacityAndDerivedProp
    PropertyGroup *-- ExcessPartialApparentEnergyProp
    PropertyGroup *-- TransportProp
    PropertyGroup *-- RefractionSurfaceTensionSoundSpeed
    PropertyGroup *-- BioProperties
    PropertyGroup *-- ReactionStateChangeProp
    PropertyGroup *-- ReactionEquilibriumProp
    Criticals *-- ePropName
    Criticals *-- eMethodName
    Criticals *-- CriticalEvaluation
    Criticals *-- Prediction
    CriticalEvaluation *-- SingleProp
    CriticalEvaluation *-- MultiProp
    CriticalEvaluation *-- EquationOfState
    SingleProp *-- EvalSinglePropRef
    EvalSinglePropRef *-- eType
    EvalSinglePropRef *-- eSourceType
    EvalSinglePropRef *-- eLanguage
    EvalSinglePropRef *-- TRCRefID
    EvalSinglePropRef *-- Book
    EvalSinglePropRef *-- Journal
    EvalSinglePropRef *-- Thesis
    MultiProp *-- EvalMultiPropRef
    EvalMultiPropRef *-- eType
    EvalMultiPropRef *-- eSourceType
    EvalMultiPropRef *-- eLanguage
    EvalMultiPropRef *-- TRCRefID
    EvalMultiPropRef *-- Book
    EvalMultiPropRef *-- Journal
    EvalMultiPropRef *-- Thesis
    EquationOfState *-- EvalEOSRef
    EvalEOSRef *-- eType
    EvalEOSRef *-- eSourceType
    EvalEOSRef *-- eLanguage
    EvalEOSRef *-- TRCRefID
    EvalEOSRef *-- Book
    EvalEOSRef *-- Journal
    EvalEOSRef *-- Thesis
    Prediction *-- ePredictionType
    Prediction *-- PredictionMethodRef
    PredictionMethodRef *-- eType
    PredictionMethodRef *-- eSourceType
    PredictionMethodRef *-- eLanguage
    PredictionMethodRef *-- TRCRefID
    PredictionMethodRef *-- Book
    PredictionMethodRef *-- Journal
    PredictionMethodRef *-- Thesis
    VaporPBoilingTAzeotropTandP *-- ePropName
    VaporPBoilingTAzeotropTandP *-- eMethodName
    VaporPBoilingTAzeotropTandP *-- CriticalEvaluation
    VaporPBoilingTAzeotropTandP *-- Prediction
    PhaseTransition *-- ePropName
    PhaseTransition *-- eMethodName
    PhaseTransition *-- CriticalEvaluation
    PhaseTransition *-- Prediction
    CompositionAtPhaseEquilibrium *-- ePropName
    CompositionAtPhaseEquilibrium *-- eMethodName
    CompositionAtPhaseEquilibrium *-- CriticalEvaluation
    CompositionAtPhaseEquilibrium *-- Prediction
    ActivityFugacityOsmoticProp *-- ePropName
    ActivityFugacityOsmoticProp *-- eMethodName
    ActivityFugacityOsmoticProp *-- CriticalEvaluation
    ActivityFugacityOsmoticProp *-- Prediction
    VolumetricProp *-- ePropName
    VolumetricProp *-- eMethodName
    VolumetricProp *-- CriticalEvaluation
    VolumetricProp *-- Prediction
    HeatCapacityAndDerivedProp *-- ePropName
    HeatCapacityAndDerivedProp *-- eMethodName
    HeatCapacityAndDerivedProp *-- CriticalEvaluation
    HeatCapacityAndDerivedProp *-- Prediction
    ExcessPartialApparentEnergyProp *-- ePropName
    ExcessPartialApparentEnergyProp *-- eMethodName
    ExcessPartialApparentEnergyProp *-- CriticalEvaluation
    ExcessPartialApparentEnergyProp *-- Prediction
    TransportProp *-- ePropName
    TransportProp *-- eMethodName
    TransportProp *-- CriticalEvaluation
    TransportProp *-- Prediction
    RefractionSurfaceTensionSoundSpeed *-- ePropName
    RefractionSurfaceTensionSoundSpeed *-- eMethodName
    RefractionSurfaceTensionSoundSpeed *-- CriticalEvaluation
    RefractionSurfaceTensionSoundSpeed *-- Prediction
    BioProperties *-- ePropName
    BioProperties *-- eMethodName
    BioProperties *-- CriticalEvaluation
    BioProperties *-- Prediction
    PropPhaseID *-- ePropPhase
    PropPhaseID *-- eCrystalLatticeType
    PropPhaseID *-- eBioState
    PropPhaseID *-- RegNum
    RefPhaseID *-- eCrystalLatticeType
    RefPhaseID *-- eRefPhase
    RefPhaseID *-- RegNum
    Solvent *-- ePhase
    Solvent *-- RegNum
    CombinedUncertainty *-- eCombUncertEvalMethod
    CombinedUncertainty *-- AsymCombStdUncert
    CombinedUncertainty *-- AsymCombExpandUncert
    PropUncertainty *-- AsymStdUncert
    PropUncertainty *-- AsymExpandUncert
    PropRepeatability *-- eRepeatMethod
    PropDeviceSpec *-- eDeviceSpecMethod
    PhaseID *-- eCrystalLatticeType
    PhaseID *-- ePhase
    PhaseID *-- RegNum
    Constraint *-- Solvent
    Constraint *-- ConstraintID
    Constraint *-- ConstraintPhaseID
    Constraint *-- ConstrUncertainty
    Constraint *-- ConstrRepeatability
    Constraint *-- ConstrDeviceSpec
    ConstraintID *-- RegNum
    ConstraintID *-- ConstraintType
    ConstraintType *-- eTemperature
    ConstraintType *-- ePressure
    ConstraintType *-- eComponentComposition
    ConstraintType *-- eSolventComposition
    ConstraintType *-- eMiscellaneous
    ConstraintType *-- eBioVariables
    ConstraintType *-- eParticipantAmount
    ConstraintPhaseID *-- eCrystalLatticeType
    ConstraintPhaseID *-- eConstraintPhase
    ConstraintPhaseID *-- RegNum
    ConstrRepeatability *-- eRepeatMethod
    ConstrDeviceSpec *-- eDeviceSpecMethod
    Variable *-- Solvent
    Variable *-- VariableID
    Variable *-- VarPhaseID
    Variable *-- VarUncertainty
    Variable *-- VarRepeatability
    Variable *-- VarDeviceSpec
    VariableID *-- RegNum
    VariableID *-- VariableType
    VariableType *-- eTemperature
    VariableType *-- ePressure
    VariableType *-- eComponentComposition
    VariableType *-- eSolventComposition
    VariableType *-- eMiscellaneous
    VariableType *-- eBioVariables
    VariableType *-- eParticipantAmount
    VarPhaseID *-- eCrystalLatticeType
    VarPhaseID *-- eVarPhase
    VarPhaseID *-- RegNum
    VarRepeatability *-- eRepeatMethod
    VarDeviceSpec *-- eDeviceSpecMethod
    NumValues *-- VariableValue
    NumValues *-- PropertyValue
    VariableValue *-- VarUncertainty
    VariableValue *-- VarRepeatability
    PropertyValue *-- CombinedUncertainty
    PropertyValue *-- PropUncertainty
    PropertyValue *-- PropRepeatability
    PropertyValue *-- CurveDev
    PropertyValue *-- PropLimit
    Equation *-- eEqName
    Equation *-- EqProperty
    Equation *-- EqConstraint
    Equation *-- EqVariable
    Equation *-- EqParameter
    Equation *-- EqConstant
    Equation *-- Covariance
    ReactionData *-- eExpPurpose
    ReactionData *-- eReactionFormalism
    ReactionData *-- eReactionType
    ReactionData *-- AuxiliarySubstance
    ReactionData *-- Property
    ReactionData *-- Solvent
    ReactionData *-- Constraint
    ReactionData *-- Variable
    ReactionData *-- NumValues
    ReactionData *-- Equation
    ReactionData *-- Participant
    Participant *-- eCrystalLatticeType
    Participant *-- eStandardState
    Participant *-- ePhase
    Participant *-- eCompositionRepresentation
    Participant *-- RegNum
    ReactionStateChangeProp *-- ePropName
    ReactionStateChangeProp *-- eMethodName
    ReactionStateChangeProp *-- CriticalEvaluation
    ReactionStateChangeProp *-- Prediction
    ReactionEquilibriumProp *-- ePropName
    ReactionEquilibriumProp *-- eMethodName
    ReactionEquilibriumProp *-- CriticalEvaluation
    ReactionEquilibriumProp *-- Prediction
    Catalyst *-- ePhase
    Catalyst *-- RegNum
    
    class DataReport {
        +Citation citation
        +Version version
        +Compound[0..*] compound
        +PureOrMixtureData[0..*] pure_or_mixture_data
        +ReactionData[0..*] reaction_data
    }
    
    class Version {
        +integer n_version_major
        +integer n_version_minor
    }
    
    class Citation {
        +Book book
        +Journal journal
        +Thesis thesis
        +string date_cit
        +eLanguage, string e_language
        +eSourceType, string e_source_type
        +eType, string e_type
        +string s_abstract
        +string[0..*] s_author
        +string s_cas_cit
        +string s_document_origin
        +string s_doi
        +string s_id_num
        +string[0..*] s_keyword
        +string s_location
        +string s_page
        +string s_pub_name
        +string s_title
        +string s_vol
        +TRCRefID trc_ref_id
        +string url_cit
        +string yr_pub_yr
    }
    
    class TRCRefID {
        +integer n_authorn
        +string s_author1
        +string s_author2
        +integer yr_yr_pub
    }
    
    class Book {
        +string s_chapter
        +string s_edition
        +string[0..*] s_editor
        +string s_isbn
        +string s_publisher
    }
    
    class Journal {
        +string s_coden
        +string s_issn
        +string s_issue
    }
    
    class Thesis {
        +string s_deg
        +string s_deg_inst
        +string s_umi_pub_num
    }
    
    class Compound {
        +Biomaterial biomaterial
        +Ion ion
        +MulticomponentSubstance multicomponent_substance
        +Polymer polymer
        +eSpeciationState, string e_speciation_state
        +integer n_comp_index
        +integer n_pub_chem_id
        +RegNum reg_num
        +string s_cas_name
        +string[0..*] s_common_name
        +string s_formula_molec
        +string s_iupac_name
        +SOrgID[0..*] s_org_id
        +string[0..*] s_smiles
        +string s_standard_in_ch_i
        +string s_standard_in_ch_i_key
        +Sample[0..*] sample
    }
    
    class RegNum {
        +integer n_org_num
        +integer n_casr_num
        +string s_organization
    }
    
    class SOrgID {
        +string s_org_identifier
        +string s_organization
    }
    
    class Polymer {
        +float n_deg_of_polymerization_dispersity
        +float n_mass_avg_mol_mass
        +float n_molar_mass_dispersity
        +float n_number_avg_mol_mass
        +float n_peak_avg_mol_mass
        +float n_viscosity_avg_mol_mass
        +float n_z_avg_mol_mass
    }
    
    class Ion {
        +integer n_charge
    }
    
    class Biomaterial {
        +string s_ec_number
        +string s_pdb_identifier
    }
    
    class MulticomponentSubstance {
        +Component[0..*] component
        +string composition_basis
        +string type
    }
    
    class Component {
        +float n_amount
        +integer n_comp_index
        +RegNum reg_num
        +integer n_sample_nm
    }
    
    class Sample {
        +integer n_sample_nm
        +ComponentSample[0..*] component_sample
        +eSource, string e_source
        +eStatus, string e_status
        +Purity[0..*] purity
    }
    
    class Purity {
        +float n_halide_mass_per_cent
        +integer n_halide_mass_per_cent_digits
        +float n_halide_mol_per_cent
        +integer n_halide_mol_per_cent_digits
        +float n_purity_mass
        +integer n_purity_mass_digits
        +float n_purity_mol
        +integer n_purity_mol_digits
        +float n_purity_vol
        +integer n_purity_vol_digits
        +integer n_step
        +float n_unknown_per_cent
        +integer n_unknown_per_cent_digits
        +float n_water_mass_per_cent
        +integer n_water_mass_per_cent_digits
        +float n_water_mol_per_cent
        +integer n_water_mol_per_cent_digits
        +eAnalMeth, string[0..*] e_anal_meth
        +ePurifMethod, string[0..*] e_purif_method
        +string[0..*] s_anal_meth
        +string[0..*] s_purif_method
    }
    
    class ComponentSample {
        +integer n_comp_index
        +integer n_sample_nm
        +RegNum reg_num
    }
    
    class PureOrMixtureData {
        +Component[0..*] component
        +PhaseID[0..*] phase_id
        +Property[0..*] property
        +AuxiliarySubstance[0..*] auxiliary_substance
        +Constraint[0..*] constraint
        +string date_date_added
        +eExpPurpose, string e_exp_purpose
        +Equation[0..*] equation
        +integer n_pure_or_mixture_data_number
        +NumValues[0..*] num_values
        +string s_compiler
        +string s_contributor
        +Variable[0..*] variable
    }
    
    class AuxiliarySubstance {
        +eFunction, string e_function
        +integer n_comp_index
        +RegNum reg_num
        +string s_function
        +ePhase, string e_phase
        +integer n_sample_nm
    }
    
    class Property {
        +ePresentation, string e_presentation
        +integer n_pressure_digits
        +float n_pressure_pa
        +integer n_prop_number
        +float n_ref_pressure
        +integer n_ref_pressure_digits
        +float n_ref_temp
        +integer n_ref_temp_digits
        +integer n_temperature_digits
        +float n_temperature_k
        +PropertyMethodID property_method_id
        +Catalyst[0..*] catalyst
        +CombinedUncertainty[0..*] combined_uncertainty
        +CurveDev[0..*] curve_dev
        +eRefStateType, string e_ref_state_type
        +eStandardState, string e_standard_state
        +PropDeviceSpec prop_device_spec
        +PropPhaseID[0..*] prop_phase_id
        +PropRepeatability prop_repeatability
        +PropUncertainty[0..*] prop_uncertainty
        +RefPhaseID ref_phase_id
        +Solvent solvent
    }
    
    class PropertyMethodID {
        +integer n_comp_index
        +PropertyGroup property_group
        +RegNum reg_num
    }
    
    class PropertyGroup {
        +ActivityFugacityOsmoticProp activity_fugacity_osmotic_prop
        +BioProperties bio_properties
        +CompositionAtPhaseEquilibrium composition_at_phase_equilibrium
        +Criticals criticals
        +ExcessPartialApparentEnergyProp excess_partial_apparent_energy_prop
        +HeatCapacityAndDerivedProp heat_capacity_and_derived_prop
        +PhaseTransition phase_transition
        +ReactionEquilibriumProp reaction_equilibrium_prop
        +ReactionStateChangeProp reaction_state_change_prop
        +RefractionSurfaceTensionSoundSpeed refraction_surface_tension_sound_speed
        +TransportProp transport_prop
        +VaporPBoilingTAzeotropTandP vapor_p_boiling_t_azeotrop_tand_p
        +VolumetricProp volumetric_prop
    }
    
    class Criticals {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class CriticalEvaluation {
        +EquationOfState equation_of_state
        +MultiProp multi_prop
        +SingleProp single_prop
    }
    
    class SingleProp {
        +EvalSinglePropRef[0..*] eval_single_prop_ref
        +string s_eval_single_prop_description
    }
    
    class EvalSinglePropRef {
        +Book book
        +Journal journal
        +Thesis thesis
        +string date_cit
        +eLanguage, string e_language
        +eSourceType, string e_source_type
        +eType, string e_type
        +string s_abstract
        +string[0..*] s_author
        +string s_cas_cit
        +string s_document_origin
        +string s_doi
        +string s_id_num
        +string[0..*] s_keyword
        +string s_location
        +string s_page
        +string s_pub_name
        +string s_title
        +string s_vol
        +TRCRefID trc_ref_id
        +string url_cit
        +string yr_pub_yr
    }
    
    class MultiProp {
        +EvalMultiPropRef[0..*] eval_multi_prop_ref
        +string s_eval_multi_prop_description
        +string s_eval_multi_prop_list
    }
    
    class EvalMultiPropRef {
        +Book book
        +Journal journal
        +Thesis thesis
        +string date_cit
        +eLanguage, string e_language
        +eSourceType, string e_source_type
        +eType, string e_type
        +string s_abstract
        +string[0..*] s_author
        +string s_cas_cit
        +string s_document_origin
        +string s_doi
        +string s_id_num
        +string[0..*] s_keyword
        +string s_location
        +string s_page
        +string s_pub_name
        +string s_title
        +string s_vol
        +TRCRefID trc_ref_id
        +string url_cit
        +string yr_pub_yr
    }
    
    class EquationOfState {
        +EvalEOSRef[0..*] eval_eos_ref
        +string s_eval_eos_description
        +string s_eval_eos_name
    }
    
    class EvalEOSRef {
        +Book book
        +Journal journal
        +Thesis thesis
        +string date_cit
        +eLanguage, string e_language
        +eSourceType, string e_source_type
        +eType, string e_type
        +string s_abstract
        +string[0..*] s_author
        +string s_cas_cit
        +string s_document_origin
        +string s_doi
        +string s_id_num
        +string[0..*] s_keyword
        +string s_location
        +string s_page
        +string s_pub_name
        +string s_title
        +string s_vol
        +TRCRefID trc_ref_id
        +string url_cit
        +string yr_pub_yr
    }
    
    class Prediction {
        +ePredictionType, string e_prediction_type
        +PredictionMethodRef[0..*] prediction_method_ref
        +string s_prediction_method_description
        +string s_prediction_method_name
    }
    
    class PredictionMethodRef {
        +Book book
        +Journal journal
        +Thesis thesis
        +string date_cit
        +eLanguage, string e_language
        +eSourceType, string e_source_type
        +eType, string e_type
        +string s_abstract
        +string[0..*] s_author
        +string s_cas_cit
        +string s_document_origin
        +string s_doi
        +string s_id_num
        +string[0..*] s_keyword
        +string s_location
        +string s_page
        +string s_pub_name
        +string s_title
        +string s_vol
        +TRCRefID trc_ref_id
        +string url_cit
        +string yr_pub_yr
    }
    
    class VaporPBoilingTAzeotropTandP {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class PhaseTransition {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class CompositionAtPhaseEquilibrium {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class ActivityFugacityOsmoticProp {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class VolumetricProp {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class HeatCapacityAndDerivedProp {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class ExcessPartialApparentEnergyProp {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class TransportProp {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class RefractionSurfaceTensionSoundSpeed {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class BioProperties {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string s_method_name
    }
    
    class PropPhaseID {
        +eBioState, string e_bio_state
        +eCrystalLatticeType, string e_crystal_lattice_type
        +ePropPhase, string e_prop_phase
        +integer n_comp_index
        +RegNum reg_num
        +string s_bio_state
        +string s_phase_description
    }
    
    class RefPhaseID {
        +eCrystalLatticeType, string e_crystal_lattice_type
        +eRefPhase, string e_ref_phase
        +integer n_comp_index
        +RegNum reg_num
        +string s_phase_description
    }
    
    class Solvent {
        +ePhase, string e_phase
        +integer n_comp_index
        +RegNum reg_num
    }
    
    class CombinedUncertainty {
        +eCombUncertEvalMethod, string e_comb_uncert_eval_method
        +integer n_comb_uncert_assess_num
        +AsymCombExpandUncert asym_comb_expand_uncert
        +AsymCombStdUncert asym_comb_std_uncert
        +float n_comb_coverage_factor
        +float n_comb_expand_uncert_value
        +float n_comb_std_uncert_value
        +float n_comb_uncert_lev_of_confid
        +string s_comb_uncert_eval_method
        +string s_comb_uncert_evaluator
    }
    
    class PropUncertainty {
        +integer n_uncert_assess_num
        +AsymExpandUncert asym_expand_uncert
        +AsymStdUncert asym_std_uncert
        +float n_coverage_factor
        +float n_expand_uncert_value
        +float n_std_uncert_value
        +float n_uncert_lev_of_confid
        +string s_uncert_eval_method
        +string s_uncert_evaluator
    }
    
    class PropRepeatability {
        +eRepeatMethod, string e_repeat_method
        +float n_prop_repeat_value
        +integer n_repetitions
        +string s_repeat_evaluator
        +string s_repeat_method
    }
    
    class PropDeviceSpec {
        +eDeviceSpecMethod, string e_device_spec_method
        +float n_device_spec_lev_of_confid
        +string s_device_spec_evaluator
        +string s_device_spec_method
    }
    
    class CurveDev {
        +integer n_curve_dev_assess_num
        +float n_curve_dev_value
        +string s_curve_spec
        +float n_curve_rms_dev_value
        +float n_curve_rms_relative_dev_value
        +string s_curve_dev_evaluator
    }
    
    class PhaseID {
        +eCrystalLatticeType, string e_crystal_lattice_type
        +ePhase, string e_phase
        +integer n_comp_index
        +RegNum reg_num
        +string s_phase_description
    }
    
    class Constraint {
        +ConstraintID constraint_id
        +integer n_constr_digits
        +float n_constraint_value
        +ConstrDeviceSpec constr_device_spec
        +ConstrRepeatability constr_repeatability
        +ConstrUncertainty[0..*] constr_uncertainty
        +ConstraintPhaseID constraint_phase_id
        +integer n_constraint_number
        +Solvent solvent
    }
    
    class ConstraintID {
        +ConstraintType constraint_type
        +integer n_comp_index
        +RegNum reg_num
    }
    
    class ConstraintType {
        +eBioVariables, string e_bio_variables
        +eComponentComposition, string e_component_composition
        +eMiscellaneous, string e_miscellaneous
        +eParticipantAmount, string e_participant_amount
        +ePressure, string e_pressure
        +eSolventComposition, string e_solvent_composition
        +eTemperature, string e_temperature
    }
    
    class ConstraintPhaseID {
        +eConstraintPhase, string e_constraint_phase
        +eCrystalLatticeType, string e_crystal_lattice_type
        +integer n_comp_index
        +RegNum reg_num
        +string s_phase_description
    }
    
    class ConstrUncertainty {
        +float n_coverage_factor
        +float n_expand_uncert_value
        +float n_std_uncert_value
        +float n_uncert_lev_of_confid
        +string s_uncert_eval_method
        +string s_uncert_evaluator
    }
    
    class ConstrRepeatability {
        +eRepeatMethod, string e_repeat_method
        +float n_repeat_value
        +integer n_repetitions
        +string s_repeat_evaluator
        +string s_repeat_method
    }
    
    class ConstrDeviceSpec {
        +eDeviceSpecMethod, string e_device_spec_method
        +float n_device_spec_lev_of_confid
        +float n_device_spec_value
        +string s_device_spec_evaluator
        +string s_device_spec_method
    }
    
    class Variable {
        +integer n_var_number
        +VariableID variable_id
        +Solvent solvent
        +VarDeviceSpec var_device_spec
        +VarPhaseID var_phase_id
        +VarRepeatability var_repeatability
        +VarUncertainty[0..*] var_uncertainty
    }
    
    class VariableID {
        +integer n_comp_index
        +RegNum reg_num
        +VariableType variable_type
    }
    
    class VariableType {
        +eBioVariables, string e_bio_variables
        +eComponentComposition, string e_component_composition
        +eMiscellaneous, string e_miscellaneous
        +eParticipantAmount, string e_participant_amount
        +ePressure, string e_pressure
        +eSolventComposition, string e_solvent_composition
        +eTemperature, string e_temperature
    }
    
    class VarPhaseID {
        +eCrystalLatticeType, string e_crystal_lattice_type
        +eVarPhase, string e_var_phase
        +integer n_comp_index
        +RegNum reg_num
        +string s_phase_description
    }
    
    class VarUncertainty {
        +integer n_uncert_assess_num
        +float n_coverage_factor
        +float n_expand_uncert_value
        +float n_std_uncert_value
        +float n_uncert_lev_of_confid
        +string s_uncert_eval_method
        +string s_uncert_evaluator
    }
    
    class VarRepeatability {
        +eRepeatMethod, string e_repeat_method
        +integer n_repetitions
        +float n_var_repeat_value
        +string s_repeat_evaluator
        +string s_repeat_method
    }
    
    class VarDeviceSpec {
        +eDeviceSpecMethod, string e_device_spec_method
        +float n_device_spec_lev_of_confid
        +string s_device_spec_evaluator
        +string s_device_spec_method
    }
    
    class NumValues {
        +PropertyValue[0..*] property_value
        +VariableValue[0..*] variable_value
    }
    
    class VariableValue {
        +integer n_var_digits
        +integer n_var_number
        +float n_var_value
        +float n_var_device_spec_value
        +VarRepeatability var_repeatability
        +VarUncertainty[0..*] var_uncertainty
    }
    
    class PropertyValue {
        +integer n_prop_digits
        +integer n_prop_number
        +float n_prop_value
        +PropLimit prop_limit
        +CombinedUncertainty[0..*] combined_uncertainty
        +CurveDev[0..*] curve_dev
        +float n_prop_device_spec_value
        +PropRepeatability prop_repeatability
        +PropUncertainty[0..*] prop_uncertainty
    }
    
    class PropLimit {
        +integer n_prop_limit_digits
        +float n_prop_lower_limit_value
        +float n_prop_upper_limit_value
    }
    
    class AsymCombStdUncert {
        +float n_negative_value
        +float n_positive_value
    }
    
    class AsymCombExpandUncert {
        +float n_negative_value
        +float n_positive_value
    }
    
    class AsymStdUncert {
        +float n_negative_value
        +float n_positive_value
    }
    
    class AsymExpandUncert {
        +float n_negative_value
        +float n_positive_value
    }
    
    class Equation {
        +eEqName, string e_eq_name
        +string s_eq_name
        +string url_math_source
        +Covariance[0..*] covariance
        +EqConstant[0..*] eq_constant
        +EqConstraint[0..*] eq_constraint
        +EqParameter[0..*] eq_parameter
        +EqProperty[0..*] eq_property
        +EqVariable[0..*] eq_variable
        +float n_covariance_lev_of_confid
    }
    
    class EqProperty {
        +integer n_prop_number
        +integer n_pure_or_mixture_data_number
        +integer n_reaction_data_number
        +string s_eq_symbol
        +integer[0..*] n_eq_prop_index
        +float n_eq_prop_range_max
        +float n_eq_prop_range_min
        +string s_other_prop_unit
    }
    
    class EqConstraint {
        +integer n_constraint_number
        +integer n_pure_or_mixture_data_number
        +integer n_reaction_data_number
        +string s_eq_symbol
        +integer[0..*] n_eq_constraint_index
        +float n_eq_constraint_range_max
        +float n_eq_constraint_range_min
        +string s_other_constraint_unit
    }
    
    class EqVariable {
        +integer n_pure_or_mixture_data_number
        +integer n_reaction_data_number
        +integer n_var_number
        +string s_eq_symbol
        +integer[0..*] n_eq_var_index
        +float n_eq_var_range_max
        +float n_eq_var_range_min
        +string s_other_var_unit
    }
    
    class EqParameter {
        +integer n_eq_par_digits
        +float n_eq_par_value
        +string s_eq_par_symbol
        +integer[0..*] n_eq_par_index
        +integer n_eq_par_number
    }
    
    class EqConstant {
        +integer n_eq_constant_digits
        +float n_eq_constant_value
        +string s_eq_constant_symbol
        +integer[0..*] n_eq_constant_index
    }
    
    class Covariance {
        +float n_covariance_value
        +integer n_eq_par_number1
        +integer n_eq_par_number2
    }
    
    class ReactionData {
        +eReactionType, string e_reaction_type
        +Participant[0..*] participant
        +Property[0..*] property
        +AuxiliarySubstance[0..*] auxiliary_substance
        +Constraint[0..*] constraint
        +string date_date_added
        +eExpPurpose, string e_exp_purpose
        +eReactionFormalism, string e_reaction_formalism
        +Equation[0..*] equation
        +integer n_electron_number
        +integer n_reaction_data_number
        +NumValues[0..*] num_values
        +string s_compiler
        +string s_contributor
        +Solvent[0..*] solvent
        +Variable[0..*] variable
    }
    
    class Participant {
        +eCrystalLatticeType, string e_crystal_lattice_type
        +ePhase, string e_phase
        +integer n_comp_index
        +RegNum reg_num
        +string s_phase_description
        +eCompositionRepresentation, string e_composition_representation
        +eStandardState, string e_standard_state
        +float n_numerical_composition
        +integer n_sample_nm
        +float n_stoichiometric_coef
    }
    
    class ReactionStateChangeProp {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string[0..*] s_method_name
    }
    
    class ReactionEquilibriumProp {
        +CriticalEvaluation critical_evaluation
        +eMethodName, string e_method_name
        +ePropName, string e_prop_name
        +Prediction prediction
        +string[0..*] s_method_name
    }
    
    class Catalyst {
        +integer n_comp_index
        +RegNum reg_num
        +ePhase, string e_phase
    }
    
    class eType {
        << Enumeration >>
        +BOOK
        +JOURNAL
        +REPORT
        +PATENT
        +THESIS
        +CONFERENCEPROCEEDINGS
        +ARCHIVEDDOCUMENT
        +PERSONALCORRESPONDENCE
        +PUBLISHEDTRANSLATION
        +UNSPECIFIED
    }
    
    class eSourceType {
        << Enumeration >>
        +ORIGINAL
        +CHEMICALABSTRACTS
        +OTHER
    }
    
    class eLanguage {
        << Enumeration >>
        +CHINESE
        +ENGLISH
        +FRENCH
        +GERMAN
        +JAPANESE
        +POLISH
        +RUSSIAN
        +OTHER_LANGUAGE
    }
    
    class eSpeciationState {
        << Enumeration >>
        +EQUILIBRIUM
        +SINGLE_SPECIES
    }
    
    class eSource {
        << Enumeration >>
        +COMMERCIAL_SOURCE
        +SYNTHESIZED_BY_THE_AUTHORS
        +SYNTHESIZED_BY_OTHERS
        +STANDARD_REFERENCE_MATERIAL_SRM
        +ISOLATED_FROM_A_NATURAL_PRODUCT
        +NOT_STATED_IN_THE_DOCUMENT
        +NO_SAMPLE_USED
    }
    
    class eStatus {
        << Enumeration >>
        +UNKNOWN
        +NOTDESCRIBED
        +PREVIOUSPAPER
        +NOSAMPLE
    }
    
    class ePurifMethod {
        << Enumeration >>
        +IMPURITY_ADSORPTION
        +VACUUM_DEGASIFICATION
        +CHEMICAL_REAGENT_TREATMENT
        +CRYSTALLIZATION_FROM_MELT
        +CRYSTALLIZATION_FROM_SOLUTION
        +LIQUID_CHROMATOGRAPHY
        +DRIED_WITH_CHEMICAL_REAGENT
        +DRIED_IN_A_DESICCATOR
        +DRIED_BY_OVEN_HEATING
        +DRIED_BY_VACUUM_HEATING
        +DEGASSED_BY_BOILING_OR_ULTRASONICALLY
        +DEGASSED_BY_EVACUATION
        +DEGASSED_BY_FREEZING_AND_MELTING_IN_VACUUM
        +FRACTIONAL_CRYSTALLIZATION
        +FRACTIONAL_DISTILLATION
        +MOLECULAR_SIEVE_TREATMENT
        +UNSPECIFIED
        +PREPARATIVE_GAS_CHROMATOGRAPHY
        +SUBLIMATION
        +STEAM_DISTILLATION
        +SOLVENT_EXTRACTION
        +SALTING_OUT_OF_SOLUTION
        +ZONE_REFINING
        +OTHER
        +NONE_USED
    }
    
    class eAnalMeth {
        << Enumeration >>
        +CHEMICAL_ANALYSIS
        +DIFFERENCE_BETWEEN_BUBBLE_AND_DEW_TEMPERATURES
        +DENSITY
        +DSC
        +ESTIMATION
        +GAS_CHROMATOGRAPHY
        +FRACTION_MELTING_IN_AN_ADIABATIC_CALORIMETER
        +MASS_SPECTROMETRY
        +NMR_PROTON
        +NMR_OTHER
        +NOT_KNOWN
        +SPECTROSCOPY
        +THERMAL_ANALYSIS_USING_TEMPERATURETIME_MEASUREMENT
        +ACIDBASE_TITRATION
        +OTHER_TYPES_OF_TITRATION
        +MASS_LOSS_ON_DRYING
        +KARL_FISCHER_TITRATION
        +HPLC
        +ION_CHROMATOGRAPHY
        +IONSELECTIVE_ELECTRODE
        +CO2_YIELD_IN_COMBUSTION_PRODUCTS
        +OTHER
        +ESTIMATED_BY_THE_COMPILER
        +STATED_BY_SUPPLIER
    }
    
    class eFunction {
        << Enumeration >>
        +COFACTOR
        +BUFFER
        +INERT
    }
    
    class eExpPurpose {
        << Enumeration >>
        +PRINCIPAL_OBJECTIVE_OF_THE_WORK
        +SECONDARY_PURPOSE_BYPRODUCT_OF_OTHER_OBJECTIVE
        +DETERMINED_FOR_IDENTIFICATION_OF_A_SYNTHESIZED_COMPOUND
    }
    
    class ePropName {
        << Enumeration >>
        +THERMODYNAMIC_EQUILIBRIUM_CONSTANT
        +EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLALITY_MOLKGN
        +EQUILIBRIUM_CONSTANT_IN_TERMS_OF_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3N
        +EQUILIBRIUM_CONSTANT_IN_TERMS_OF_PARTIAL_PRESSURE_KPAN
        +EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLE_FRACTION
        +NATURAL_LOGARITHM_OF_THERMODYNAMIC_EQUILIBRIUM_CONSTANT
        +NATURAL_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLALITY_MOLKGN
        +NATURAL_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3N
        +NATURAL_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_PARTIAL_PRESSURE_KPAN
        +NATURAL_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLE_FRACTION
        +DECADIC_LOGARITHM_OF_THERMODYNAMIC_EQUILIBRIUM_CONSTANT
        +DECADIC_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLALITY_MOLKGN
        +DECADIC_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3N
        +DECADIC_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_PARTIAL_PRESSURE_KPAN
        +DECADIC_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLE_FRACTION
    }
    
    class eMethodName {
        << Enumeration >>
        +STATIC_EQUILIBRATION
        +DYNAMIC_EQUILIBRATION
        +CHROMATOGRAPHY
        +IR_SPECTROMETRY
        +UV_SPECTROSCOPY
        +NMR_SPECTROMETRY
        +TITRATION
        +POTENTIAL_DIFFERENCE_OF_AN_ELECTROCHEMICAL_CELL
        +ANION_EXCHANGE
        +CATION_EXCHANGE
        +CELL_POTENTIAL_WITH_GLASS_ELECTRODE
        +CELL_POTENTIAL_WITH_PLATINUM_ELECTRODE
        +CELL_POTENTIAL_WITH_QUINHYDRONE_ELECTRODE
        +CELL_POTENTIAL_WITH_REDOX_ELECTRODE
        +COLORIMETRY
        +CONDUCTIVITY_MEASUREMENT
        +COULOMETRY
        +CRYOSCOPY
        +DISTRIBUTION_BETWEEN_TWO_PHASES
        +ION_SELECTIVE_ELECTRODE
        +MOLAR_VOLUME_DETERMINATION
        +POLAROGRAPHY
        +POTENTIOMETRY
        +PROTON_RELAXATION
        +RATE_OF_REACTION
        +SOLUBILITY_MEASUREMENT
        +SPECTROPHOTOMETRY
        +THERMAL_LENSING_SPECTROPHOTOMETRY
        +TRANSIENT_CONDUCTIVITY_MEASUREMENT
        +SOLVENT_EXTRACTION
        +VOLTAMMETRY
        +OTHER
    }
    
    class ePredictionType {
        << Enumeration >>
        +AB_INITIO
        +MOLECULAR_DYNAMICS
        +SEMIEMPIRICAL_QUANTUM_METHODS
        +MOLECULAR_MECHANICS
        +STATISTICAL_MECHANICS
        +CORRESPONDING_STATES
        +CORRELATION
        +GROUP_CONTRIBUTION
    }
    
    class ePropPhase {
        << Enumeration >>
        +CRYSTAL_5
        +CRYSTAL_4
        +CRYSTAL_3
        +CRYSTAL_2
        +CRYSTAL_1
        +CRYSTAL
        +CRYSTAL_OF_UNKNOWN_TYPE
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3
        +METASTABLE_CRYSTAL
        +GLASS
        +SMECTIC_LIQUID_CRYSTAL
        +SMECTIC_LIQUID_CRYSTAL_1
        +SMECTIC_LIQUID_CRYSTAL_2
        +NEMATIC_LIQUID_CRYSTAL
        +NEMATIC_LIQUID_CRYSTAL_1
        +NEMATIC_LIQUID_CRYSTAL_2
        +CHOLESTERIC_LIQUID_CRYSTAL
        +LIQUID_CRYSTAL_OF_UNKNOWN_TYPE
        +LIQUID
        +LIQUID_MIXTURE_1
        +LIQUID_MIXTURE_2
        +LIQUID_MIXTURE_3
        +SOLUTION
        +SOLUTION_1
        +SOLUTION_2
        +SOLUTION_3
        +SOLUTION_4
        +FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES
        +IDEAL_GAS
        +GAS
        +AIR_AT_1_ATMOSPHERE
    }
    
    class eCrystalLatticeType {
        << Enumeration >>
        +CUBIC
        +TETRAGONAL
        +HEXAGONAL
        +RHOMBOHEDRAL
        +ORTHORHOMBIC
        +MONOCLINIC
        +TRICLINIC
    }
    
    class eBioState {
        << Enumeration >>
        +NATIVE
        +DENATURATED
    }
    
    class ePresentation {
        << Enumeration >>
        +DIRECT_VALUE_X
        +DIFFERENCE_BETWEEN_UPPER_AND_LOWER_TEMPERATURE_XT2XT1
        +DIFFERENCE_BETWEEN_UPPER_AND_LOWER_PRESSURE_XP2XP1
        +MEAN_BETWEEN_UPPER_AND_LOWER_TEMPERATURE_XT2XT12
        +DIFFERENCE_WITH_THE_REFERENCE_STATE_XXREF
        +RATIO_WITH_THE_REFERENCE_STATE_XXREF
        +RATIO_OF_DIFFERENCE_WITH_THE_REFERENCE_STATE_TO_THE_REFERENCE_STATE_XXREFXREF
    }
    
    class eRefStateType {
        << Enumeration >>
        +REFERENCE_PHASE_WITH_THE_SAME_COMPOSITION_AT_FIXED_TEMPERATURE_AND_PRESSURE
        +REFERENCE_PHASE_WITH_THE_SAME_COMPOSITION_TEMPERATURE_AND_PRESSURE
        +REFERENCE_PHASE_AT_FIXED_TEMPERATURE_AND_THE_SAME_PRESSURE
        +REFERENCE_PHASE_AT_THE_SAME_TEMPERATURE_AND_FIXED_PRESSURE
        +IDEAL_GAS_AT_THE_SAME_AMOUNT_DENSITY_TEMPERATURE_AND_COMPOSITION
        +IDEAL_MIXTURE_OF_PURE_FLUID_COMPONENTS_AT_THE_SAME_AMOUNT_DENSITY_TEMPERATURE_AND_COMPOSITION
        +PHASE_IN_EQUILIBRIUM_WITH_PRIMARY_PHASE_AT_THE_SAME_TEMPERATURE_AND_PRESSURE
        +PURE_COMPONENTS_IN_THE_SAME_PROPORTION_AT_FIXED_TEMPERATURE_AND_PRESSURE
        +PURE_COMPONENTS_IN_THE_SAME_PROPORTION_AT_THE_SAME_TEMPERATURE_AND_PRESSURE
        +PURE_SOLVENT_AT_THE_TEMPERATURE_OF_THE_SAME_PHASE_EQUILIBRIUM
        +PURE_SOLVENT_AT_THE_SAME_TEMPERATURE_AND_PRESSURE
        +PURE_SOLUTE_AT_THE_SAME_TEMPERATURE_AND_PRESSURE
    }
    
    class eRefPhase {
        << Enumeration >>
        +CRYSTAL_5
        +CRYSTAL_4
        +CRYSTAL_3
        +CRYSTAL_2
        +CRYSTAL_1
        +CRYSTAL
        +CRYSTAL_OF_UNKNOWN_TYPE
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3
        +METASTABLE_CRYSTAL
        +GLASS
        +SMECTIC_LIQUID_CRYSTAL
        +SMECTIC_LIQUID_CRYSTAL_1
        +SMECTIC_LIQUID_CRYSTAL_2
        +NEMATIC_LIQUID_CRYSTAL
        +NEMATIC_LIQUID_CRYSTAL_1
        +NEMATIC_LIQUID_CRYSTAL_2
        +CHOLESTERIC_LIQUID_CRYSTAL
        +LIQUID_CRYSTAL_OF_UNKNOWN_TYPE
        +LIQUID
        +LIQUID_MIXTURE_1
        +LIQUID_MIXTURE_2
        +LIQUID_MIXTURE_3
        +SOLUTION
        +SOLUTION_1
        +SOLUTION_2
        +SOLUTION_3
        +SOLUTION_4
        +FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES
        +IDEAL_GAS
        +GAS
        +AIR_AT_1_ATMOSPHERE
    }
    
    class eStandardState {
        << Enumeration >>
        +PURE_COMPOUND
        +PURE_LIQUID_SOLUTE
        +STANDARD_MOLALITY_1_MOLKG_SOLUTE
        +STANDARD_AMOUNT_CONCENTRATION_1_MOLDM3_SOLUTE
        +INFINITE_DILUTION_SOLUTE
    }
    
    class eCombUncertEvalMethod {
        << Enumeration >>
        +PROPAGATION_OF_EVALUATED_STANDARD_UNCERTAINTIES
        +COMPARISON_WITH_REFERENCE_PROPERTY_VALUES
    }
    
    class eRepeatMethod {
        << Enumeration >>
        +STANDARD_DEVIATION_OF_A_SINGLE_VALUE_BIASED
        +STANDARD_DEVIATION_OF_A_SINGLE_VALUE_UNBIASED
        +STANDARD_DEVIATION_OF_THE_MEAN
        +OTHER
    }
    
    class eDeviceSpecMethod {
        << Enumeration >>
        +SPECIFIED_BY_THE_MANUFACTURER
        +CERTIFIED_OR_CALIBRATED_BY_A_THIRD_PARTY
        +CALIBRATED_BY_THE_EXPERIMENTALIST
    }
    
    class ePhase {
        << Enumeration >>
        +CRYSTAL_5
        +CRYSTAL_4
        +CRYSTAL_3
        +CRYSTAL_2
        +CRYSTAL_1
        +CRYSTAL
        +CRYSTAL_OF_UNKNOWN_TYPE
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3
        +METASTABLE_CRYSTAL
        +GLASS
        +SMECTIC_LIQUID_CRYSTAL
        +SMECTIC_LIQUID_CRYSTAL_1
        +SMECTIC_LIQUID_CRYSTAL_2
        +NEMATIC_LIQUID_CRYSTAL
        +NEMATIC_LIQUID_CRYSTAL_1
        +NEMATIC_LIQUID_CRYSTAL_2
        +CHOLESTERIC_LIQUID_CRYSTAL
        +LIQUID_CRYSTAL_OF_UNKNOWN_TYPE
        +LIQUID
        +LIQUID_MIXTURE_1
        +LIQUID_MIXTURE_2
        +LIQUID_MIXTURE_3
        +SOLUTION
        +SOLUTION_1
        +SOLUTION_2
        +SOLUTION_3
        +SOLUTION_4
        +FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES
        +IDEAL_GAS
        +GAS
        +AIR_AT_1_ATMOSPHERE
    }
    
    class eTemperature {
        << Enumeration >>
        +TEMPERATURE_K
        +UPPER_TEMPERATURE_K
        +LOWER_TEMPERATURE_K
    }
    
    class ePressure {
        << Enumeration >>
        +PRESSURE_KPA
        +PARTIAL_PRESSURE_KPA
        +UPPER_PRESSURE_KPA
        +LOWER_PRESSURE_KPA
    }
    
    class eComponentComposition {
        << Enumeration >>
        +MOLE_FRACTION
        +MASS_FRACTION
        +MOLALITY_MOLKG
        +AMOUNT_CONCENTRATION_MOLARITY_MOLDM3
        +VOLUME_FRACTION
        +RATIO_OF_AMOUNT_OF_SOLUTE_TO_MASS_OF_SOLUTION_MOLKG
        +RATIO_OF_MASS_OF_SOLUTE_TO_VOLUME_OF_SOLUTION_KGM3
        +AMOUNT_RATIO_OF_SOLUTE_TO_SOLVENT
        +MASS_RATIO_OF_SOLUTE_TO_SOLVENT
        +VOLUME_RATIO_OF_SOLUTE_TO_SOLVENT
        +INITIAL_MOLE_FRACTION_OF_SOLUTE
        +FINAL_MOLE_FRACTION_OF_SOLUTE
        +INITIAL_MASS_FRACTION_OF_SOLUTE
        +FINAL_MASS_FRACTION_OF_SOLUTE
        +INITIAL_MOLALITY_OF_SOLUTE_MOLKG
        +FINAL_MOLALITY_OF_SOLUTE_MOLKG
    }
    
    class eSolventComposition {
        << Enumeration >>
        +SOLVENT_MOLE_FRACTION
        +SOLVENT_MASS_FRACTION
        +SOLVENT_VOLUME_FRACTION
        +SOLVENT_MOLALITY_MOLKG
        +SOLVENT_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3
        +SOLVENT_AMOUNT_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT
        +SOLVENT_MASS_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT
        +SOLVENT_VOLUME_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT
        +SOLVENT_RATIO_OF_AMOUNT_OF_COMPONENT_TO_MASS_OF_SOLVENT_MOLKG
        +SOLVENT_RATIO_OF_COMPONENT_MASS_TO_VOLUME_OF_SOLVENT_KGM3
    }
    
    class eMiscellaneous {
        << Enumeration >>
        +WAVELENGTH_NM
        +FREQUENCY_MHZ
        +MOLAR_VOLUME_M3MOL
        +SPECIFIC_VOLUME_M3KG
        +MASS_DENSITY_KGM3
        +AMOUNT_DENSITY_MOLM3
        +MOLAR_ENTROPY_JKMOL
        +RELATIVE_ACTIVITY
        +ACTIVITY_COEFFICIENT
    }
    
    class eBioVariables {
        << Enumeration >>
        +PH
        +IONIC_STRENGTH_MOLALITY_BASIS_MOLKG
        +IONIC_STRENGTH_AMOUNT_CONCENTRATION_BASIS_MOLDM3
        +PC_AMOUNT_CONCENTRATION_BASIS
        +SOLVENT_PC_AMOUNT_CONCENTRATION_BASIS
    }
    
    class eParticipantAmount {
        << Enumeration >>
        +AMOUNT_MOL
        +MASS_KG
    }
    
    class eConstraintPhase {
        << Enumeration >>
        +CRYSTAL_5
        +CRYSTAL_4
        +CRYSTAL_3
        +CRYSTAL_2
        +CRYSTAL_1
        +CRYSTAL
        +CRYSTAL_OF_UNKNOWN_TYPE
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3
        +METASTABLE_CRYSTAL
        +GLASS
        +SMECTIC_LIQUID_CRYSTAL
        +SMECTIC_LIQUID_CRYSTAL_1
        +SMECTIC_LIQUID_CRYSTAL_2
        +NEMATIC_LIQUID_CRYSTAL
        +NEMATIC_LIQUID_CRYSTAL_1
        +NEMATIC_LIQUID_CRYSTAL_2
        +CHOLESTERIC_LIQUID_CRYSTAL
        +LIQUID_CRYSTAL_OF_UNKNOWN_TYPE
        +LIQUID
        +LIQUID_MIXTURE_1
        +LIQUID_MIXTURE_2
        +LIQUID_MIXTURE_3
        +SOLUTION
        +SOLUTION_1
        +SOLUTION_2
        +SOLUTION_3
        +SOLUTION_4
        +FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES
        +IDEAL_GAS
        +GAS
        +AIR_AT_1_ATMOSPHERE
    }
    
    class eVarPhase {
        << Enumeration >>
        +CRYSTAL_5
        +CRYSTAL_4
        +CRYSTAL_3
        +CRYSTAL_2
        +CRYSTAL_1
        +CRYSTAL
        +CRYSTAL_OF_UNKNOWN_TYPE
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2
        +CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3
        +METASTABLE_CRYSTAL
        +GLASS
        +SMECTIC_LIQUID_CRYSTAL
        +SMECTIC_LIQUID_CRYSTAL_1
        +SMECTIC_LIQUID_CRYSTAL_2
        +NEMATIC_LIQUID_CRYSTAL
        +NEMATIC_LIQUID_CRYSTAL_1
        +NEMATIC_LIQUID_CRYSTAL_2
        +CHOLESTERIC_LIQUID_CRYSTAL
        +LIQUID_CRYSTAL_OF_UNKNOWN_TYPE
        +LIQUID
        +LIQUID_MIXTURE_1
        +LIQUID_MIXTURE_2
        +LIQUID_MIXTURE_3
        +SOLUTION
        +SOLUTION_1
        +SOLUTION_2
        +SOLUTION_3
        +SOLUTION_4
        +FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES
        +IDEAL_GAS
        +GAS
        +AIR_AT_1_ATMOSPHERE
    }
    
    class eEqName {
        << Enumeration >>
        +THERMOMLANTOINEVAPORPRESSURE
        +THERMOMLCUSTOMEXPANSION
        +THERMOMLHELMHOLTZ3GENERALEOS
        +THERMOMLHELMHOLTZ4GENERALEOS
        +THERMOMLWAGNERLINEARVAPORPRESSURE
        +THERMOMLWAGNER25LINEARVAPORPRESSURE
        +THERMOMLWAGNER36LINEARVAPORPRESSURE
        +THERMOMLPOLYNOMIALEXPANSION
        +THERMOMLSPANWAGNER12NONPOLAREOS
        +THERMOMLSPANWAGNER12POLAREOS
    }
    
    class eCompositionRepresentation {
        << Enumeration >>
        +AMOUNT_RATIO_OF_SOLVENT_TO_PARTICIPANT
        +MOLALITY_AMOUNT_OF_PARTICIPANT_PER_MASS_OF_SOLVENT_MOLKG
        +AMOUNT_OF_PARTICIPANT_PER_MASS_OF_SOLUTION_MOLKG
        +AMOUNT_CONCENTRATION_AMOUNT_OF_PARTICIPANT_PER_VOLUME_OF_SOLUTION_MOLDM3
        +AMOUNT_RATIO_OF_PARTICIPANT_TO_SOLVENT
        +MASS_RATIO_OF_PARTICIPANT_TO_SOLVENT
        +VOLUME_RATIO_OF_PARTICIPANT_TO_SOLVENT
        +MASS_OF_PARTICIPANT_PER_VOLUME_OF_SOLUTION_KGM3
    }
    
    class eReactionFormalism {
        << Enumeration >>
        +CHEMICAL
        +BIOCHEMICAL
    }
    
    class eReactionType {
        << Enumeration >>
        +COMBUSTION_WITH_OXYGEN
        +ADDITION_OF_VARIOUS_COMPOUNDS_TO_UNSATURATED_COMPOUNDS
        +ADDITION_OF_WATER_TO_A_LIQUID_OR_SOLID_TO_PRODUCE_A_HYDRATE
        +ATOMIZATION_OR_FORMATION_FROM_ATOMS
        +COMBUSTION_WITH_OTHER_ELEMENTS_OR_COMPOUNDS
        +ESTERIFICATION
        +EXCHANGE_OF_ALKYL_GROUPS
        +EXCHANGE_OF_HYDROGEN_ATOMS_WITH_OTHER_GROUPS
        +FORMATION_OF_A_COMPOUND_FROM_ELEMENTS_IN_THEIR_STABLE_STATE
        +HALOGENATION_ADDITION_OF_OR_REPLACEMENT_BY_A_HALOGEN
        +HYDROGENATION_ADDITION_OF_HYDROGEN_TO_UNSATURATED_COMPOUNDS
        +HYDROHALOGENATION
        +HYDROLYSIS_OF_IONS
        +OTHER_REACTIONS_WITH_WATER
        +ION_EXCHANGE
        +NEUTRALIZATION_REACTION_OF_AN_ACID_WITH_A_BASE
        +OXIDATION_WITH_OXIDIZING_AGENTS_OTHER_THAN_OXYGEN
        +OXIDATION_WITH_OXYGEN_NOT_COMPLETE
        +POLYMERIZATION_ALL_OTHER_TYPES
        +HOMONUCLEAR_DIMERIZATION
        +SOLVOLYIS_SOLVENTS_OTHER_THAN_WATER
        +STEREOISOMERISM
        +STRUCTURAL_ISOMERIZATION
        +FORMATION_OF_ION
        +OTHER_REACTIONS
    }
    
```