---
id-field: false
xmlns:
  "": http://www.iupac.org/namespaces/ThermoML
  xsi: http://www.w3.org/2001/XMLSchema
---

# Thermoml

## Objects

### DataReport

- citation
  - Type: Citation
  - XML: Citation
- version
  - Type: Version
  - XML: Version
- compound
  - Type: Compound[]
  - XML: Compound
- pure_or_mixture_data
  - Type: PureOrMixtureData[]
  - XML: PureOrMixtureData
- reaction_data
  - Type: ReactionData[]
  - XML: ReactionData

### Version

- n_version_major
  - Type: integer
  - XML: nVersionMajor
- n_version_minor
  - Type: integer
  - XML: nVersionMinor

### Citation

- book
  - Type: Book
  - XML: book
- journal
  - Type: Journal
  - XML: journal
- thesis
  - Type: Thesis
  - XML: thesis
- date_cit
  - Type: string
  - XML: dateCit
  - Description: Date of the citation
- e_language
  - Type: eLanguage, string
  - XML: eLanguage
  - Description: Language of publication
- e_source_type
  - Type: eSourceType, string
  - XML: eSourceType
  - Description: The source status type for a citation
- e_type
  - Type: eType, string
  - XML: eType
  - Description: The type of publication
- s_abstract
  - Type: string
  - XML: sAbstract
  - Description: An abstract of the publication
- s_author
  - Type: string[]
  - XML: sAuthor
  - Description: Author of publication
- s_cas_cit
  - Type: string
  - XML: sCASCit
  - Description: The Chemical Abstracts Service citation
- s_document_origin
  - Type: string
  - XML: sDocumentOrigin
  - Description: Company, institution, or conference name
- s_doi
  - Type: string
  - XML: sDOI
  - Description: DOI
- s_id_num
  - Type: string
  - XML: sIDNum
  - Description: Identification number, e.g., a patent number or a document number
- s_keyword
  - Type: string[]
  - XML: sKeyword
- s_location
  - Type: string
  - XML: sLocation
  - Description: Reference to a location
- s_page
  - Type: string
  - XML: sPage
  - Description: Page range where the publication can be found
- s_pub_name
  - Type: string
  - XML: sPubName
  - Description: Name of the publication.
- s_title
  - Type: string
  - XML: sTitle
  - Description: Title of the publication
- s_vol
  - Type: string
  - XML: sVol
  - Description: Volume number
- trc_ref_id
  - Type: TRCRefID
  - XML: TRCRefID
- url_cit
  - Type: string
  - XML: urlCit
  - Description: URL to the publication
- yr_pub_yr
  - Type: string
  - XML: yrPubYr
  - Description: Publication year

### TRCRefID

- n_authorn
  - Type: integer
  - XML: nAuthorn
  - Description: Integer identifier to distinguish conflicts
- s_author1
  - Type: string
  - XML: sAuthor1
  - Description: First 3 characters of Author 1 last name
- s_author2
  - Type: string
  - XML: sAuthor2
  - Description: First 3 characters of Author 2 last name
- yr_yr_pub
  - Type: integer
  - XML: yrYrPub
  - Description: Integer year of publication

### Book

- s_chapter
  - Type: string
  - XML: sChapter
  - Description: Chapter number
- s_edition
  - Type: string
  - XML: sEdition
  - Description: Edition number of the book
- s_editor
  - Type: string[]
  - XML: sEditor
  - Description: Editor of the book
- s_isbn
  - Type: string
  - XML: sISBN
  - Description: The International Standard Book Number
- s_publisher
  - Type: string
  - XML: sPublisher
  - Description: Publisher name and city

### Journal

- s_coden
  - Type: string
  - XML: sCODEN
  - Description: The CODEN identification of the journal
- s_issn
  - Type: string
  - XML: sISSN
  - Description: The International Standard Subscription Number
- s_issue
  - Type: string
  - XML: sIssue
  - Description: Issue number, usually indicates month

### Thesis

- s_deg
  - Type: string
  - XML: sDeg
  - Description: Academic degree designation, e.g., MS or PhD
- s_deg_inst
  - Type: string
  - XML: sDegInst
  - Description: Academic degree granting institution
- s_umi_pub_num
  - Type: string
  - XML: sUMIPubNum
  - Description: University Microfilms International Publication Number

### Compound

- biomaterial
  - Type: Biomaterial
  - XML: biomaterial
- ion
  - Type: Ion
  - XML: ion
- multicomponent_substance
  - Type: MulticomponentSubstance
  - XML: MulticomponentSubstance
- polymer
  - Type: Polymer
  - XML: polymer
- e_speciation_state
  - Type: eSpeciationState, string
  - XML: eSpeciationState
- n_comp_index
  - Type: integer
  - XML: nCompIndex
  - Description: Index to link compounds to data
- n_pub_chem_id
  - Type: integer
  - XML: nPubChemID
- reg_num
  - Type: RegNum
  - XML: RegNum
- s_cas_name
  - Type: string
  - XML: sCASName
- s_common_name
  - Type: string[]
  - XML: sCommonName
  - Description: Common name, string Common name
- s_formula_molec
  - Type: string
  - XML: sFormulaMolec
  - Description: Molecular formula, string Chemical molecular formula
- s_iupac_name
  - Type: string
  - XML: sIUPACName
  - Description: IUPAC name, string International Union of Physics and Applied Chemistry name
- s_org_id
  - Type: SOrgID[]
  - XML: sOrgID
- s_smiles
  - Type: string[]
  - XML: sSmiles
  - Description: SMILES notation, string SMILES notation
- s_standard_in_ch_i
  - Type: string
  - XML: sStandardInChI
  - Description: Standard InChI string IUPAC International Chemical Identifier
- s_standard_in_ch_i_key
  - Type: string
  - XML: sStandardInChIKey
  - Description: Standard InChI key
- sample
  - Type: Sample[]
  - XML: Sample

### RegNum

- n_org_num
  - Type: integer
  - XML: nOrgNum
- n_casr_num
  - Type: integer
  - XML: nCASRNum
- s_organization
  - Type: string
  - XML: sOrganization

### SOrgID

- s_org_identifier
  - Type: string
  - XML: sOrgIdentifier
- s_organization
  - Type: string
  - XML: sOrganization

### Polymer

- n_deg_of_polymerization_dispersity
  - Type: float
  - XML: nDegOfPolymerizationDispersity
- n_mass_avg_mol_mass
  - Type: float
  - XML: nMassAvgMolMass
  - Description: Weight average molecular mass, kg/kmol
- n_molar_mass_dispersity
  - Type: float
  - XML: nMolarMassDispersity
- n_number_avg_mol_mass
  - Type: float
  - XML: nNumberAvgMolMass
  - Description: Number average molecular mass, kg/kmol
- n_peak_avg_mol_mass
  - Type: float
  - XML: nPeakAvgMolMass
  - Description: Peak average molecular mass, kg/kmol
- n_viscosity_avg_mol_mass
  - Type: float
  - XML: nViscosityAvgMolMass
  - Description: Viscosity average molecular mass, kg/kmol
- n_z_avg_mol_mass
  - Type: float
  - XML: nZAvgMolMass
  - Description: Z average molecular mass, kg/kmol

### Ion

- n_charge
  - Type: integer
  - XML: nCharge

### Biomaterial

- s_ec_number
  - Type: string
  - XML: sECNumber
- s_pdb_identifier
  - Type: string
  - XML: sPDBIdentifier

### MulticomponentSubstance

- component
  - Type: Component[]
  - XML: Component
- composition_basis
  - Type: string
  - XML: @compositionBasis
- type
  - Type: string
  - XML: @type

### Component

- n_amount
  - Type: float
  - XML: nAmount
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- n_sample_nm
  - Type: integer
  - XML: nSampleNm

### Sample

- n_sample_nm
  - Type: integer
  - XML: nSampleNm
- component_sample
  - Type: ComponentSample[]
  - XML: ComponentSample
- e_source
  - Type: eSource, string
  - XML: eSource
- e_status
  - Type: eStatus, string
  - XML: eStatus
- purity
  - Type: Purity[]
  - XML: purity
  - Description: Purity of the sample

### Purity

- n_halide_mass_per_cent
  - Type: float
  - XML: nHalideMassPerCent
  - Description: mass per cent of halide impurity
- n_halide_mass_per_cent_digits
  - Type: integer
  - XML: nHalideMassPerCentDigits
- n_halide_mol_per_cent
  - Type: float
  - XML: nHalideMolPerCent
  - Description: mass per cent of halide impurity
- n_halide_mol_per_cent_digits
  - Type: integer
  - XML: nHalideMolPerCentDigits
- n_purity_mass
  - Type: float
  - XML: nPurityMass
  - Description: purity value in mass percent
- n_purity_mass_digits
  - Type: integer
  - XML: nPurityMassDigits
- n_purity_mol
  - Type: float
  - XML: nPurityMol
  - Description: purity value in mole percent
- n_purity_mol_digits
  - Type: integer
  - XML: nPurityMolDigits
- n_purity_vol
  - Type: float
  - XML: nPurityVol
  - Description: purity value in volume percent
- n_purity_vol_digits
  - Type: integer
  - XML: nPurityVolDigits
- n_step
  - Type: integer
  - XML: nStep
- n_unknown_per_cent
  - Type: float
  - XML: nUnknownPerCent
  - Description: purity value in not specified percent
- n_unknown_per_cent_digits
  - Type: integer
  - XML: nUnknownPerCentDigits
- n_water_mass_per_cent
  - Type: float
  - XML: nWaterMassPerCent
  - Description: mass per cent of water
- n_water_mass_per_cent_digits
  - Type: integer
  - XML: nWaterMassPerCentDigits
- n_water_mol_per_cent
  - Type: float
  - XML: nWaterMolPerCent
  - Description: mole per cent of water
- n_water_mol_per_cent_digits
  - Type: integer
  - XML: nWaterMolPerCentDigits
- e_anal_meth
  - Type: eAnalMeth, string[]
  - XML: eAnalMeth
  - Description: Analytical method used to determine purity
- e_purif_method
  - Type: ePurifMethod, string[]
  - XML: ePurifMethod
- s_anal_meth
  - Type: string[]
  - XML: sAnalMeth
- s_purif_method
  - Type: string[]
  - XML: sPurifMethod

### ComponentSample

- n_comp_index
  - Type: integer
  - XML: nCompIndex
