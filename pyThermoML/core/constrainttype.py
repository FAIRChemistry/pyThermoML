import sdRDM

from typing import Dict, Optional, Union
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .etemperature import eTemperature
from .ecomponentcomposition import eComponentComposition
from .epressure import ePressure
from .eparticipantamount import eParticipantAmount
from .esolventcomposition import eSolventComposition
from .ebiovariables import eBioVariables
from .emiscellaneous import eMiscellaneous


@forge_signature
class ConstraintType(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_bio_variables: Union[eBioVariables, str, None] = element(
        default=None, tag="eBioVariables", json_schema_extra=dict(xml="eBioVariables")
    )
    e_component_composition: Union[eComponentComposition, str, None] = element(
        default=None,
        tag="eComponentComposition",
        json_schema_extra=dict(xml="eComponentComposition"),
    )
    e_miscellaneous: Union[eMiscellaneous, str, None] = element(
        default=None, tag="eMiscellaneous", json_schema_extra=dict(xml="eMiscellaneous")
    )
    e_participant_amount: Union[eParticipantAmount, str, None] = element(
        default=None,
        tag="eParticipantAmount",
        json_schema_extra=dict(xml="eParticipantAmount"),
    )
    e_pressure: Union[ePressure, str, None] = element(
        default=None, tag="ePressure", json_schema_extra=dict(xml="ePressure")
    )
    e_solvent_composition: Union[eSolventComposition, str, None] = element(
        default=None,
        tag="eSolventComposition",
        json_schema_extra=dict(xml="eSolventComposition"),
    )
    e_temperature: Union[eTemperature, str, None] = element(
        default=None, tag="eTemperature", json_schema_extra=dict(xml="eTemperature")
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/FAIRChemistry/pyThermoML"
    )
    _commit: Optional[str] = PrivateAttr(
        default="4014e57ac2f3b9b09cdefb1c3e2f2cfca298f660"
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
