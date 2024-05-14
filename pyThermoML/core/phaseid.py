import sdRDM

from typing import Dict, Optional, Union
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .regnum import RegNum
from .ephase import ePhase
from .ecrystallatticetype import eCrystalLatticeType


@forge_signature
class PhaseID(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_crystal_lattice_type: Union[eCrystalLatticeType, str, None] = element(
        default=None,
        tag="eCrystalLatticeType",
        json_schema_extra=dict(xml="eCrystalLatticeType"),
    )
    e_phase: Union[ePhase, str, None] = element(
        default=None, tag="ePhase", json_schema_extra=dict(xml="ePhase")
    )
    n_comp_index: Optional[int] = element(
        default=None, tag="nCompIndex", json_schema_extra=dict(xml="nCompIndex")
    )
    reg_num: Optional[RegNum] = element(
        default_factory=RegNum, tag="RegNum", json_schema_extra=dict(xml="RegNum")
    )
    s_phase_description: Optional[str] = element(
        default=None,
        tag="sPhaseDescription",
        json_schema_extra=dict(xml="sPhaseDescription"),
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