- n_sample_nm
  - Type: integer
  - XML: nSampleNm
- reg_num
  - Type: RegNum
  - XML: RegNum

### PureOrMixtureData

- component
  - Type: Component[]
  - XML: Component
- phase_id
  - Type: PhaseID[]
  - XML: PhaseID
  - Description:  CASRN is necessary for mixtures only
- property
  - Type: Property[]
  - XML: Property
- auxiliary_substance
  - Type: AuxiliarySubstance[]
  - XML: AuxiliarySubstance
- constraint
  - Type: Constraint[]
  - XML: Constraint
- date_date_added
  - Type: string
  - XML: dateDateAdded
- e_exp_purpose
  - Type: eExpPurpose, string
  - XML: eExpPurpose
  - Description: Purpose of measurement
- equation
  - Type: Equation[]
  - XML: Equation
- n_pure_or_mixture_data_number
  - Type: integer
  - XML: nPureOrMixtureDataNumber
- num_values
  - Type: NumValues[]
  - XML: NumValues
- s_compiler
  - Type: string
  - XML: sCompiler
- s_contributor
  - Type: string
  - XML: sContributor
- variable
  - Type: Variable[]
  - XML: Variable

### AuxiliarySubstance

- e_function
  - Type: eFunction, string
  - XML: eFunction
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- s_function
  - Type: string
  - XML: sFunction
- e_phase
  - Type: ePhase, string
  - XML: ePhase
- n_sample_nm
  - Type: integer
  - XML: nSampleNm

### Property

- e_presentation
  - Type: ePresentation, string
  - XML: ePresentation
- n_pressure_digits
  - Type: integer
  - XML: nPressureDigits
- n_pressure_pa
  - Type: float
  - XML: nPressure-kPa
- n_prop_number
  - Type: integer
  - XML: nPropNumber
- n_ref_pressure
  - Type: float
  - XML: nRefPressure
- n_ref_pressure_digits
  - Type: integer
  - XML: nRefPressureDigits
- n_ref_temp
  - Type: float
  - XML: nRefTemp
- n_ref_temp_digits
  - Type: integer
  - XML: nRefTempDigits
- n_temperature_digits
  - Type: integer
  - XML: nTemperatureDigits
- n_temperature_k
  - Type: float
  - XML: nTemperature-K
- property_method_id
  - Type: PropertyMethodID
  - XML: Property-MethodID
  - Description:  CASRN is necessary for mixtures only
- catalyst
  - Type: Catalyst[]
  - XML: Catalyst
- combined_uncertainty
  - Type: CombinedUncertainty[]
  - XML: CombinedUncertainty
- curve_dev
  - Type: CurveDev[]
  - XML: CurveDev
- e_ref_state_type
  - Type: eRefStateType, string
  - XML: eRefStateType
- e_standard_state
  - Type: eStandardState, string
  - XML: eStandardState
- prop_device_spec
  - Type: PropDeviceSpec
  - XML: PropDeviceSpec
- prop_phase_id
  - Type: PropPhaseID[]
  - XML: PropPhaseID
  - Description:  CASRN is necessary for mixtures only
- prop_repeatability
  - Type: PropRepeatability
  - XML: PropRepeatability
- prop_uncertainty
  - Type: PropUncertainty[]
  - XML: PropUncertainty
- ref_phase_id
  - Type: RefPhaseID
  - XML: RefPhaseID
  - Description:  CASRN is necessary for mixtures only
- solvent
  - Type: Solvent
  - XML: Solvent

### PropertyMethodID

- n_comp_index
  - Type: integer
  - XML: nCompIndex
- property_group
  - Type: PropertyGroup
  - XML: PropertyGroup
- reg_num
  - Type: RegNum
  - XML: RegNum

### PropertyGroup

- activity_fugacity_osmotic_prop
  - Type: ActivityFugacityOsmoticProp
  - XML: ActivityFugacityOsmoticProp
- bio_properties
  - Type: BioProperties
  - XML: BioProperties
- composition_at_phase_equilibrium
  - Type: CompositionAtPhaseEquilibrium
  - XML: CompositionAtPhaseEquilibrium
- criticals
  - Type: Criticals
  - XML: Criticals
- excess_partial_apparent_energy_prop
  - Type: ExcessPartialApparentEnergyProp
  - XML: ExcessPartialApparentEnergyProp
- heat_capacity_and_derived_prop
  - Type: HeatCapacityAndDerivedProp
  - XML: HeatCapacityAndDerivedProp
- phase_transition
  - Type: PhaseTransition
  - XML: PhaseTransition
- reaction_equilibrium_prop
  - Type: ReactionEquilibriumProp
  - XML: ReactionEquilibriumProp
- reaction_state_change_prop
  - Type: ReactionStateChangeProp
  - XML: ReactionStateChangeProp
- refraction_surface_tension_sound_speed
  - Type: RefractionSurfaceTensionSoundSpeed
  - XML: RefractionSurfaceTensionSoundSpeed
- transport_prop
  - Type: TransportProp
  - XML: TransportProp
- vapor_p_boiling_t_azeotrop_tand_p
  - Type: VaporPBoilingTAzeotropTandP
  - XML: VaporPBoilingTAzeotropTandP
- volumetric_prop
  - Type: VolumetricProp
  - XML: VolumetricProp

### Criticals

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### CriticalEvaluation

- equation_of_state
  - Type: EquationOfState
  - XML: EquationOfState
- multi_prop
  - Type: MultiProp
  - XML: MultiProp
- single_prop
  - Type: SingleProp
  - XML: SingleProp

### SingleProp

- eval_single_prop_ref
  - Type: EvalSinglePropRef[]
  - XML: EvalSinglePropRef
- s_eval_single_prop_description
  - Type: string
  - XML: sEvalSinglePropDescription

### EvalSinglePropRef

- book
  - Type: Book
  - XML: book
- journal
  - Type: Journal
  - XML: journal
- thesis
  - Type: Thesis
  - XML: thesis
- date_cit
  - Type: string
  - XML: dateCit
  - Description: Date of the citation
- e_language
  - Type: eLanguage, string
  - XML: eLanguage
  - Description: Language of publication
- e_source_type
  - Type: eSourceType, string
  - XML: eSourceType
  - Description: The source status type for a citation
- e_type
  - Type: eType, string
  - XML: eType
  - Description: The type of publication
- s_abstract
  - Type: string
  - XML: sAbstract
  - Description: An abstract of the publication
- s_author
  - Type: string[]
  - XML: sAuthor
  - Description: Author of publication
- s_cas_cit
  - Type: string
  - XML: sCASCit
  - Description: The Chemical Abstracts Service citation
- s_document_origin
  - Type: string
  - XML: sDocumentOrigin
  - Description: Company, institution, or conference name
- s_doi
  - Type: string
  - XML: sDOI
  - Description: DOI
- s_id_num
  - Type: string
  - XML: sIDNum
  - Description: Identification number, e.g., a patent number or a document number
- s_keyword
  - Type: string[]
  - XML: sKeyword
- s_location
  - Type: string
  - XML: sLocation
  - Description: Reference to a location
- s_page
  - Type: string
  - XML: sPage
  - Description: Page range where the publication can be found
- s_pub_name
  - Type: string
  - XML: sPubName
  - Description: Name of the publication.
- s_title
  - Type: string
  - XML: sTitle
  - Description: Title of the publication
- s_vol
  - Type: string
  - XML: sVol
  - Description: Volume number
- trc_ref_id
  - Type: TRCRefID
  - XML: TRCRefID
- url_cit
  - Type: string
  - XML: urlCit
  - Description: URL to the publication
- yr_pub_yr
  - Type: string
  - XML: yrPubYr
  - Description: Publication year

### MultiProp

- eval_multi_prop_ref
  - Type: EvalMultiPropRef[]
  - XML: EvalMultiPropRef
- s_eval_multi_prop_description
  - Type: string
  - XML: sEvalMultiPropDescription
- s_eval_multi_prop_list
  - Type: string
  - XML: sEvalMultiPropList

### EvalMultiPropRef

- book
  - Type: Book
  - XML: book
- journal
  - Type: Journal
  - XML: journal
- thesis
  - Type: Thesis
  - XML: thesis
- date_cit
  - Type: string
  - XML: dateCit
  - Description: Date of the citation
- e_language
  - Type: eLanguage, string
  - XML: eLanguage
  - Description: Language of publication
- e_source_type
  - Type: eSourceType, string
  - XML: eSourceType
  - Description: The source status type for a citation
- e_type
  - Type: eType, string
  - XML: eType
  - Description: The type of publication
- s_abstract
  - Type: string
  - XML: sAbstract
  - Description: An abstract of the publication
- s_author
  - Type: string[]
  - XML: sAuthor
  - Description: Author of publication
- s_cas_cit
  - Type: string
  - XML: sCASCit
  - Description: The Chemical Abstracts Service citation
- s_document_origin
  - Type: string
  - XML: sDocumentOrigin
  - Description: Company, institution, or conference name
- s_doi
  - Type: string
  - XML: sDOI
  - Description: DOI
- s_id_num
  - Type: string
  - XML: sIDNum
  - Description: Identification number, e.g., a patent number or a document number
- s_keyword
  - Type: string[]
  - XML: sKeyword
- s_location
  - Type: string
  - XML: sLocation
  - Description: Reference to a location
- s_page
  - Type: string
  - XML: sPage
  - Description: Page range where the publication can be found
- s_pub_name
  - Type: string
  - XML: sPubName
  - Description: Name of the publication.
- s_title
  - Type: string
  - XML: sTitle
  - Description: Title of the publication
- s_vol
  - Type: string
  - XML: sVol
  - Description: Volume number
- trc_ref_id
  - Type: TRCRefID
  - XML: TRCRefID
- url_cit
  - Type: string
  - XML: urlCit
  - Description: URL to the publication
- yr_pub_yr
  - Type: string
  - XML: yrPubYr
  - Description: Publication year

### EquationOfState

- eval_eos_ref
  - Type: EvalEOSRef[]
  - XML: EvalEOSRef
- s_eval_eos_description
  - Type: string
  - XML: sEvalEOSDescription
- s_eval_eos_name
  - Type: string
  - XML: sEvalEOSName

### EvalEOSRef

- book
  - Type: Book
  - XML: book
- journal
  - Type: Journal
  - XML: journal
