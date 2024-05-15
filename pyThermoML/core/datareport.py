import sdRDM

import pubchempy
import numpy as np
import pandas as pd
from typing import Optional, Union, List, Dict
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .sorgid import SOrgID
from .property import Property
from .propphaseid import PropPhaseID
from .reactiondata import ReactionData
from .pureormixturedata import PureOrMixtureData
from .compound import Compound
from .variable import Variable
from .ion import Ion
from .equation import Equation
from .auxiliarysubstance import AuxiliarySubstance
from .multicomponentsubstance import MulticomponentSubstance
from .participant import Participant
from .propertymethodid import PropertyMethodID
from .eexppurpose import eExpPurpose
from .component import Component
from .ereactiontype import eReactionType
from .solvent import Solvent
from .citation import Citation
from .numvalues import NumValues
from .especiationstate import eSpeciationState
from .ereactionformalism import eReactionFormalism
from .sample import Sample
from .version import Version
from .combineduncertainty import CombinedUncertainty
from .biomaterial import Biomaterial
from .constraint import Constraint
from .polymer import Polymer
from .regnum import RegNum
from .phaseid import PhaseID
from ..tools.mapping import (
    CONTSTRAINT_IDS,
    VARIABLES_IDS,
    PROPERTY_GROUPS,
    ID_MAP,
    is_actual_letters,
    NoMatchingProperty,
    set_property_group,
    get_num_values_from_json,
)


