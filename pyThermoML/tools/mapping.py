import json
import numpy as np
from typing import List, Dict

from ..core.regnum import RegNum
from ..core.variableid import VariableID
from ..core.constraintid import ConstraintID
from ..core.propertygroup import PropertyGroup
from ..core.predictionmethodref import PredictionMethodRef


def list_possible_properties( verbose: bool=True ):
    txt = "Implemented properties for each group:\n"
    for key,value in PROPERTY_GROUPS.items():
        if value: txt += f"\nGroup: {key}\n{'; '.join(value)}\n"
    if verbose:
        print(txt)
    else:
        return txt

def list_possible_constraints( verbose: bool=True ):
    txt = f"Implemented constraints are:\n  {'; '.join(CONTSTRAINT_IDS.keys())}"
    if verbose:
        print(txt)
    else:
        return txt

def list_possible_variables( verbose: bool=True ):
    txt = f"Implemented variables are:\n  {'; '.join(VARIABLES_IDS.keys())}"
    if verbose:
        print(txt)
    else:
        return txt

class NoMatchingProperty(Exception):
    def __init__(self, property_name: str):
        txt = list_possible_properties( verbose = False )
        message = f"No property group found for property: '{property_name}'. {txt}"
        super().__init__(message)

def set_pressure_const(**kwargs):
    return ConstraintID( constraint_type = {"e_pressure": "Pressure, kPa"} )

def set_temperature_const(**kwargs):
    return ConstraintID( constraint_type = {"e_temperature": "Temperature, K"} )

def set_mass_fraction(reg_num: RegNum, **kwargs):
    return ConstraintID( constraint_type = {"e_component_composition": "Mass fraction"}, reg_num = reg_num )

def set_mole_fraction(reg_num: RegNum, **kwargs):
    return ConstraintID( constraint_type = {"e_component_composition": "Mole fraction"}, reg_num = reg_num )

def set_pressure_var(**kwargs):
    return VariableID( variable_type = {"e_pressure": "Pressure, kPa"} )

def set_temperature_var(**kwargs):
    return VariableID( variable_type = {"e_temperature": "Temperature, K"} )

def set_property_group(prop_group: str, prop_name: str,**kwargs):
    return PropertyGroup( **{ prop_group: { "e_prop_name": prop_name, 
                                            "e_method_name": "N/A",
                                            "prediction": { "e_prediction_type": kwargs["prediction_type"], 
                                                            "s_prediction_method_name": kwargs["method_name"], 
                                                            "s_prediction_method_description": kwargs["method_description"],
                                                            "prediction_method_ref": [ PredictionMethodRef( s_doi = kwargs["method_ref_doi"] ) ]
                                                          } } } )


PROPERTY_GROUPS = {
    'activity_fugacity_osmotic_prop': ["Activity", "Activity coefficient", "Osmotic pressure, kPa", "Osmotic coefficient"],
    'bio_properties': [],
    'composition_at_phase_equilibrium': ["Henry's Law constant (mole fraction scale), kPa",
                                         "Henry's Law constant (molality scale), kPakg/mol",
                                         "Henry's Law constant (amount concentration scale), kPadm3/mol",
                                         "Amount per mass of solution, mol/kg", "Molality, mol/kg", 
                                         "Amount concentration (molarity), mol/dm3"],
    'criticals': [],
    'excess_partial_apparent_energy_prop': ["Excess molar enthalpy (molar enthalpy of mixing), kJ/mol"],
    'heat_capacity_and_derived_prop': ["Molar enthalpy, kJ/mol"],
    'phase_transition': [],
    'reaction_equilibrium_prop': [],
    'reaction_state_change_prop': [],
    'refraction_surface_tension_sound_speed': [],
    'transport_prop': ["Self diffusion coefficient, m2/s", "Viscosity, Pas", "Kinematic Viscosity m2/s"],
    'vapor_p_boiling_t_azeotrop_tand_p': [],
    'volumetric_prop': ["Mass density, kg/m3","Specific volume, m3/kg","Amount density. mol/m3", "Molar volume, m3/mol", "Compressibility factor",
                        "Adiabatic compressibility, 1/kPa", "Isothermal compressibility, 1/kPa", "Isobaric coefficient of expansion, 1/K",
                        "Excess molar volume, m3/mol", "Partial molar volume, m3/mol"]
}

CONTSTRAINT_IDS = { "mass_fraction": set_mass_fraction,
                    "mole_fraction": set_mole_fraction,
                    "pressure": set_pressure_const,
                    "temperature": set_temperature_const }

VARIABLES_IDS = { "pressure": set_pressure_var,
                  "temperature": set_temperature_var }

ID_MAP = { "common_name": "s_common_name",
           "smiles": "s_smiles"   
         }

def is_actual_letters(s):
    return all(char.isalpha() or char.isspace() for char in s)

def get_num_values_from_json( json_file: str, key_list: List[str] ):
    """
    Get the numerical values from a JSON file based on a list of keys.

    Parameters:
    - json_file (str): The path to the JSON file.
    - key_list (List[str]): A list of keys to access the desired value in the JSON file.

    Returns:
    - dict: A dictionary containing the numerical value and its uncertainty. The value is obtained by recursively accessing the JSON file using the provided list of keys, 
            and the uncertainty is calculated by multiplying the standard deviation by two.

    Example:
    get_num_values_from_json('data.json', [['results','data','value']])
    # Output: {value:{'mean': 10.5, 'uncertainty': 0.2}}

    Note:
    - The function assumes that the JSON file is structured in a way that allows accessing the desired value using the provided list of keys.
    - The function assumes that the JSON file contains a key named 'mean' for the numerical value and a key named 'std' for the standard deviation.
    - The function assumes that the standard deviation represents the uncertainty of the numerical value.
    """
    with open(json_file) as f:
        data = json.load(f)
    
    for i,key in enumerate(key_list):
        if i == 0:
            if key not in data.keys():
                raise KeyError(f"Specified key '{key}' does not exist in json file: '{json_file}'")
            result = data[key]
        else:
            if key not in result.keys():
                raise KeyError(f"Specified key '{key}' does not exist in json file: '{json_file}' in the subkey '{key_list[i-1]}'")
            result = result[key]
        
    # To get 95% confidence interval, multiply std with two.
    return {"value": result["mean"], "uncertainty": result["std"]*2 }