- thesis
  - Type: Thesis
  - XML: thesis
- date_cit
  - Type: string
  - XML: dateCit
  - Description: Date of the citation
- e_language
  - Type: eLanguage, string
  - XML: eLanguage
  - Description: Language of publication
- e_source_type
  - Type: eSourceType, string
  - XML: eSourceType
  - Description: The source status type for a citation
- e_type
  - Type: eType, string
  - XML: eType
  - Description: The type of publication
- s_abstract
  - Type: string
  - XML: sAbstract
  - Description: An abstract of the publication
- s_author
  - Type: string[]
  - XML: sAuthor
  - Description: Author of publication
- s_cas_cit
  - Type: string
  - XML: sCASCit
  - Description: The Chemical Abstracts Service citation
- s_document_origin
  - Type: string
  - XML: sDocumentOrigin
  - Description: Company, institution, or conference name
- s_doi
  - Type: string
  - XML: sDOI
  - Description: DOI
- s_id_num
  - Type: string
  - XML: sIDNum
  - Description: Identification number, e.g., a patent number or a document number
- s_keyword
  - Type: string[]
  - XML: sKeyword
- s_location
  - Type: string
  - XML: sLocation
  - Description: Reference to a location
- s_page
  - Type: string
  - XML: sPage
  - Description: Page range where the publication can be found
- s_pub_name
  - Type: string
  - XML: sPubName
  - Description: Name of the publication.
- s_title
  - Type: string
  - XML: sTitle
  - Description: Title of the publication
- s_vol
  - Type: string
  - XML: sVol
  - Description: Volume number
- trc_ref_id
  - Type: TRCRefID
  - XML: TRCRefID
- url_cit
  - Type: string
  - XML: urlCit
  - Description: URL to the publication
- yr_pub_yr
  - Type: string
  - XML: yrPubYr
  - Description: Publication year

### Prediction

- e_prediction_type
  - Type: ePredictionType, string
  - XML: ePredictionType
- prediction_method_ref
  - Type: PredictionMethodRef[]
  - XML: PredictionMethodRef
- s_prediction_method_description
  - Type: string
  - XML: sPredictionMethodDescription
- s_prediction_method_name
  - Type: string
  - XML: sPredictionMethodName

### PredictionMethodRef

- book
  - Type: Book
  - XML: book
- journal
  - Type: Journal
  - XML: journal
- thesis
  - Type: Thesis
  - XML: thesis
- date_cit
  - Type: string
  - XML: dateCit
  - Description: Date of the citation
- e_language
  - Type: eLanguage, string
  - XML: eLanguage
  - Description: Language of publication
- e_source_type
  - Type: eSourceType, string
  - XML: eSourceType
  - Description: The source status type for a citation
- e_type
  - Type: eType, string
  - XML: eType
  - Description: The type of publication
- s_abstract
  - Type: string
  - XML: sAbstract
  - Description: An abstract of the publication
- s_author
  - Type: string[]
  - XML: sAuthor
  - Description: Author of publication
- s_cas_cit
  - Type: string
  - XML: sCASCit
  - Description: The Chemical Abstracts Service citation
- s_document_origin
  - Type: string
  - XML: sDocumentOrigin
  - Description: Company, institution, or conference name
- s_doi
  - Type: string
  - XML: sDOI
  - Description: DOI
- s_id_num
  - Type: string
  - XML: sIDNum
  - Description: Identification number, e.g., a patent number or a document number
- s_keyword
  - Type: string[]
  - XML: sKeyword
- s_location
  - Type: string
  - XML: sLocation
  - Description: Reference to a location
- s_page
  - Type: string
  - XML: sPage
  - Description: Page range where the publication can be found
- s_pub_name
  - Type: string
  - XML: sPubName
  - Description: Name of the publication.
- s_title
  - Type: string
  - XML: sTitle
  - Description: Title of the publication
- s_vol
  - Type: string
  - XML: sVol
  - Description: Volume number
- trc_ref_id
  - Type: TRCRefID
  - XML: TRCRefID
- url_cit
  - Type: string
  - XML: urlCit
  - Description: URL to the publication
- yr_pub_yr
  - Type: string
  - XML: yrPubYr
  - Description: Publication year

### VaporPBoilingTAzeotropTandP

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### PhaseTransition

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### CompositionAtPhaseEquilibrium

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### ActivityFugacityOsmoticProp

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### VolumetricProp

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### HeatCapacityAndDerivedProp

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### ExcessPartialApparentEnergyProp

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### TransportProp

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### RefractionSurfaceTensionSoundSpeed

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### BioProperties

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string
  - XML: sMethodName

### PropPhaseID

- e_bio_state
  - Type: eBioState, string
  - XML: eBioState
- e_crystal_lattice_type
  - Type: eCrystalLatticeType, string
  - XML: eCrystalLatticeType
- e_prop_phase
  - Type: ePropPhase, string
  - XML: ePropPhase
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- s_bio_state
  - Type: string
  - XML: sBioState
- s_phase_description
  - Type: string
  - XML: sPhaseDescription

### RefPhaseID

- e_crystal_lattice_type
  - Type: eCrystalLatticeType, string
  - XML: eCrystalLatticeType
- e_ref_phase
  - Type: eRefPhase, string
  - XML: eRefPhase
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- s_phase_description
  - Type: string
  - XML: sPhaseDescription

### Solvent

- e_phase
  - Type: ePhase, string
  - XML: ePhase
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum

### CombinedUncertainty

- e_comb_uncert_eval_method
  - Type: eCombUncertEvalMethod, string
  - XML: eCombUncertEvalMethod
- n_comb_uncert_assess_num
  - Type: integer
  - XML: nCombUncertAssessNum
- asym_comb_expand_uncert
  - Type: AsymCombExpandUncert
  - XML: AsymCombExpandUncert
- asym_comb_std_uncert
  - Type: AsymCombStdUncert
  - XML: AsymCombStdUncert
- n_comb_coverage_factor
  - Type: float
  - XML: nCombCoverageFactor
- n_comb_expand_uncert_value
  - Type: float
  - XML: nCombExpandUncertValue
- n_comb_std_uncert_value
  - Type: float
  - XML: nCombStdUncertValue
- n_comb_uncert_lev_of_confid
  - Type: float
  - XML: nCombUncertLevOfConfid
- s_comb_uncert_eval_method
  - Type: string
  - XML: sCombUncertEvalMethod
- s_comb_uncert_evaluator
  - Type: string
  - XML: sCombUncertEvaluator

### PropUncertainty

- n_uncert_assess_num
  - Type: integer
  - XML: nUncertAssessNum
- asym_expand_uncert
  - Type: AsymExpandUncert
  - XML: AsymExpandUncert
- asym_std_uncert
  - Type: AsymStdUncert
  - XML: AsymStdUncert
- n_coverage_factor
  - Type: float
  - XML: nCoverageFactor
- n_expand_uncert_value
  - Type: float
  - XML: nExpandUncertValue
- n_std_uncert_value
  - Type: float
  - XML: nStdUncertValue
- n_uncert_lev_of_confid
  - Type: float
  - XML: nUncertLevOfConfid
- s_uncert_eval_method
  - Type: string
  - XML: sUncertEvalMethod
- s_uncert_evaluator
  - Type: string
  - XML: sUncertEvaluator

### PropRepeatability

- e_repeat_method
  - Type: eRepeatMethod, string
  - XML: eRepeatMethod
- n_prop_repeat_value
  - Type: float
  - XML: nPropRepeatValue
- n_repetitions
  - Type: integer
  - XML: nRepetitions
- s_repeat_evaluator
  - Type: string
  - XML: sRepeatEvaluator
- s_repeat_method
  - Type: string
  - XML: sRepeatMethod

### PropDeviceSpec

- e_device_spec_method
  - Type: eDeviceSpecMethod, string
  - XML: eDeviceSpecMethod
- n_device_spec_lev_of_confid
  - Type: float
  - XML: nDeviceSpecLevOfConfid
- s_device_spec_evaluator
  - Type: string
  - XML: sDeviceSpecEvaluator
- s_device_spec_method
  - Type: string
  - XML: sDeviceSpecMethod

### CurveDev

- n_curve_dev_assess_num
  - Type: integer
  - XML: nCurveDevAssessNum
- n_curve_dev_value
  - Type: float
  - XML: nCurveDevValue
- s_curve_spec
  - Type: string
  - XML: sCurveSpec
- n_curve_rms_dev_value
  - Type: float
  - XML: nCurveRmsDevValue
- n_curve_rms_relative_dev_value
  - Type: float
  - XML: nCurveRmsRelativeDevValue
- s_curve_dev_evaluator
  - Type: string
  - XML: sCurveDevEvaluator

### PhaseID

- e_crystal_lattice_type
  - Type: eCrystalLatticeType, string
  - XML: eCrystalLatticeType
- e_phase
  - Type: ePhase, string
  - XML: ePhase
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- s_phase_description
  - Type: string
  - XML: sPhaseDescription

### Constraint

- constraint_id
  - Type: ConstraintID
  - XML: ConstraintID
  - Description:  CASRN is necessary for mixtures only
- n_constr_digits
  - Type: integer
  - XML: nConstrDigits
- n_constraint_value
  - Type: float
  - XML: nConstraintValue
- constr_device_spec
  - Type: ConstrDeviceSpec
  - XML: ConstrDeviceSpec
- constr_repeatability
  - Type: ConstrRepeatability
  - XML: ConstrRepeatability
- constr_uncertainty
  - Type: ConstrUncertainty[]
  - XML: ConstrUncertainty
- constraint_phase_id
  - Type: ConstraintPhaseID
  - XML: ConstraintPhaseID
  - Description:  CASRN is necessary for mixtures only
- n_constraint_number
  - Type: integer
  - XML: nConstraintNumber
- solvent
  - Type: Solvent
  - XML: Solvent

### ConstraintID

- constraint_type
  - Type: ConstraintType
  - XML: ConstraintType
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum

### ConstraintType

- e_bio_variables
  - Type: eBioVariables, string
  - XML: eBioVariables
- e_component_composition
  - Type: eComponentComposition, string
  - XML: eComponentComposition
- e_miscellaneous
  - Type: eMiscellaneous, string
  - XML: eMiscellaneous
- e_participant_amount
  - Type: eParticipantAmount, string
  - XML: eParticipantAmount
