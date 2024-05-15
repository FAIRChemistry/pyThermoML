import sdRDM

from typing import Dict, Optional
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .bioproperties import BioProperties
from .activityfugacityosmoticprop import ActivityFugacityOsmoticProp
from .phasetransition import PhaseTransition
from .refractionsurfacetensionsoundspeed import RefractionSurfaceTensionSoundSpeed
from .volumetricprop import VolumetricProp
from .criticals import Criticals
from .excesspartialapparentenergyprop import ExcessPartialApparentEnergyProp
from .transportprop import TransportProp
from .heatcapacityandderivedprop import HeatCapacityAndDerivedProp
from .compositionatphaseequilibrium import CompositionAtPhaseEquilibrium
from .reactionstatechangeprop import ReactionStateChangeProp
from .vaporpboilingtazeotroptandp import VaporPBoilingTAzeotropTandP
from .reactionequilibriumprop import ReactionEquilibriumProp


@forge_signature
class PropertyGroup(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    activity_fugacity_osmotic_prop: Optional[ActivityFugacityOsmoticProp] = element(
        default_factory=ActivityFugacityOsmoticProp,
        tag="ActivityFugacityOsmoticProp",
        json_schema_extra=dict(xml="ActivityFugacityOsmoticProp"),
    )
    bio_properties: Optional[BioProperties] = element(
        default_factory=BioProperties,
        tag="BioProperties",
        json_schema_extra=dict(xml="BioProperties"),
    )
    composition_at_phase_equilibrium: Optional[CompositionAtPhaseEquilibrium] = element(
        default_factory=CompositionAtPhaseEquilibrium,
        tag="CompositionAtPhaseEquilibrium",
        json_schema_extra=dict(xml="CompositionAtPhaseEquilibrium"),
    )
    criticals: Optional[Criticals] = element(
        default_factory=Criticals,
        tag="Criticals",
        json_schema_extra=dict(xml="Criticals"),
    )
    excess_partial_apparent_energy_prop: Optional[ExcessPartialApparentEnergyProp] = (
        element(
            default_factory=ExcessPartialApparentEnergyProp,
            tag="ExcessPartialApparentEnergyProp",
            json_schema_extra=dict(xml="ExcessPartialApparentEnergyProp"),
        )
    )
    heat_capacity_and_derived_prop: Optional[HeatCapacityAndDerivedProp] = element(
        default_factory=HeatCapacityAndDerivedProp,
        tag="HeatCapacityAndDerivedProp",
        json_schema_extra=dict(xml="HeatCapacityAndDerivedProp"),
    )
    phase_transition: Optional[PhaseTransition] = element(
        default_factory=PhaseTransition,
        tag="PhaseTransition",
        json_schema_extra=dict(xml="PhaseTransition"),
    )
    reaction_equilibrium_prop: Optional[ReactionEquilibriumProp] = element(
        default_factory=ReactionEquilibriumProp,
        tag="ReactionEquilibriumProp",
        json_schema_extra=dict(xml="ReactionEquilibriumProp"),
    )
    reaction_state_change_prop: Optional[ReactionStateChangeProp] = element(
        default_factory=ReactionStateChangeProp,
        tag="ReactionStateChangeProp",
        json_schema_extra=dict(xml="ReactionStateChangeProp"),
    )
    refraction_surface_tension_sound_speed: Optional[
        RefractionSurfaceTensionSoundSpeed
    ] = element(
        default_factory=RefractionSurfaceTensionSoundSpeed,
        tag="RefractionSurfaceTensionSoundSpeed",
        json_schema_extra=dict(xml="RefractionSurfaceTensionSoundSpeed"),
    )
    transport_prop: Optional[TransportProp] = element(
        default_factory=TransportProp,
        tag="TransportProp",
        json_schema_extra=dict(xml="TransportProp"),
    )
    vapor_p_boiling_t_azeotrop_tand_p: Optional[VaporPBoilingTAzeotropTandP] = element(
        default_factory=VaporPBoilingTAzeotropTandP,
        tag="VaporPBoilingTAzeotropTandP",
        json_schema_extra=dict(xml="VaporPBoilingTAzeotropTandP"),
    )
    volumetric_prop: Optional[VolumetricProp] = element(
        default_factory=VolumetricProp,
        tag="VolumetricProp",
        json_schema_extra=dict(xml="VolumetricProp"),
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
