import sdRDM

from typing import Dict, Optional, Union
from pydantic import PrivateAttr, model_validator
from pydantic_xml import element
from lxml.etree import _Element
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from sdRDM.tools.utils import elem2dict
from .ebiostate import eBioState
from .regnum import RegNum
from .ecrystallatticetype import eCrystalLatticeType
from .epropphase import ePropPhase


@forge_signature
class PropPhaseID(
    sdRDM.DataModel,
    nsmap={
        "": "http://www.iupac.org/namespaces/ThermoML",
        "xsi": "http://www.w3.org/2001/XMLSchema",
    },
    search_mode="unordered",
):
    """"""

    e_bio_state: Union[eBioState, str, None] = element(
        default=None, tag="eBioState", json_schema_extra=dict(xml="eBioState")
    )
    e_crystal_lattice_type: Union[eCrystalLatticeType, str, None] = element(
        default=None,
        tag="eCrystalLatticeType",
        json_schema_extra=dict(xml="eCrystalLatticeType"),
    )
    e_prop_phase: Union[ePropPhase, str, None] = element(
        default=None, tag="ePropPhase", json_schema_extra=dict(xml="ePropPhase")
    )
    n_comp_index: Optional[int] = element(
        default=None, tag="nCompIndex", json_schema_extra=dict(xml="nCompIndex")
    )
    reg_num: Optional[RegNum] = element(
        default_factory=RegNum, tag="RegNum", json_schema_extra=dict(xml="RegNum")
    )
    s_bio_state: Optional[str] = element(
        default=None, tag="sBioState", json_schema_extra=dict(xml="sBioState")
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