- e_pressure
  - Type: ePressure, string
  - XML: ePressure
- e_solvent_composition
  - Type: eSolventComposition, string
  - XML: eSolventComposition
- e_temperature
  - Type: eTemperature, string
  - XML: eTemperature

### ConstraintPhaseID

- e_constraint_phase
  - Type: eConstraintPhase, string
  - XML: eConstraintPhase
- e_crystal_lattice_type
  - Type: eCrystalLatticeType, string
  - XML: eCrystalLatticeType
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- s_phase_description
  - Type: string
  - XML: sPhaseDescription

### ConstrUncertainty

- n_coverage_factor
  - Type: float
  - XML: nCoverageFactor
- n_expand_uncert_value
  - Type: float
  - XML: nExpandUncertValue
- n_std_uncert_value
  - Type: float
  - XML: nStdUncertValue
- n_uncert_lev_of_confid
  - Type: float
  - XML: nUncertLevOfConfid
- s_uncert_eval_method
  - Type: string
  - XML: sUncertEvalMethod
- s_uncert_evaluator
  - Type: string
  - XML: sUncertEvaluator

### ConstrRepeatability

- e_repeat_method
  - Type: eRepeatMethod, string
  - XML: eRepeatMethod
- n_repeat_value
  - Type: float
  - XML: nRepeatValue
- n_repetitions
  - Type: integer
  - XML: nRepetitions
- s_repeat_evaluator
  - Type: string
  - XML: sRepeatEvaluator
- s_repeat_method
  - Type: string
  - XML: sRepeatMethod

### ConstrDeviceSpec

- e_device_spec_method
  - Type: eDeviceSpecMethod, string
  - XML: eDeviceSpecMethod
- n_device_spec_lev_of_confid
  - Type: float
  - XML: nDeviceSpecLevOfConfid
- n_device_spec_value
  - Type: float
  - XML: nDeviceSpecValue
- s_device_spec_evaluator
  - Type: string
  - XML: sDeviceSpecEvaluator
- s_device_spec_method
  - Type: string
  - XML: sDeviceSpecMethod

### Variable

- n_var_number
  - Type: integer
  - XML: nVarNumber
- variable_id
  - Type: VariableID
  - XML: VariableID
  - Description:  CASRN is necessary for mixtures only
- solvent
  - Type: Solvent
  - XML: Solvent
- var_device_spec
  - Type: VarDeviceSpec
  - XML: VarDeviceSpec
- var_phase_id
  - Type: VarPhaseID
  - XML: VarPhaseID
  - Description:  CASRN is necessary for mixtures only
- var_repeatability
  - Type: VarRepeatability
  - XML: VarRepeatability
- var_uncertainty
  - Type: VarUncertainty[]
  - XML: VarUncertainty

### VariableID

- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- variable_type
  - Type: VariableType
  - XML: VariableType

### VariableType

- e_bio_variables
  - Type: eBioVariables, string
  - XML: eBioVariables
- e_component_composition
  - Type: eComponentComposition, string
  - XML: eComponentComposition
- e_miscellaneous
  - Type: eMiscellaneous, string
  - XML: eMiscellaneous
- e_participant_amount
  - Type: eParticipantAmount, string
  - XML: eParticipantAmount
- e_pressure
  - Type: ePressure, string
  - XML: ePressure
- e_solvent_composition
  - Type: eSolventComposition, string
  - XML: eSolventComposition
- e_temperature
  - Type: eTemperature, string
  - XML: eTemperature

### VarPhaseID

- e_crystal_lattice_type
  - Type: eCrystalLatticeType, string
  - XML: eCrystalLatticeType
- e_var_phase
  - Type: eVarPhase, string
  - XML: eVarPhase
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- s_phase_description
  - Type: string
  - XML: sPhaseDescription

### VarUncertainty

- n_uncert_assess_num
  - Type: integer
  - XML: nUncertAssessNum
- n_coverage_factor
  - Type: float
  - XML: nCoverageFactor
- n_expand_uncert_value
  - Type: float
  - XML: nExpandUncertValue
- n_std_uncert_value
  - Type: float
  - XML: nStdUncertValue
- n_uncert_lev_of_confid
  - Type: float
  - XML: nUncertLevOfConfid
- s_uncert_eval_method
  - Type: string
  - XML: sUncertEvalMethod
- s_uncert_evaluator
  - Type: string
  - XML: sUncertEvaluator

### VarRepeatability

- e_repeat_method
  - Type: eRepeatMethod, string
  - XML: eRepeatMethod
- n_repetitions
  - Type: integer
  - XML: nRepetitions
- n_var_repeat_value
  - Type: float
  - XML: nVarRepeatValue
- s_repeat_evaluator
  - Type: string
  - XML: sRepeatEvaluator
- s_repeat_method
  - Type: string
  - XML: sRepeatMethod

### VarDeviceSpec

- e_device_spec_method
  - Type: eDeviceSpecMethod, string
  - XML: eDeviceSpecMethod
- n_device_spec_lev_of_confid
  - Type: float
  - XML: nDeviceSpecLevOfConfid
- s_device_spec_evaluator
  - Type: string
  - XML: sDeviceSpecEvaluator
- s_device_spec_method
  - Type: string
  - XML: sDeviceSpecMethod

### NumValues

- property_value
  - Type: PropertyValue[]
  - XML: PropertyValue
- variable_value
  - Type: VariableValue[]
  - XML: VariableValue

### VariableValue

- n_var_digits
  - Type: integer
  - XML: nVarDigits
- n_var_number
  - Type: integer
  - XML: nVarNumber
- n_var_value
  - Type: float
  - XML: nVarValue
- n_var_device_spec_value
  - Type: float
  - XML: nVarDeviceSpecValue
- var_repeatability
  - Type: VarRepeatability
  - XML: VarRepeatability
- var_uncertainty
  - Type: VarUncertainty[]
  - XML: VarUncertainty

### PropertyValue

- n_prop_digits
  - Type: integer
  - XML: nPropDigits
- n_prop_number
  - Type: integer
  - XML: nPropNumber
- n_prop_value
  - Type: float
  - XML: nPropValue
- prop_limit
  - Type: PropLimit
  - XML: PropLimit
- combined_uncertainty
  - Type: CombinedUncertainty[]
  - XML: CombinedUncertainty
- curve_dev
  - Type: CurveDev[]
  - XML: CurveDev
- n_prop_device_spec_value
  - Type: float
  - XML: nPropDeviceSpecValue
- prop_repeatability
  - Type: PropRepeatability
  - XML: PropRepeatability
- prop_uncertainty
  - Type: PropUncertainty[]
  - XML: PropUncertainty

### PropLimit

- n_prop_limit_digits
  - Type: integer
  - XML: nPropLimitDigits
- n_prop_lower_limit_value
  - Type: float
  - XML: nPropLowerLimitValue
- n_prop_upper_limit_value
  - Type: float
  - XML: nPropUpperLimitValue

### AsymCombStdUncert

- n_negative_value
  - Type: float
  - XML: nNegativeValue
- n_positive_value
  - Type: float
  - XML: nPositiveValue

### AsymCombExpandUncert

- n_negative_value
  - Type: float
  - XML: nNegativeValue
- n_positive_value
  - Type: float
  - XML: nPositiveValue

### AsymStdUncert

- n_negative_value
  - Type: float
  - XML: nNegativeValue
- n_positive_value
  - Type: float
  - XML: nPositiveValue

### AsymExpandUncert

- n_negative_value
  - Type: float
  - XML: nNegativeValue
- n_positive_value
  - Type: float
  - XML: nPositiveValue

### Equation

- e_eq_name
  - Type: eEqName, string
  - XML: eEqName
- s_eq_name
  - Type: string
  - XML: sEqName
- url_math_source
  - Type: string
  - XML: urlMathSource
- covariance
  - Type: Covariance[]
  - XML: Covariance
- eq_constant
  - Type: EqConstant[]
  - XML: EqConstant
- eq_constraint
  - Type: EqConstraint[]
  - XML: EqConstraint
- eq_parameter
  - Type: EqParameter[]
  - XML: EqParameter
- eq_property
  - Type: EqProperty[]
  - XML: EqProperty
- eq_variable
  - Type: EqVariable[]
  - XML: EqVariable
- n_covariance_lev_of_confid
  - Type: float
  - XML: nCovarianceLevOfConfid

### EqProperty

- n_prop_number
  - Type: integer
  - XML: nPropNumber
- n_pure_or_mixture_data_number
  - Type: integer
  - XML: nPureOrMixtureDataNumber
- n_reaction_data_number
  - Type: integer
  - XML: nReactionDataNumber
- s_eq_symbol
  - Type: string
  - XML: sEqSymbol
- n_eq_prop_index
  - Type: integer[]
  - XML: nEqPropIndex
- n_eq_prop_range_max
  - Type: float
  - XML: nEqPropRangeMax
- n_eq_prop_range_min
  - Type: float
  - XML: nEqPropRangeMin
- s_other_prop_unit
  - Type: string
  - XML: sOtherPropUnit

### EqConstraint

- n_constraint_number
  - Type: integer
  - XML: nConstraintNumber
- n_pure_or_mixture_data_number
  - Type: integer
  - XML: nPureOrMixtureDataNumber
- n_reaction_data_number
  - Type: integer
  - XML: nReactionDataNumber
- s_eq_symbol
  - Type: string
  - XML: sEqSymbol
- n_eq_constraint_index
  - Type: integer[]
  - XML: nEqConstraintIndex
- n_eq_constraint_range_max
  - Type: float
  - XML: nEqConstraintRangeMax
- n_eq_constraint_range_min
  - Type: float
  - XML: nEqConstraintRangeMin
- s_other_constraint_unit
  - Type: string
  - XML: sOtherConstraintUnit

### EqVariable

- n_pure_or_mixture_data_number
  - Type: integer
  - XML: nPureOrMixtureDataNumber
- n_reaction_data_number
  - Type: integer
  - XML: nReactionDataNumber
- n_var_number
  - Type: integer
  - XML: nVarNumber
- s_eq_symbol
  - Type: string
  - XML: sEqSymbol
- n_eq_var_index
  - Type: integer[]
  - XML: nEqVarIndex
- n_eq_var_range_max
  - Type: float
  - XML: nEqVarRangeMax
- n_eq_var_range_min
  - Type: float
  - XML: nEqVarRangeMin