@forge_signature
class DataReport(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    citation: Optional[Citation] = element(
        default_factory=Citation, tag="Citation", json_schema_extra=dict(xml="Citation")
    )
    version: Optional[Version] = element(
        default_factory=Version, tag="Version", json_schema_extra=dict(xml="Version")
    )
    compound: List[Compound] = element(
        default_factory=ListPlus,
        tag="Compound",
        json_schema_extra=dict(multiple=True, xml="Compound"),
    )
    pure_or_mixture_data: List[PureOrMixtureData] = element(
        default_factory=ListPlus,
        tag="PureOrMixtureData",
        json_schema_extra=dict(multiple=True, xml="PureOrMixtureData"),
    )
    reaction_data: List[ReactionData] = element(
        default_factory=ListPlus,
        tag="ReactionData",
        json_schema_extra=dict(multiple=True, xml="ReactionData"),
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

    def add_to_compound(
        self,
        biomaterial: Optional[Biomaterial] = None,
        ion: Optional[Ion] = None,
        multicomponent_substance: Optional[MulticomponentSubstance] = None,
        polymer: Optional[Polymer] = None,
        e_speciation_state: Union[eSpeciationState, str, None] = None,
        n_comp_index: Optional[int] = None,
        n_pub_chem_id: Optional[int] = None,
        reg_num: Optional[RegNum] = None,
        s_cas_name: Optional[str] = None,
        s_common_name: List[str] = ListPlus(),
        s_formula_molec: Optional[str] = None,
        s_iupac_name: Optional[str] = None,
        s_org_id: List[SOrgID] = ListPlus(),
        s_smiles: List[str] = ListPlus(),
        s_standard_in_ch_i: Optional[str] = None,
        s_standard_in_ch_i_key: Optional[str] = None,
        sample: List[Sample] = ListPlus(),
        **kwargs,
    ) -> Compound:
        """
        This method adds an object of type 'Compound' to attribute compound

        Args:

            biomaterial (): . Defaults to None
            ion (): . Defaults to None
            multicomponent_substance (): . Defaults to None
            polymer (): . Defaults to None
            e_speciation_state (): . Defaults to None
            n_comp_index (): Index to link compounds to data. Defaults to None
            n_pub_chem_id (): . Defaults to None
            reg_num (): . Defaults to None
            s_cas_name (): . Defaults to None
            s_common_name (): Common name, string Common name. Defaults to ListPlus()
            s_formula_molec (): Molecular formula, string Chemical molecular formula. Defaults to None
            s_iupac_name (): IUPAC name, string International Union of Physics and Applied Chemistry name. Defaults to None
            s_org_id (): . Defaults to ListPlus()
            s_smiles (): SMILES notation, string SMILES notation. Defaults to ListPlus()
            s_standard_in_ch_i (): Standard InChI string IUPAC International Chemical Identifier. Defaults to None
            s_standard_in_ch_i_key (): Standard InChI key. Defaults to None
            sample (): . Defaults to ListPlus()
        """
        params = {
            "biomaterial": biomaterial,
            "ion": ion,
            "multicomponent_substance": multicomponent_substance,
            "polymer": polymer,
            "e_speciation_state": e_speciation_state,
            "n_comp_index": n_comp_index,
            "n_pub_chem_id": n_pub_chem_id,
            "reg_num": reg_num,
            "s_cas_name": s_cas_name,
            "s_common_name": s_common_name,
            "s_formula_molec": s_formula_molec,
            "s_iupac_name": s_iupac_name,
            "s_org_id": s_org_id,
            "s_smiles": s_smiles,
            "s_standard_in_ch_i": s_standard_in_ch_i,
            "s_standard_in_ch_i_key": s_standard_in_ch_i_key,
            "sample": sample,
        }
        if id is not None:
            params["id"] = id
        self.compound.append(Compound(**params))
        return self.compound[-1]

    def add_to_pure_or_mixture_data(
        self,
        component: List[Component] = ListPlus(),
        phase_id: List[PhaseID] = ListPlus(),
        property: List[Property] = ListPlus(),
        auxiliary_substance: List[AuxiliarySubstance] = ListPlus(),
        constraint: List[Constraint] = ListPlus(),
        date_date_added: Optional[str] = None,
        e_exp_purpose: Union[eExpPurpose, str, None] = None,
        equation: List[Equation] = ListPlus(),
        n_pure_or_mixture_data_number: Optional[int] = None,
        num_values: List[NumValues] = ListPlus(),
        s_compiler: Optional[str] = None,
        s_contributor: Optional[str] = None,
        variable: List[Variable] = ListPlus(),
        **kwargs,
    ) -> PureOrMixtureData:
        """
        This method adds an object of type 'PureOrMixtureData' to attribute pure_or_mixture_data

        Args:

            component (): . Defaults to ListPlus()
            phase_id (): CASRN is necessary for mixtures only. Defaults to ListPlus()
            property (): . Defaults to ListPlus()
            auxiliary_substance (): . Defaults to ListPlus()
            constraint (): . Defaults to ListPlus()
            date_date_added (): . Defaults to None
            e_exp_purpose (): Purpose of measurement. Defaults to None
            equation (): . Defaults to ListPlus()
            n_pure_or_mixture_data_number (): . Defaults to None
            num_values (): . Defaults to ListPlus()
            s_compiler (): . Defaults to None
            s_contributor (): . Defaults to None
            variable (): . Defaults to ListPlus()
        """
        params = {
            "component": component,
            "phase_id": phase_id,
            "property": property,
            "auxiliary_substance": auxiliary_substance,
            "constraint": constraint,
            "date_date_added": date_date_added,
            "e_exp_purpose": e_exp_purpose,
            "equation": equation,
            "n_pure_or_mixture_data_number": n_pure_or_mixture_data_number,
            "num_values": num_values,
            "s_compiler": s_compiler,
            "s_contributor": s_contributor,
            "variable": variable,
        }
        if id is not None:
            params["id"] = id
        self.pure_or_mixture_data.append(PureOrMixtureData(**params))
        return self.pure_or_mixture_data[-1]

    def add_to_reaction_data(
        self,
        e_reaction_type: Union[eReactionType, str, None] = None,
        participant: List[Participant] = ListPlus(),
        property: List[Property] = ListPlus(),
        auxiliary_substance: List[AuxiliarySubstance] = ListPlus(),
        constraint: List[Constraint] = ListPlus(),
        date_date_added: Optional[str] = None,
        e_exp_purpose: Union[eExpPurpose, str, None] = None,
        e_reaction_formalism: Union[eReactionFormalism, str, None] = None,
        equation: List[Equation] = ListPlus(),
        n_electron_number: Optional[int] = None,
        n_reaction_data_number: Optional[int] = None,
        num_values: List[NumValues] = ListPlus(),
        s_compiler: Optional[str] = None,
        s_contributor: Optional[str] = None,
        solvent: List[Solvent] = ListPlus(),
        variable: List[Variable] = ListPlus(),
        **kwargs,
    ) -> ReactionData:
        """
        This method adds an object of type 'ReactionData' to attribute reaction_data

        Args:

            e_reaction_type (): . Defaults to None
            participant (): . Defaults to ListPlus()
            property (): . Defaults to ListPlus()
            auxiliary_substance (): . Defaults to ListPlus()
            constraint (): . Defaults to ListPlus()
            date_date_added (): . Defaults to None
            e_exp_purpose (): Purpose of measurement. Defaults to None
            e_reaction_formalism (): . Defaults to None
            equation (): . Defaults to ListPlus()
            n_electron_number (): . Defaults to None
            n_reaction_data_number (): . Defaults to None
            num_values (): . Defaults to ListPlus()
            s_compiler (): . Defaults to None
            s_contributor (): . Defaults to None
            solvent (): . Defaults to ListPlus()
            variable (): . Defaults to ListPlus()
        """
        params = {
            "e_reaction_type": e_reaction_type,
            "participant": participant,
            "property": property,
            "auxiliary_substance": auxiliary_substance,
            "constraint": constraint,
            "date_date_added": date_date_added,
            "e_exp_purpose": e_exp_purpose,
            "e_reaction_formalism": e_reaction_formalism,
            "equation": equation,
            "n_electron_number": n_electron_number,
            "n_reaction_data_number": n_reaction_data_number,
            "num_values": num_values,
            "s_compiler": s_compiler,
            "s_contributor": s_contributor,
            "solvent": solvent,
            "variable": variable,
        }
        if id is not None:
            params["id"] = id
        self.reaction_data.append(ReactionData(**params))
        return self.reaction_data[-1]

    def add_compounds_via_smiles(self, smiles_dict: Dict[str, str]):
        """
        This function retrieves properties from PubChem for a given compound represented by its SMILES string
        and add it to the ThermoML datareport.

        Parameters:
        - datareport (DataReport): Datareport to add the compounds.
        - smiles_dict(Dict[str, str]): A dictionary with compound name and its corresponding smiles

        """
        for i, (compound_name, smiles) in enumerate(smiles_dict.items()):
            print(f"\nAdd component: '{compound_name}' with SMILES: '{smiles}'")
            compounds = pubchempy.get_compounds(smiles, namespace="smiles")
            if compounds:
                compound = compounds[0]

                properties = {
                    "n_pub_chem_id": compound.cid,
                    "s_formula_molec": compound.molecular_formula,
                    "s_iupac_name": compound.iupac_name,
                    "s_common_name": (
                        [*compound.synonyms[:3], compound_name]
                        if compound_name not in compound.synonyms[:3]
                        else compound.synonyms[:3]
                    ),
                    "s_standard_in_ch_i": compound.inchi,
                    "s_standard_in_ch_i_key": compound.inchikey,
                }

                self.add_to_compound(**properties, reg_num=RegNum(n_org_num=i + 1))
                print("Success!")
            else:
                raise KeyError(
                    f"No compound found that matches the presented SMILES: '{smiles}'"
                )

    def list_compounds(self, id: str = "common_name", verbose: bool = True):
        """
        This function uses either a integer number to identify a component or loops through the saved compounds of the DataReport class and compares the smiles.

        Parameters:
         - id (str, optional): Identifier type, either common_name or or smiles.
         - verbose (bool,optional): Print components to screen if True. Defaults to True.

        Returns:
         - reg_num (RegNum): An RegNum instance representing the component.

        """
        if id not in ID_MAP:
            raise KeyError(
                f"Specified compound identification: '{id}' is not implemented."
                f" Available are '{', '.join(ID_MAP.keys())}'"
            )

        ids = {
            comp.reg_num.n_org_num: sorted(
                getattr(comp, ID_MAP[id]), key=lambda x: not is_actual_letters(x)
            )
            for comp in self.compound
        }

        if verbose:
            print(f"\nThe datareport contains the following compounds:\n")
            for key, value in ids.items():
                print(f"   {key}: {value[0]}")

        return ids

    def get_reg_num(self, identifier: str | int, id: str = "common_name") -> RegNum:
        """
        This function uses either a integer number to identify a component or loops through the saved compounds of the DataReport class and compares the smiles.

        Parameters:
         - datareport (DataReport): Datareport containing compounds.
         - identifier (str|int): The name of the component or the identifing integer number.
         - id (str, optional): Identifier type, either common_name or or smiles.

        Returns:
         - reg_num (RegNum): An RegNum instance representing the component.

        """
        ids = self.list_compounds(id=id, verbose=False)

        if isinstance(identifier, int):
            reg_num = RegNum(n_org_num=identifier)

        elif isinstance(identifier, str):
            # In case an empty string is parsed, return empty RegNum
            if not identifier:
                reg_num = RegNum()
            else:
                flag = False
                for key, values in ids.items():
                    if identifier.lower() in (value.lower() for value in values):
                        reg_num = RegNum(n_org_num=key)
                        flag = True
                if not flag:
                    raise KeyError(
                        f"Specified identifier '{identifier}' is not present in the"
                        " datareport."
                    )

        return reg_num

    def get_common_name(self, identifier: int):
        if not isinstance(identifier, int):
            raise TypeError(f"Specified identifier is not an integer: '{identifier}'")

        ids = self.list_compounds(verbose=False)

        if not identifier in ids:
            raise KeyError(
                f"Specified identifier '{identifier}' is not present in the datareport."
            )

        return ids[identifier]

    def get_property_list(self, verbose: bool = False):

        # Get the id_dict
        id_dict = self.list_compounds(verbose=False)

        property_list = sorted({
            f'"{pomd.property_name()["type"]}" of'
            f' {id_dict[pomd.property_name()["component_identifier"].n_org_num][0] if pomd.property_name()["component_identifier"].n_org_num else "system"}'
            for pomd in self.pure_or_mixture_data
        })

        if verbose:
            print("\n".join(property_list))

        return property_list

    def get_all_data(self, verbose: bool = True):

        # Get the id_dict
        id_dict = self.list_compounds(verbose=False)

        final = []

        if verbose:
            print("All data saved in the datareport:\n")

        for pomd in self.pure_or_mixture_data:

            df = pomd.get_property()
            property_dict = pomd.property_name()
            variables = pomd.get_variables()
            constraints = pomd.get_constraints()

            values = [
                df["mean"].values,
                df["95_confidence"].values,
                *[var["values"] for var in variables],
                *[[const["value"]] * len(df["mean"]) for const in constraints],
            ]
            indexes = (
                [
                    (
                        (
                            f'"{property_dict["type"]}" of'
                            f' {id_dict[property_dict["component_identifier"].n_org_num][0] if property_dict["component_identifier"].n_org_num else "system"}'
                        ),
                        "mean",
                    ),
                    ("", "95_confidence"),
                ]
                + [("variable", var["type"]) for var in variables]
                + [
                    (
                        "constraint",
                        (
                            f'"{const["type"]}" of'
                            f' {id_dict[const["component_identifier"].n_org_num][0] if const["component_identifier"].n_org_num else "system"}'
                        ),
                    )
                    for const in constraints
                ]
            )

            df_result = pd.DataFrame(values).T
            df_result.columns = pd.MultiIndex.from_tuples(indexes)
            final.append(df_result)

            if verbose:
                print(df_result.to_string(), "\n")

        return final

    def analysis_property(
        self,
        prop_name: str,
        prop_identifier: str = "",
    ):
        """
        Analyzes a specific property in a DataReport.

        Parameters:
            prop_name (str): The name of the property to analyze. This can also be a substring of the property.
            prop_identifier (RegNum, optional): Component identifier for the property. Defaults to "".

        Returns:
            pd.DataFrame: A DataFrame containing the analyzed property values over the composition of the component.
        """

        # Get reg_num for property identifier
        property_identifier = self.get_reg_num(prop_identifier)

        # Get the id_dict
        id_dict = self.list_compounds(verbose=False)

        if prop_identifier and property_identifier.n_org_num == None:
            raise KeyError(
                f"Property identifier '{prop_identifier}' is not matched with compounds"
                " from datareport!"
            )

        final = []

        for pomd in self.pure_or_mixture_data:
            # Check if property exists in pure of mixture data
            if pomd.property_exists(prop_name, property_identifier):

                # Get properties
                prop_df = pomd.get_property()

                # Get variables
                variables = pomd.get_variables()

                for variable in variables:
                    prop_df[variable["type"]] = variable["values"]

                # Get constraints
                constraints = pomd.get_constraints()

                for const in constraints:
                    txt = f'{const["type"]} of'
                    txt += (
                        f' {id_dict[const["component_identifier"].n_org_num][0] if const["component_identifier"].n_org_num else "system"}'
                    )
                    prop_df[txt] = [const["value"]] * prop_df.shape[0]

                final.append(prop_df)

        if not final:
            prop_list = self.get_property_list()
            raise KeyError(
                f"Property{'combined with the identifier of the property' if prop_identifier else '' } not"
                " found in datareport! Exisiting properties are: \n",
                "\n".join(prop_list),
            )

        return pd.concat(final)

    def get_property_method_id(
        self,
        property_dict: Dict[str, str | float],
        component_identifier: str | int = "",
    ):
        """
        Function to get the PropertyMethodID for a given property in a DataReport object.

        Parameters:
            property_dict (Dict[str, Union[str, float]]): A dictionary containing the property name and value.
            component_identifier (Union[str, int], optional): An optional component identifier for the property. Defaults to "".

        Returns:
            PropertyMethodID: The PropertyMethodID object for the matched property.

        Raises:
            NoMatchingProperty: If no matching property is found in the ThermoML property groups.

        """
        flag = False
        for key, values in PROPERTY_GROUPS.items():
            for prop in values:
                if property_dict["name"] in prop:
                    print(
                        f"Matched '{property_dict['name']}' with ThermoML property"
                        f" '{prop}' in following category: '{key}'\n"
                    )
                    matched_group = key
                    matched_property = prop
                    flag = True
                    break
            if flag:
                break
        if not flag:
            raise NoMatchingProperty(property_dict["name"])

        if component_identifier:
            cmp_identifier = self.get_reg_num(component_identifier)
            if cmp_identifier.n_org_num == None:
                raise KeyError(
                    f"Provided component identifier '{component_identifier}' for the"
                    f" properity: '{property_dict['name']}' can't be found in the"
                    " compounds of the datareport."
                )
        else:
            cmp_identifier = RegNum()

        property_method_id = PropertyMethodID(
            property_group=set_property_group(
                prop_group=matched_group, prop_name=matched_property, **property_dict
            ),
            reg_num=cmp_identifier,
        )

        return property_method_id

    def create_pure_or_mixture_data(
        self,
        components: List[str | int],
        phase: str,
        constraints: Dict[str, float | int | Dict[str, float | int]],
        variables: Dict[str, List[float]],
        property_dict: Dict[str, str | float],
        precision: int = 5,
    ):
        """
        Create a PureOrMixtureData entry in the DataReport.

        Parameters:
        - components (List[str|int]): A list of component names or RegNums.
        - phase (str): The phase of the pure or mixture data.
        - constraints (Dict[str, float|int|Dict[str, float|int]]): A dictionary of constraints. The keys are constraint IDs and the values can be either floats, ints, or nested dictionaries.
        - variables (Dict[str, List[float]]): A dictionary of variables. The keys are variable IDs and the values are lists of variable values.
        - property_dict (Dict[str, str|float]): A dictionary containing information about the property. If "paths" are specified, data is extracted from json, otherwise "property_results" needs to be provided.
        - precision (int, optional): Precision of floating point numbers. Defaults to 5.

        Returns:
        - dict: A dictionary representation of the PureOrMixtureData object.

        Raises:
        - KeyError: If the constraint format is incorrect.

        """
        pomd = PureOrMixtureData()

        # Add components (identify component via RegNum or via name)
        for component in components:
            pomd.add_to_component(
                reg_num=self.get_reg_num(component),
            )

        # Add the phase
        phase_id = pomd.add_to_phase_id(e_phase=phase)

        # Add constraints
        i = 1
        for key, value in constraints.items():
            if isinstance(value, dict):
                for keykey, valval in value.items():
                    pomd.add_to_constraint(
                        constraint_id=CONTSTRAINT_IDS[key](
                            reg_num=self.get_reg_num(keykey)
                        ),
                        n_constr_digits=precision,
                        n_constraint_value=np.round(valval, precision),
                        constraint_phase_id={
                            "e_prop_phase": phase_id.e_phase,
                            **{
                                key: value
                                for key, value in phase_id
                                if key != "e_phase"
                            },
                        },
                        n_constraint_number=i,
                    )
                    i += 1
            elif isinstance(value, float) or isinstance(value, int):
                pomd.add_to_constraint(
                    constraint_id=CONTSTRAINT_IDS[key](),
                    n_constr_digits=3,
                    n_constraint_value=np.round(value, precision),
                    constraint_phase_id={
                        "e_prop_phase": phase_id.e_phase,
                        **{key: value for key, value in phase_id if key != "e_phase"},
                    },
                    n_constraint_number=i,
                )
                i += 1
            else:
                raise KeyError(
                    "Wrong constraint format specified. Either a float or a dict"
                    f" should be presented. Not type: '{type(value)}'"
                )

        # Add variables
        for i, (key, value) in enumerate(variables.items()):
            pomd.add_to_variable(
                variable_id=VARIABLES_IDS[key](),
                var_phase_id={
                    "e_var_phase": phase_id.e_phase,
                    **{key: value for key, value in phase_id if key != "e_phase"},
                },
                n_var_number=i + 1,
            )

        # Add numerical values
        if "paths" in property_dict.keys():
            print("Extract property values via json file!")
            for i, (paths, (_, variable_values)) in enumerate(
                zip(property_dict["paths"], variables.items())
            ):
                for path, value in zip(paths, variable_values):
                    num_values = pomd.add_to_num_values()

                    # get property value
                    property_results = get_num_values_from_json(
                        path, property_dict["keys"]
                    )

                    num_values.add_to_property_value(
                        n_prop_value=np.round(property_results["value"], precision),
                        n_prop_digits=precision,
                        n_prop_number=1,
                        combined_uncertainty=[
                            CombinedUncertainty(
                                n_comb_uncert_assess_num=1,
                                n_comb_expand_uncert_value=np.round(
                                    property_results["uncertainty"], 6
                                ),
                            )
                        ],
                    )

                    num_values.add_to_variable_value(
                        n_var_digits=precision,
                        n_var_value=np.round(value, precision),
                        n_var_number=i + 1,
                    )

        elif "property_results" in property_dict.keys():
            for i, (properties_results, (_, variable_values)) in enumerate(
                zip(property_dict["property_results"], variables.items())
            ):
                for property_results, value in zip(properties_results, variable_values):
                    num_values = pomd.add_to_num_values()

                    num_values.add_to_property_value(
                        n_prop_value=np.round(property_results["value"], precision),
                        n_prop_digits=precision,
                        n_prop_number=1,
                        combined_uncertainty=[
                            CombinedUncertainty(
                                n_comb_uncert_assess_num=1,
                                n_comb_expand_uncert_value=np.round(
                                    property_results["uncertainty"], 6
                                ),
                            )
                        ],
                    )

                    num_values.add_to_variable_value(
                        n_var_digits=precision,
                        n_var_value=np.round(value, precision),
                        n_var_number=i + 1,
                    )

        # Add property
        pomd.add_to_property(
            property_method_id=self.get_property_method_id(
                property_dict=property_dict,
                component_identifier=property_dict["component_identifier"],
            ),
            e_presentation="Direct value, X",
            combined_uncertainty=[
                CombinedUncertainty(
                    n_comb_uncert_assess_num=1,
                    s_comb_uncert_eval_method="Data file compiler",
                    n_comb_uncert_lev_of_confid=property_dict["confidence_interval"],
                    e_comb_uncert_eval_method=property_dict["uncertanty_method"],
                )
            ],
            prop_phase_id=[
                PropPhaseID(
                    e_prop_phase=phase_id.e_phase,
                    **{key: value for key, value in phase_id if key != "e_phase"},
                )
            ],
            n_prop_number=1,
        )

        self.add_to_pure_or_mixture_data(**pomd.__dict__)