- s_other_var_unit
  - Type: string
  - XML: sOtherVarUnit

### EqParameter

- n_eq_par_digits
  - Type: integer
  - XML: nEqParDigits
- n_eq_par_value
  - Type: float
  - XML: nEqParValue
- s_eq_par_symbol
  - Type: string
  - XML: sEqParSymbol
- n_eq_par_index
  - Type: integer[]
  - XML: nEqParIndex
- n_eq_par_number
  - Type: integer
  - XML: nEqParNumber

### EqConstant

- n_eq_constant_digits
  - Type: integer
  - XML: nEqConstantDigits
- n_eq_constant_value
  - Type: float
  - XML: nEqConstantValue
- s_eq_constant_symbol
  - Type: string
  - XML: sEqConstantSymbol
- n_eq_constant_index
  - Type: integer[]
  - XML: nEqConstantIndex

### Covariance

- n_covariance_value
  - Type: float
  - XML: nCovarianceValue
- n_eq_par_number1
  - Type: integer
  - XML: nEqParNumber1
- n_eq_par_number2
  - Type: integer
  - XML: nEqParNumber2

### ReactionData

- e_reaction_type
  - Type: eReactionType, string
  - XML: eReactionType
- participant
  - Type: Participant[]
  - XML: Participant
- property
  - Type: Property[]
  - XML: Property
- auxiliary_substance
  - Type: AuxiliarySubstance[]
  - XML: AuxiliarySubstance
- constraint
  - Type: Constraint[]
  - XML: Constraint
- date_date_added
  - Type: string
  - XML: dateDateAdded
- e_exp_purpose
  - Type: eExpPurpose, string
  - XML: eExpPurpose
  - Description: Purpose of measurement
- e_reaction_formalism
  - Type: eReactionFormalism, string
  - XML: eReactionFormalism
- equation
  - Type: Equation[]
  - XML: Equation
- n_electron_number
  - Type: integer
  - XML: nElectronNumber
- n_reaction_data_number
  - Type: integer
  - XML: nReactionDataNumber
- num_values
  - Type: NumValues[]
  - XML: NumValues
- s_compiler
  - Type: string
  - XML: sCompiler
- s_contributor
  - Type: string
  - XML: sContributor
- solvent
  - Type: Solvent[]
  - XML: Solvent
- variable
  - Type: Variable[]
  - XML: Variable

### Participant

- e_crystal_lattice_type
  - Type: eCrystalLatticeType, string
  - XML: eCrystalLatticeType
- e_phase
  - Type: ePhase, string
  - XML: ePhase
- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- s_phase_description
  - Type: string
  - XML: sPhaseDescription
- e_composition_representation
  - Type: eCompositionRepresentation, string
  - XML: eCompositionRepresentation
- e_standard_state
  - Type: eStandardState, string
  - XML: eStandardState
- n_numerical_composition
  - Type: float
  - XML: nNumericalComposition
- n_sample_nm
  - Type: integer
  - XML: nSampleNm
- n_stoichiometric_coef
  - Type: float
  - XML: nStoichiometricCoef

### ReactionStateChangeProp

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string[]
  - XML: sMethodName

### ReactionEquilibriumProp

- critical_evaluation
  - Type: CriticalEvaluation
  - XML: CriticalEvaluation
- e_method_name
  - Type: eMethodName, string
  - XML: eMethodName
- e_prop_name
  - Type: ePropName, string
  - XML: ePropName
- prediction
  - Type: Prediction
  - XML: Prediction
- s_method_name
  - Type: string[]
  - XML: sMethodName

### Catalyst

- n_comp_index
  - Type: integer
  - XML: nCompIndex
- reg_num
  - Type: RegNum
  - XML: RegNum
- e_phase
  - Type: ePhase, string
  - XML: ePhase

## Enumerations

### eType

```python
BOOK = 'book'
JOURNAL = 'journal'
REPORT = 'report'
PATENT = 'patent'
THESIS = 'thesis'
CONFERENCEPROCEEDINGS = 'conferenceProceedings'
ARCHIVEDDOCUMENT = 'archivedDocument'
PERSONALCORRESPONDENCE = 'personalCorrespondence'
PUBLISHEDTRANSLATION = 'publishedTranslation'
UNSPECIFIED = 'unspecified'
```

### eSourceType

```python
ORIGINAL = 'Original'
CHEMICALABSTRACTS = 'ChemicalAbstracts'
OTHER = 'Other'
```

### eLanguage

```python
CHINESE = 'Chinese'
ENGLISH = 'English'
FRENCH = 'French'
GERMAN = 'German'
JAPANESE = 'Japanese'
POLISH = 'Polish'
RUSSIAN = 'Russian'
OTHER_LANGUAGE = 'Other language'
```

### eSpeciationState

```python
EQUILIBRIUM = 'equilibrium'
SINGLE_SPECIES = 'single species'
```

### eSource

```python
COMMERCIAL_SOURCE = 'Commercial source'
SYNTHESIZED_BY_THE_AUTHORS = 'Synthesized by the authors'
SYNTHESIZED_BY_OTHERS = 'Synthesized by others'
STANDARD_REFERENCE_MATERIAL_SRM = 'Standard Reference Material (SRM)'
ISOLATED_FROM_A_NATURAL_PRODUCT = 'Isolated from a natural product'
NOT_STATED_IN_THE_DOCUMENT = 'Not stated in the document'
NO_SAMPLE_USED = 'No sample used'
```

### eStatus

```python
UNKNOWN = 'unknown'
NOTDESCRIBED = 'notDescribed'
PREVIOUSPAPER = 'previousPaper'
NOSAMPLE = 'noSample'
```

### ePurifMethod

```python
IMPURITY_ADSORPTION = 'Impurity adsorption'
VACUUM_DEGASIFICATION = 'Vacuum degasification'
CHEMICAL_REAGENT_TREATMENT = 'Chemical reagent treatment'
CRYSTALLIZATION_FROM_MELT = 'Crystallization from melt'
CRYSTALLIZATION_FROM_SOLUTION = 'Crystallization from solution'
LIQUID_CHROMATOGRAPHY = 'Liquid chromatography'
DRIED_WITH_CHEMICAL_REAGENT = 'Dried with chemical reagent'
DRIED_IN_A_DESICCATOR = 'Dried in a desiccator'
DRIED_BY_OVEN_HEATING = 'Dried by oven heating'
DRIED_BY_VACUUM_HEATING = 'Dried by vacuum heating'
DEGASSED_BY_BOILING_OR_ULTRASONICALLY = 'De-gassed by boiling or ultrasonically'
DEGASSED_BY_EVACUATION = 'De-gassed by evacuation'
DEGASSED_BY_FREEZING_AND_MELTING_IN_VACUUM = 'De-gassed by freezing and melting in vacuum'
FRACTIONAL_CRYSTALLIZATION = 'Fractional crystallization'
FRACTIONAL_DISTILLATION = 'Fractional distillation'
MOLECULAR_SIEVE_TREATMENT = 'Molecular sieve treatment'
UNSPECIFIED = 'Unspecified'
PREPARATIVE_GAS_CHROMATOGRAPHY = 'Preparative gas chromatography'
SUBLIMATION = 'Sublimation'
STEAM_DISTILLATION = 'Steam distillation'
SOLVENT_EXTRACTION = 'Solvent extraction'
SALTING_OUT_OF_SOLUTION = 'Salting out of solution'
ZONE_REFINING = 'Zone refining'
OTHER = 'Other'
NONE_USED = 'None used'
```

### eAnalMeth

```python
CHEMICAL_ANALYSIS = 'Chemical analysis'
DIFFERENCE_BETWEEN_BUBBLE_AND_DEW_TEMPERATURES = 'Difference between bubble and dew temperatures'
DENSITY = 'Density'
DSC = 'DSC'
ESTIMATION = 'Estimation'
GAS_CHROMATOGRAPHY = 'Gas chromatography'
FRACTION_MELTING_IN_AN_ADIABATIC_CALORIMETER = 'Fraction melting in an adiabatic calorimeter'
MASS_SPECTROMETRY = 'Mass spectrometry'
NMR_PROTON = 'NMR (proton)'
NMR_OTHER = 'NMR (other)'
NOT_KNOWN = 'Not known'
SPECTROSCOPY = 'Spectroscopy'
THERMAL_ANALYSIS_USING_TEMPERATURETIME_MEASUREMENT = 'Thermal analysis using temperature-time measurement'
ACIDBASE_TITRATION = 'Acid-base titration'
OTHER_TYPES_OF_TITRATION = 'Other types of titration'
MASS_LOSS_ON_DRYING = 'Mass loss on drying'
KARL_FISCHER_TITRATION = 'Karl Fischer titration'
HPLC = 'HPLC'
ION_CHROMATOGRAPHY = 'Ion chromatography'
IONSELECTIVE_ELECTRODE = 'Ion-selective electrode'
CO2_YIELD_IN_COMBUSTION_PRODUCTS = 'CO2 yield in combustion products'
OTHER = 'Other'
ESTIMATED_BY_THE_COMPILER = 'Estimated by the compiler'
STATED_BY_SUPPLIER = 'Stated by supplier'
```

### eFunction

```python
COFACTOR = 'Cofactor'
BUFFER = 'Buffer'
INERT = 'Inert'
```

### eExpPurpose

```python
PRINCIPAL_OBJECTIVE_OF_THE_WORK = 'Principal objective of the work'
SECONDARY_PURPOSE_BYPRODUCT_OF_OTHER_OBJECTIVE = 'Secondary purpose (by-product of other objective)'
DETERMINED_FOR_IDENTIFICATION_OF_A_SYNTHESIZED_COMPOUND = 'Determined for identification of a synthesized compound'
```

### ePropName

```python
THERMODYNAMIC_EQUILIBRIUM_CONSTANT = 'Thermodynamic equilibrium constant'
EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLALITY_MOLKGN = 'Equilibrium constant in terms of molality, (mol/kg)^n'
EQUILIBRIUM_CONSTANT_IN_TERMS_OF_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3N = 'Equilibrium constant in terms of amount concentration (molarity), (mol/dm3)^n'
EQUILIBRIUM_CONSTANT_IN_TERMS_OF_PARTIAL_PRESSURE_KPAN = 'Equilibrium constant in terms of partial pressure, kPa^n'
EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLE_FRACTION = 'Equilibrium constant in terms of mole fraction'
NATURAL_LOGARITHM_OF_THERMODYNAMIC_EQUILIBRIUM_CONSTANT = 'Natural logarithm of thermodynamic equilibrium constant'
NATURAL_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLALITY_MOLKGN = 'Natural logarithm of equilibrium constant in terms of molality, (mol/kg)^n'
NATURAL_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3N = 'Natural logarithm of equilibrium constant in terms of amount concentration (molarity), (mol/dm3)^n'
NATURAL_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_PARTIAL_PRESSURE_KPAN = 'Natural logarithm of equilibrium constant in terms of partial pressure, kPa^n'
NATURAL_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLE_FRACTION = 'Natural logarithm of equilibrium constant in terms of mole fraction'
DECADIC_LOGARITHM_OF_THERMODYNAMIC_EQUILIBRIUM_CONSTANT = 'Decadic logarithm of thermodynamic equilibrium constant'
DECADIC_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLALITY_MOLKGN = 'Decadic logarithm of equilibrium constant in terms of molality, (mol/kg)^n'
DECADIC_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3N = 'Decadic logarithm of equilibrium constant in terms of amount concentration (molarity), (mol/dm3)^n'
DECADIC_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_PARTIAL_PRESSURE_KPAN = 'Decadic logarithm of equilibrium constant in terms of partial pressure, kPa^n'
DECADIC_LOGARITHM_OF_EQUILIBRIUM_CONSTANT_IN_TERMS_OF_MOLE_FRACTION = 'Decadic logarithm of equilibrium constant in terms of mole fraction'
```

### eMethodName

```python
STATIC_EQUILIBRATION = 'Static equilibration'
DYNAMIC_EQUILIBRATION = 'Dynamic equilibration'
CHROMATOGRAPHY = 'Chromatography'
IR_SPECTROMETRY = 'IR spectrometry'
UV_SPECTROSCOPY = 'UV spectroscopy'
NMR_SPECTROMETRY = 'NMR spectrometry'
TITRATION = 'Titration'
POTENTIAL_DIFFERENCE_OF_AN_ELECTROCHEMICAL_CELL = 'Potential difference of an electrochemical cell'
ANION_EXCHANGE = 'Anion exchange'
CATION_EXCHANGE = 'Cation exchange'
CELL_POTENTIAL_WITH_GLASS_ELECTRODE = 'Cell potential with glass electrode'
CELL_POTENTIAL_WITH_PLATINUM_ELECTRODE = 'Cell potential with platinum electrode'
CELL_POTENTIAL_WITH_QUINHYDRONE_ELECTRODE = 'Cell potential with quinhydrone electrode'
CELL_POTENTIAL_WITH_REDOX_ELECTRODE = 'Cell potential with redox electrode'
COLORIMETRY = 'Colorimetry'
CONDUCTIVITY_MEASUREMENT = 'Conductivity measurement'
COULOMETRY = 'Coulometry'
CRYOSCOPY = 'Cryoscopy'
DISTRIBUTION_BETWEEN_TWO_PHASES = 'Distribution between two phases'
ION_SELECTIVE_ELECTRODE = 'Ion selective electrode'
MOLAR_VOLUME_DETERMINATION = 'Molar volume determination'
POLAROGRAPHY = 'Polarography'
POTENTIOMETRY = 'Potentiometry'
PROTON_RELAXATION = 'Proton relaxation'
RATE_OF_REACTION = 'Rate of reaction'
SOLUBILITY_MEASUREMENT = 'Solubility measurement'
SPECTROPHOTOMETRY = 'Spectrophotometry'
THERMAL_LENSING_SPECTROPHOTOMETRY = 'Thermal lensing spectrophotometry'
TRANSIENT_CONDUCTIVITY_MEASUREMENT = 'Transient conductivity measurement'
SOLVENT_EXTRACTION = 'Solvent extraction'
VOLTAMMETRY = 'Voltammetry'
OTHER = 'Other'
```

### ePredictionType

```python
AB_INITIO = 'Ab initio'
MOLECULAR_DYNAMICS = 'Molecular dynamics'
SEMIEMPIRICAL_QUANTUM_METHODS = 'Semiempirical quantum methods'
MOLECULAR_MECHANICS = 'Molecular mechanics'
STATISTICAL_MECHANICS = 'Statistical mechanics'
CORRESPONDING_STATES = 'Corresponding states'
CORRELATION = 'Correlation'
GROUP_CONTRIBUTION = 'Group contribution'
```

### ePropPhase

```python
CRYSTAL_5 = 'Crystal 5'
CRYSTAL_4 = 'Crystal 4'
CRYSTAL_3 = 'Crystal 3'
CRYSTAL_2 = 'Crystal 2'
CRYSTAL_1 = 'Crystal 1'
CRYSTAL = 'Crystal'
CRYSTAL_OF_UNKNOWN_TYPE = 'Crystal of unknown type'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1 = 'Crystal of intercomponent compound 1'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2 = 'Crystal of intercomponent compound 2'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3 = 'Crystal of intercomponent compound 3'
METASTABLE_CRYSTAL = 'Metastable crystal'
GLASS = 'Glass'
SMECTIC_LIQUID_CRYSTAL = 'Smectic liquid crystal'
SMECTIC_LIQUID_CRYSTAL_1 = 'Smectic liquid crystal 1'
SMECTIC_LIQUID_CRYSTAL_2 = 'Smectic liquid crystal 2'
NEMATIC_LIQUID_CRYSTAL = 'Nematic liquid crystal'
NEMATIC_LIQUID_CRYSTAL_1 = 'Nematic liquid crystal 1'
NEMATIC_LIQUID_CRYSTAL_2 = 'Nematic liquid crystal 2'
CHOLESTERIC_LIQUID_CRYSTAL = 'Cholesteric liquid crystal'
LIQUID_CRYSTAL_OF_UNKNOWN_TYPE = 'Liquid crystal of unknown type'
LIQUID = 'Liquid'
LIQUID_MIXTURE_1 = 'Liquid mixture 1'
LIQUID_MIXTURE_2 = 'Liquid mixture 2'
LIQUID_MIXTURE_3 = 'Liquid mixture 3'
SOLUTION = 'Solution'
SOLUTION_1 = 'Solution 1'
SOLUTION_2 = 'Solution 2'
SOLUTION_3 = 'Solution 3'
SOLUTION_4 = 'Solution 4'
FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES = 'Fluid (supercritical or subcritical phases)'
IDEAL_GAS = 'Ideal gas'
GAS = 'Gas'
AIR_AT_1_ATMOSPHERE = 'Air at 1 atmosphere'
```

### eCrystalLatticeType

```python
CUBIC = 'Cubic'
TETRAGONAL = 'Tetragonal'
HEXAGONAL = 'Hexagonal'
RHOMBOHEDRAL = 'Rhombohedral'
ORTHORHOMBIC = 'Orthorhombic'
MONOCLINIC = 'Monoclinic'
TRICLINIC = 'Triclinic'
```

### eBioState

```python
NATIVE = 'Native'
DENATURATED = 'Denaturated'
```

### ePresentation

```python
DIRECT_VALUE_X = 'Direct value, X'
DIFFERENCE_BETWEEN_UPPER_AND_LOWER_TEMPERATURE_XT2XT1 = 'Difference between upper and lower temperature, X(T2)-X(T1)'
DIFFERENCE_BETWEEN_UPPER_AND_LOWER_PRESSURE_XP2XP1 = 'Difference between upper and lower pressure, X(P2)-X(P1)'
MEAN_BETWEEN_UPPER_AND_LOWER_TEMPERATURE_XT2XT12 = 'Mean between upper and lower temperature, [X(T2)+X(T1)]/2'
DIFFERENCE_WITH_THE_REFERENCE_STATE_XXREF = 'Difference with the reference state, X-X(REF)'
RATIO_WITH_THE_REFERENCE_STATE_XXREF = 'Ratio with the reference state, X/X(REF)'
RATIO_OF_DIFFERENCE_WITH_THE_REFERENCE_STATE_TO_THE_REFERENCE_STATE_XXREFXREF = 'Ratio of difference with the reference state to the reference state, [X-X(REF)]/X(REF)'
```

### eRefStateType

```python
REFERENCE_PHASE_WITH_THE_SAME_COMPOSITION_AT_FIXED_TEMPERATURE_AND_PRESSURE = 'Reference phase with the same composition at fixed temperature and pressure'
REFERENCE_PHASE_WITH_THE_SAME_COMPOSITION_TEMPERATURE_AND_PRESSURE = 'Reference phase with the same composition, temperature and pressure'
REFERENCE_PHASE_AT_FIXED_TEMPERATURE_AND_THE_SAME_PRESSURE = 'Reference phase at fixed temperature and the same pressure'
REFERENCE_PHASE_AT_THE_SAME_TEMPERATURE_AND_FIXED_PRESSURE = 'Reference phase at the same temperature and fixed pressure'
IDEAL_GAS_AT_THE_SAME_AMOUNT_DENSITY_TEMPERATURE_AND_COMPOSITION = 'Ideal gas at the same amount density, temperature, and composition'
IDEAL_MIXTURE_OF_PURE_FLUID_COMPONENTS_AT_THE_SAME_AMOUNT_DENSITY_TEMPERATURE_AND_COMPOSITION = 'Ideal mixture of pure fluid components at the same amount density, temperature, and composition'
PHASE_IN_EQUILIBRIUM_WITH_PRIMARY_PHASE_AT_THE_SAME_TEMPERATURE_AND_PRESSURE = 'Phase in equilibrium with primary phase at the same temperature and pressure'
PURE_COMPONENTS_IN_THE_SAME_PROPORTION_AT_FIXED_TEMPERATURE_AND_PRESSURE = 'Pure components in the same proportion at fixed temperature and pressure'
PURE_COMPONENTS_IN_THE_SAME_PROPORTION_AT_THE_SAME_TEMPERATURE_AND_PRESSURE = 'Pure components in the same proportion at the same temperature and pressure'
PURE_SOLVENT_AT_THE_TEMPERATURE_OF_THE_SAME_PHASE_EQUILIBRIUM = 'Pure solvent at the temperature of the same phase equilibrium'
PURE_SOLVENT_AT_THE_SAME_TEMPERATURE_AND_PRESSURE = 'Pure solvent at the same temperature and pressure'
PURE_SOLUTE_AT_THE_SAME_TEMPERATURE_AND_PRESSURE = 'Pure solute at the same temperature and pressure'
```

### eRefPhase

```python
CRYSTAL_5 = 'Crystal 5'
CRYSTAL_4 = 'Crystal 4'
CRYSTAL_3 = 'Crystal 3'
CRYSTAL_2 = 'Crystal 2'
CRYSTAL_1 = 'Crystal 1'
CRYSTAL = 'Crystal'
CRYSTAL_OF_UNKNOWN_TYPE = 'Crystal of unknown type'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1 = 'Crystal of intercomponent compound 1'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2 = 'Crystal of intercomponent compound 2'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3 = 'Crystal of intercomponent compound 3'
METASTABLE_CRYSTAL = 'Metastable crystal'
GLASS = 'Glass'
SMECTIC_LIQUID_CRYSTAL = 'Smectic liquid crystal'
SMECTIC_LIQUID_CRYSTAL_1 = 'Smectic liquid crystal 1'
SMECTIC_LIQUID_CRYSTAL_2 = 'Smectic liquid crystal 2'
NEMATIC_LIQUID_CRYSTAL = 'Nematic liquid crystal'
NEMATIC_LIQUID_CRYSTAL_1 = 'Nematic liquid crystal 1'
NEMATIC_LIQUID_CRYSTAL_2 = 'Nematic liquid crystal 2'
CHOLESTERIC_LIQUID_CRYSTAL = 'Cholesteric liquid crystal'
LIQUID_CRYSTAL_OF_UNKNOWN_TYPE = 'Liquid crystal of unknown type'
LIQUID = 'Liquid'
LIQUID_MIXTURE_1 = 'Liquid mixture 1'
LIQUID_MIXTURE_2 = 'Liquid mixture 2'
LIQUID_MIXTURE_3 = 'Liquid mixture 3'
SOLUTION = 'Solution'
SOLUTION_1 = 'Solution 1'
SOLUTION_2 = 'Solution 2'
SOLUTION_3 = 'Solution 3'
SOLUTION_4 = 'Solution 4'
FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES = 'Fluid (supercritical or subcritical phases)'
IDEAL_GAS = 'Ideal gas'
GAS = 'Gas'
AIR_AT_1_ATMOSPHERE = 'Air at 1 atmosphere'
```

### eStandardState

```python
PURE_COMPOUND = 'Pure compound'
PURE_LIQUID_SOLUTE = 'Pure liquid solute'
STANDARD_MOLALITY_1_MOLKG_SOLUTE = 'Standard molality (1 mol/kg) solute'
STANDARD_AMOUNT_CONCENTRATION_1_MOLDM3_SOLUTE = 'Standard amount concentration (1 mol/dm3) solute'
INFINITE_DILUTION_SOLUTE = 'Infinite dilution solute'
```

### eCombUncertEvalMethod

```python
PROPAGATION_OF_EVALUATED_STANDARD_UNCERTAINTIES = 'Propagation of evaluated standard uncertainties'
COMPARISON_WITH_REFERENCE_PROPERTY_VALUES = 'Comparison with reference property values'
```

### eRepeatMethod

```python
STANDARD_DEVIATION_OF_A_SINGLE_VALUE_BIASED = 'Standard deviation of a single value (biased)'
STANDARD_DEVIATION_OF_A_SINGLE_VALUE_UNBIASED = 'Standard deviation of a single value (unbiased)'
STANDARD_DEVIATION_OF_THE_MEAN = 'Standard deviation of the mean'
OTHER = 'Other'
```

### eDeviceSpecMethod

```python
SPECIFIED_BY_THE_MANUFACTURER = 'Specified by the manufacturer'
CERTIFIED_OR_CALIBRATED_BY_A_THIRD_PARTY = 'Certified or calibrated by a third party'
CALIBRATED_BY_THE_EXPERIMENTALIST = 'Calibrated by the experimentalist'
```

### ePhase

```python
CRYSTAL_5 = 'Crystal 5'
CRYSTAL_4 = 'Crystal 4'
CRYSTAL_3 = 'Crystal 3'
CRYSTAL_2 = 'Crystal 2'
CRYSTAL_1 = 'Crystal 1'
CRYSTAL = 'Crystal'
CRYSTAL_OF_UNKNOWN_TYPE = 'Crystal of unknown type'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1 = 'Crystal of intercomponent compound 1'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2 = 'Crystal of intercomponent compound 2'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3 = 'Crystal of intercomponent compound 3'
METASTABLE_CRYSTAL = 'Metastable crystal'
GLASS = 'Glass'
SMECTIC_LIQUID_CRYSTAL = 'Smectic liquid crystal'
SMECTIC_LIQUID_CRYSTAL_1 = 'Smectic liquid crystal 1'
SMECTIC_LIQUID_CRYSTAL_2 = 'Smectic liquid crystal 2'
NEMATIC_LIQUID_CRYSTAL = 'Nematic liquid crystal'
NEMATIC_LIQUID_CRYSTAL_1 = 'Nematic liquid crystal 1'
NEMATIC_LIQUID_CRYSTAL_2 = 'Nematic liquid crystal 2'
CHOLESTERIC_LIQUID_CRYSTAL = 'Cholesteric liquid crystal'
LIQUID_CRYSTAL_OF_UNKNOWN_TYPE = 'Liquid crystal of unknown type'
LIQUID = 'Liquid'
LIQUID_MIXTURE_1 = 'Liquid mixture 1'
LIQUID_MIXTURE_2 = 'Liquid mixture 2'
LIQUID_MIXTURE_3 = 'Liquid mixture 3'
SOLUTION = 'Solution'
SOLUTION_1 = 'Solution 1'
SOLUTION_2 = 'Solution 2'
SOLUTION_3 = 'Solution 3'
SOLUTION_4 = 'Solution 4'
FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES = 'Fluid (supercritical or subcritical phases)'
IDEAL_GAS = 'Ideal gas'
GAS = 'Gas'
AIR_AT_1_ATMOSPHERE = 'Air at 1 atmosphere'
```

### eTemperature

```python
TEMPERATURE_K = 'Temperature, K'
UPPER_TEMPERATURE_K = 'Upper temperature, K'
LOWER_TEMPERATURE_K = 'Lower temperature, K'
```

### ePressure

```python
PRESSURE_KPA = 'Pressure, kPa'
PARTIAL_PRESSURE_KPA = 'Partial pressure, kPa'
UPPER_PRESSURE_KPA = 'Upper pressure, kPa'
LOWER_PRESSURE_KPA = 'Lower pressure, kPa'
```

### eComponentComposition

```python
MOLE_FRACTION = 'Mole fraction'
MASS_FRACTION = 'Mass fraction'
MOLALITY_MOLKG = 'Molality, mol/kg'
AMOUNT_CONCENTRATION_MOLARITY_MOLDM3 = 'Amount concentration (molarity), mol/dm3'
VOLUME_FRACTION = 'Volume fraction'
RATIO_OF_AMOUNT_OF_SOLUTE_TO_MASS_OF_SOLUTION_MOLKG = 'Ratio of amount of solute to mass of solution, mol/kg'
RATIO_OF_MASS_OF_SOLUTE_TO_VOLUME_OF_SOLUTION_KGM3 = 'Ratio of mass of solute to volume of solution, kg/m3'
AMOUNT_RATIO_OF_SOLUTE_TO_SOLVENT = 'Amount ratio of solute to solvent'
MASS_RATIO_OF_SOLUTE_TO_SOLVENT = 'Mass ratio of solute to solvent'
VOLUME_RATIO_OF_SOLUTE_TO_SOLVENT = 'Volume ratio of solute to solvent'
INITIAL_MOLE_FRACTION_OF_SOLUTE = 'Initial mole fraction of solute'
FINAL_MOLE_FRACTION_OF_SOLUTE = 'Final mole fraction of solute'
INITIAL_MASS_FRACTION_OF_SOLUTE = 'Initial mass fraction of solute'
FINAL_MASS_FRACTION_OF_SOLUTE = 'Final mass fraction of solute'
INITIAL_MOLALITY_OF_SOLUTE_MOLKG = 'Initial molality of solute, mol/kg'
FINAL_MOLALITY_OF_SOLUTE_MOLKG = 'Final molality of solute, mol/kg'
```

### eSolventComposition

```python
SOLVENT_MOLE_FRACTION = 'Solvent: Mole fraction'
SOLVENT_MASS_FRACTION = 'Solvent: Mass fraction'
SOLVENT_VOLUME_FRACTION = 'Solvent: Volume fraction'
SOLVENT_MOLALITY_MOLKG = 'Solvent: Molality, mol/kg'
SOLVENT_AMOUNT_CONCENTRATION_MOLARITY_MOLDM3 = 'Solvent: Amount concentration (molarity), mol/dm3'
SOLVENT_AMOUNT_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT = 'Solvent: Amount ratio of component to other component of binary solvent'
SOLVENT_MASS_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT = 'Solvent: Mass ratio of component to other component of binary solvent'
SOLVENT_VOLUME_RATIO_OF_COMPONENT_TO_OTHER_COMPONENT_OF_BINARY_SOLVENT = 'Solvent: Volume ratio of component to other component of binary solvent'
SOLVENT_RATIO_OF_AMOUNT_OF_COMPONENT_TO_MASS_OF_SOLVENT_MOLKG = 'Solvent: Ratio of amount of component to mass of solvent, mol/kg'
SOLVENT_RATIO_OF_COMPONENT_MASS_TO_VOLUME_OF_SOLVENT_KGM3 = 'Solvent: Ratio of component mass to volume of solvent, kg/m3'
```

### eMiscellaneous

```python
WAVELENGTH_NM = 'Wavelength, nm'
FREQUENCY_MHZ = 'Frequency, MHz'
MOLAR_VOLUME_M3MOL = 'Molar volume, m3/mol'
SPECIFIC_VOLUME_M3KG = 'Specific volume, m3/kg'
MASS_DENSITY_KGM3 = 'Mass density, kg/m3'
AMOUNT_DENSITY_MOLM3 = 'Amount density, mol/m3'
MOLAR_ENTROPY_JKMOL = 'Molar entropy, J/K/mol'
RELATIVE_ACTIVITY = '(Relative) activity'
ACTIVITY_COEFFICIENT = 'Activity coefficient'
```

### eBioVariables

```python
PH = 'pH'
IONIC_STRENGTH_MOLALITY_BASIS_MOLKG = 'Ionic strength (molality basis), mol/kg'
IONIC_STRENGTH_AMOUNT_CONCENTRATION_BASIS_MOLDM3 = 'Ionic strength (amount concentration basis), mol/dm3'
PC_AMOUNT_CONCENTRATION_BASIS = 'pC (amount concentration basis)'
SOLVENT_PC_AMOUNT_CONCENTRATION_BASIS = 'Solvent: pC (amount concentration basis)'
```

### eParticipantAmount

```python
AMOUNT_MOL = 'Amount, mol'
MASS_KG = 'Mass, kg'
```

### eConstraintPhase

```python
CRYSTAL_5 = 'Crystal 5'
CRYSTAL_4 = 'Crystal 4'
CRYSTAL_3 = 'Crystal 3'
CRYSTAL_2 = 'Crystal 2'
CRYSTAL_1 = 'Crystal 1'
CRYSTAL = 'Crystal'
CRYSTAL_OF_UNKNOWN_TYPE = 'Crystal of unknown type'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1 = 'Crystal of intercomponent compound 1'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2 = 'Crystal of intercomponent compound 2'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3 = 'Crystal of intercomponent compound 3'
METASTABLE_CRYSTAL = 'Metastable crystal'
GLASS = 'Glass'
SMECTIC_LIQUID_CRYSTAL = 'Smectic liquid crystal'
SMECTIC_LIQUID_CRYSTAL_1 = 'Smectic liquid crystal 1'
SMECTIC_LIQUID_CRYSTAL_2 = 'Smectic liquid crystal 2'
NEMATIC_LIQUID_CRYSTAL = 'Nematic liquid crystal'
NEMATIC_LIQUID_CRYSTAL_1 = 'Nematic liquid crystal 1'
NEMATIC_LIQUID_CRYSTAL_2 = 'Nematic liquid crystal 2'
CHOLESTERIC_LIQUID_CRYSTAL = 'Cholesteric liquid crystal'
LIQUID_CRYSTAL_OF_UNKNOWN_TYPE = 'Liquid crystal of unknown type'
LIQUID = 'Liquid'
LIQUID_MIXTURE_1 = 'Liquid mixture 1'
LIQUID_MIXTURE_2 = 'Liquid mixture 2'
LIQUID_MIXTURE_3 = 'Liquid mixture 3'
SOLUTION = 'Solution'
SOLUTION_1 = 'Solution 1'
SOLUTION_2 = 'Solution 2'
SOLUTION_3 = 'Solution 3'
SOLUTION_4 = 'Solution 4'
FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES = 'Fluid (supercritical or subcritical phases)'
IDEAL_GAS = 'Ideal gas'
GAS = 'Gas'
AIR_AT_1_ATMOSPHERE = 'Air at 1 atmosphere'
```

### eVarPhase

```python
CRYSTAL_5 = 'Crystal 5'
CRYSTAL_4 = 'Crystal 4'
CRYSTAL_3 = 'Crystal 3'
CRYSTAL_2 = 'Crystal 2'
CRYSTAL_1 = 'Crystal 1'
CRYSTAL = 'Crystal'
CRYSTAL_OF_UNKNOWN_TYPE = 'Crystal of unknown type'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_1 = 'Crystal of intercomponent compound 1'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_2 = 'Crystal of intercomponent compound 2'
CRYSTAL_OF_INTERCOMPONENT_COMPOUND_3 = 'Crystal of intercomponent compound 3'
METASTABLE_CRYSTAL = 'Metastable crystal'
GLASS = 'Glass'
SMECTIC_LIQUID_CRYSTAL = 'Smectic liquid crystal'
SMECTIC_LIQUID_CRYSTAL_1 = 'Smectic liquid crystal 1'
SMECTIC_LIQUID_CRYSTAL_2 = 'Smectic liquid crystal 2'
NEMATIC_LIQUID_CRYSTAL = 'Nematic liquid crystal'
NEMATIC_LIQUID_CRYSTAL_1 = 'Nematic liquid crystal 1'
NEMATIC_LIQUID_CRYSTAL_2 = 'Nematic liquid crystal 2'
CHOLESTERIC_LIQUID_CRYSTAL = 'Cholesteric liquid crystal'
LIQUID_CRYSTAL_OF_UNKNOWN_TYPE = 'Liquid crystal of unknown type'
LIQUID = 'Liquid'
LIQUID_MIXTURE_1 = 'Liquid mixture 1'
LIQUID_MIXTURE_2 = 'Liquid mixture 2'
LIQUID_MIXTURE_3 = 'Liquid mixture 3'
SOLUTION = 'Solution'
SOLUTION_1 = 'Solution 1'
SOLUTION_2 = 'Solution 2'
SOLUTION_3 = 'Solution 3'
SOLUTION_4 = 'Solution 4'
FLUID_SUPERCRITICAL_OR_SUBCRITICAL_PHASES = 'Fluid (supercritical or subcritical phases)'
IDEAL_GAS = 'Ideal gas'
GAS = 'Gas'
AIR_AT_1_ATMOSPHERE = 'Air at 1 atmosphere'
```

### eEqName

```python
THERMOMLANTOINEVAPORPRESSURE = 'ThermoML.Antoine.VaporPressure'
THERMOMLCUSTOMEXPANSION = 'ThermoML.CustomExpansion'
THERMOMLHELMHOLTZ3GENERALEOS = 'ThermoML.Helmholtz3General.EOS'
THERMOMLHELMHOLTZ4GENERALEOS = 'ThermoML.Helmholtz4General.EOS'
THERMOMLWAGNERLINEARVAPORPRESSURE = 'ThermoML.WagnerLinear.VaporPressure'
THERMOMLWAGNER25LINEARVAPORPRESSURE = 'ThermoML.Wagner25Linear.VaporPressure'
THERMOMLWAGNER36LINEARVAPORPRESSURE = 'ThermoML.Wagner36Linear.VaporPressure'
THERMOMLPOLYNOMIALEXPANSION = 'ThermoML.PolynomialExpansion'
THERMOMLSPANWAGNER12NONPOLAREOS = 'ThermoML.SpanWagner12Nonpolar.EOS'
THERMOMLSPANWAGNER12POLAREOS = 'ThermoML.SpanWagner12Polar.EOS'
```

### eCompositionRepresentation

```python
AMOUNT_RATIO_OF_SOLVENT_TO_PARTICIPANT = 'Amount ratio of solvent to participant'
MOLALITY_AMOUNT_OF_PARTICIPANT_PER_MASS_OF_SOLVENT_MOLKG = 'Molality - amount of participant per mass of solvent, mol/kg'
AMOUNT_OF_PARTICIPANT_PER_MASS_OF_SOLUTION_MOLKG = 'Amount of participant per mass of solution, mol/kg'
AMOUNT_CONCENTRATION_AMOUNT_OF_PARTICIPANT_PER_VOLUME_OF_SOLUTION_MOLDM3 = 'Amount concentration - amount of participant per volume of solution, mol/dm3'
AMOUNT_RATIO_OF_PARTICIPANT_TO_SOLVENT = 'Amount ratio of participant to solvent'
MASS_RATIO_OF_PARTICIPANT_TO_SOLVENT = 'Mass ratio of participant to solvent'
VOLUME_RATIO_OF_PARTICIPANT_TO_SOLVENT = 'Volume ratio of participant to solvent'
MASS_OF_PARTICIPANT_PER_VOLUME_OF_SOLUTION_KGM3 = 'Mass of participant per volume of solution, kg/m3'
```

### eReactionFormalism

```python
CHEMICAL = 'chemical'
BIOCHEMICAL = 'biochemical'
```

### eReactionType

```python
COMBUSTION_WITH_OXYGEN = 'Combustion with oxygen'
ADDITION_OF_VARIOUS_COMPOUNDS_TO_UNSATURATED_COMPOUNDS = 'Addition of various compounds to unsaturated compounds'
ADDITION_OF_WATER_TO_A_LIQUID_OR_SOLID_TO_PRODUCE_A_HYDRATE = 'Addition of water to a liquid or solid to produce a hydrate'
ATOMIZATION_OR_FORMATION_FROM_ATOMS = 'Atomization (or formation from atoms)'
COMBUSTION_WITH_OTHER_ELEMENTS_OR_COMPOUNDS = 'Combustion with other elements or compounds'
ESTERIFICATION = 'Esterification'
EXCHANGE_OF_ALKYL_GROUPS = 'Exchange of alkyl groups'
EXCHANGE_OF_HYDROGEN_ATOMS_WITH_OTHER_GROUPS = 'Exchange of hydrogen (atoms) with other groups'
FORMATION_OF_A_COMPOUND_FROM_ELEMENTS_IN_THEIR_STABLE_STATE = 'Formation of a compound from elements in their stable state'
HALOGENATION_ADDITION_OF_OR_REPLACEMENT_BY_A_HALOGEN = 'Halogenation (addition of or replacement by a halogen)'
HYDROGENATION_ADDITION_OF_HYDROGEN_TO_UNSATURATED_COMPOUNDS = 'Hydrogenation (addition of hydrogen to unsaturated compounds)'
HYDROHALOGENATION = 'Hydrohalogenation'
HYDROLYSIS_OF_IONS = 'Hydrolysis of ions'
OTHER_REACTIONS_WITH_WATER = 'Other reactions with water'
ION_EXCHANGE = 'Ion exchange'
NEUTRALIZATION_REACTION_OF_AN_ACID_WITH_A_BASE = 'Neutralization (reaction of an acid with a base)'
OXIDATION_WITH_OXIDIZING_AGENTS_OTHER_THAN_OXYGEN = 'Oxidation with oxidizing agents other than oxygen'
OXIDATION_WITH_OXYGEN_NOT_COMPLETE = 'Oxidation with oxygen (not complete)'
POLYMERIZATION_ALL_OTHER_TYPES = 'Polymerization (all other types)'
HOMONUCLEAR_DIMERIZATION = 'Homonuclear dimerization'
SOLVOLYIS_SOLVENTS_OTHER_THAN_WATER = 'Solvolyis (solvents other than water)'
STEREOISOMERISM = 'Stereoisomerism'
STRUCTURAL_ISOMERIZATION = 'Structural isomerization'
FORMATION_OF_ION = 'Formation of ion'
OTHER_REACTIONS = 'Other reactions'
```

